import copy
from notebook_labeling.nlp.constants import (
    DEBUG_MODE,
    INSERT_HEADERS,
)
from notebook_labeling.nlp.heuristics import (
    get_current_heuristic_dict,
    init_heuristics_dict,
    reset_heuristics_dict,
    create_cell_properties,
    run_source_nlp_hybrid_heuristics,
)
from notebook_labeling.nlp.utils import (
    make_labels,
    preprocess_source_cell_nlp,
    debug_print,
    load_pre_trained_models,
)


def pre_process_notebook_nlp(notebook: dict):
    debug_print("Starting to pre-process notebook.\nInitializing heuristics...")
    init_heuristics_dict(len(notebook["cells"]))
    debug_print("Finished initializing heuristics.\nCleaning notebook from newlines...")
    for cell_number, cell in enumerate(notebook["cells"]):
        create_cell_properties(cell_number, cell)
        cell["cell_number"] = cell_number
        if cell["cell_type"] == "code":
            if len(cell["source"]) > 0:
                cell["source_old"] = cell["source"]
                cell["source"] = preprocess_source_cell_nlp(cell["source"])
        debug_print("Finished cleaning notebook from newlines.")


# Creates a dict with heuristics for each cell and returns the result after we replied the heuristics on the notebook
def analyze_notebook_nlp_hybrid(preprocessed_notebook: dict):
    """Applies the nlp hybrid based solution and will only consider the source code of a cell."""
    for cell_number, cell in enumerate(preprocessed_notebook["cells"]):
        if cell["cell_type"] == "code":
            if len(cell["source"]) > 0:
                run_source_nlp_hybrid_heuristics(cell_number, cell["source"])
    debug_print("Finished applying all heuristics on each cell.")


def post_process_notebook_nlp(original_notebook: dict):
    """Creates the labeling of the cells."""
    debug_print("Starting post-processing...\nStarting to create labels...")
    heuristics_dict = get_current_heuristic_dict()
    make_labels(heuristics_dict, original_notebook)
    # original_notebook["metadata"]["celltoolbar"] = "Tags"
    if DEBUG_MODE[0]:
        debug_print("Finished creating labels.\nSaving notebook to disk...")
    print("Finished creating labels.\n")


def start_pipeline_hybrid(notebook: dict, debug_mode: bool, headers: bool):
    """Starts the pipeline for nlp based solution."""
    load_pre_trained_models()
    DEBUG_MODE[0] = debug_mode
    INSERT_HEADERS[0] = headers
    original_notebook = copy.deepcopy(notebook)
    debug_print("Starting pipeline for notebook: ")
    # Python passes dicts by reference therefore we do not need to save the result to a new variable
    pre_process_notebook_nlp(notebook)
    analyze_notebook_nlp_hybrid(notebook)
    post_process_notebook_nlp(original_notebook)
    reset_heuristics_dict()
    return original_notebook