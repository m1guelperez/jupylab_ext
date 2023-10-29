import re
import joblib
from pprint import pprint
import xgboost as xgb
from datetime import datetime
from notebook_labeling.nlp.utils import number_of_print_calls, debug_print
from notebook_labeling.nlp.constants import (
    HEURISTIC_NAMES_HYBRID,
    FILE_NAME_MAPPINGS,
    HEURISTIC_NAMES,
    DICT_NAMES,
)

TAG_MAPPINGS = {
    "Setup Activity": "Setup_Activity",
    "Data Ingestion": "Data_Ingestion_Activity",
    "Data Validation": "Data_Validation_Activity",
    "Data Pre-Processing": "Data_Pre_Processing_Activity",
    "Model Training": "Model_Training_Activity",
    "Model Evaluation": "Model_Evaluation_Activity",
    "Checkpoint Activity": "Checkpoint_Activity",
    "Post Development Phase": "Post_Development_Phase",
    "Data Visualization Phase": "Data_Visualization_Phase",
}

CELLS = None
CLASSIFIERS = None
VECTORIZERS = None
pattern_constants = re.compile(r"^[A-Z]{1,}(?:[_A-Z0-9]{1,})=.{1,}$")
pattern_hardcoded_constant = re.compile(r"\bCONST\b")
pattern_hardcoded_setup = re.compile(r"\bSETUP\b")


FILE_NAME_WORDS = [
    "Data Pre-Processing Activity",
    "Model Training Activity",
    "Model Evaluation Activity",
    "Data Ingestion Activity",
    "Data Validation Activity",
    "Setup Activity",
    "Checkpoint Activity",
    "Data Visualization Phase",
    "Post Development Phase",
]


# If a cell has a match for two heuristics, we can suggest to split the cell into subcells
def init_heuristics_dict(cell_count: int):
    """This function takes the number of cells and creates as many dictionaries."""
    cells = {}
    for i in range(cell_count):
        cells[i] = {
            "cell_number": i,
            "cell_type": "unknown",
            "cell_output_type": "unknown",
            "number_of_tags": "unknown",
            "activities": {
                "setup_activity": -999,
                "data_ingestion_activity": -999,
                "data_validation_activity": -999,
                "data_pre_processing_activity": -999,
                "model_training_activity": -999,
                "model_evaluation_activity": -999,
                "post_development_phase": -999,
                "checkpoint_activity": -999,
                "data_visualization_phase": -999,
            },
        }
    global CELLS
    CELLS = cells
    debug_print("Initialized dictionaries for each notebook cell.")


def load_pre_trained_models():
    global CLASSIFIERS
    global VECTORIZERS
    classifiers = {}
    vectorizers = {}
    for tag in TAG_MAPPINGS.keys():
        debug_print("Loading " + tag + " ...")
        classifier = xgb.XGBClassifier()
        classifier.load_model(
            "./notebook_labeling/resources/new_trained_models/model_"
            + TAG_MAPPINGS[tag].replace("-", "_").replace(" ", "_")
            + "_boost-"
            + "2023-10-01"
            + ".json"
        )
        classifiers[TAG_MAPPINGS[tag]] = classifier
        vectorizers[TAG_MAPPINGS[tag]] = joblib.load(
            "./notebook_labeling/resources/new_trained_models/vectorizer_"
            + TAG_MAPPINGS[tag].replace("-", "_").replace(" ", "_")
            + "_boost-"
            + "2023-10-01"
            + ".joblib"
        )

    CLASSIFIERS = classifiers
    VECTORIZERS = vectorizers


heuristic_name = [
    HEURISTIC_NAMES.CHECKPOINT_ACTIVITY,
    HEURISTIC_NAMES.DATA_INGESTION_ACTIVTIY,
    HEURISTIC_NAMES.DATA_PRE_PROCESSING_ACTIVITY,
    HEURISTIC_NAMES.DATA_VALIDATION,
    HEURISTIC_NAMES.MODEL_EVALUATION_ACTIVITY,
    HEURISTIC_NAMES.MODEL_TRAINING_ACTIVITY,
    HEURISTIC_NAMES.POST_DEVELOPMENT_PHASE,
    HEURISTIC_NAMES.SETUP_ACTIVITY,
    HEURISTIC_NAMES.DATA_VISUALIZATION_PHASE,
]

heuristic_name_hybrid = [
    HEURISTIC_NAMES_HYBRID.DATA_INGESTION_ACTIVTIY,
    HEURISTIC_NAMES_HYBRID.DATA_PRE_PROCESSING_ACTIVITY,
    HEURISTIC_NAMES_HYBRID.DATA_VALIDATION,
    HEURISTIC_NAMES_HYBRID.MODEL_EVALUATION_ACTIVITY,
    HEURISTIC_NAMES_HYBRID.MODEL_TRAINING_ACTIVITY,
    HEURISTIC_NAMES_HYBRID.POST_DEVELOPMENT_PHASE,
]


def setup_phase_heuristic_hybrid(content: str) -> int:
    if "SETUP" in content:
        return 1
    else:
        classifier = CLASSIFIERS[TAG_MAPPINGS["Setup Activity"]]
        vectorizer = VECTORIZERS[TAG_MAPPINGS["Setup Activity"]]
        vectorized_cell = vectorizer.transform([content])
        prediction = classifier.predict(vectorized_cell)
        if prediction[0] == 1:
            return 1
        else:
            return 0


def checkpoint_activity_heuristic_hybrid(content: str):
    if "CHECKPOINT" in content:
        return 1
    else:
        classifier = CLASSIFIERS[TAG_MAPPINGS["Checkpoint Activity"]]
        vectorizer = VECTORIZERS[TAG_MAPPINGS["Checkpoint Activity"]]
        vectorized_cell = vectorizer.transform([content])
        prediction = classifier.predict(vectorized_cell)
        if prediction == 1:
            return 1
        else:
            return 0


def data_visualization_heuristic_hybrid(content: str, cell_number: int):
    if CELLS[cell_number]["cell_output_type"] == "display_data":
        return 1
    else:
        classifier = CLASSIFIERS[TAG_MAPPINGS["Data Visualization Phase"]]
        vectorizer = VECTORIZERS[TAG_MAPPINGS["Data Visualization Phase"]]
        vectorized_cell = vectorizer.transform([content])
        prediction = classifier.predict(vectorized_cell)
        if prediction == 1:
            return 1
        else:
            return 0


def create_cell_properties(cell_number: int, cell: dict):
    CELLS[cell_number]["cell_type"] = cell["cell_type"]
    CELLS[cell_number]["cell_number"] = cell_number
    if "outputs" in cell and len(cell["outputs"]) > 0:
        CELLS[cell_number]["cell_output_type"] = cell["outputs"][0]["output_type"]
    else:
        CELLS[cell_number]["cell_output_type"] = "not_existent"


def machine_learning_prediction_hybrid(cell_number: int, text_as_list: list) -> int:
    sentence = " ".join(text_as_list)
    if len(text_as_list) == 0:
        return

    if setup_phase_heuristic_hybrid(sentence) == 1:
        CELLS[cell_number]["activities"].update({"setup_activity": float(1)})
    if data_visualization_heuristic_hybrid(sentence, cell_number) == 1:
        CELLS[cell_number]["activities"].update({"data_visualization_phase": float(1)})
    if checkpoint_activity_heuristic_hybrid(sentence) == 1:
        CELLS[cell_number]["activities"].update({"checkpoint_activity": float(1)})
    sentence = " ".join(text_as_list)
    for phase in heuristic_name_hybrid:
        sentence_transformed = VECTORIZERS[TAG_MAPPINGS[phase]].transform([sentence])
        prediciton = CLASSIFIERS[TAG_MAPPINGS[phase]].predict(sentence_transformed)

        if float(CELLS[cell_number]["activities"][DICT_NAMES[phase]]) < prediciton[0]:
            CELLS[cell_number]["activities"].update({DICT_NAMES[phase]: prediciton[0]})


def run_source_nlp_hybrid_heuristics(cell_number: int, cell_source: list):
    machine_learning_prediction_hybrid(cell_number, cell_source)


def get_current_heuristic_dict() -> dict:
    return CELLS


def reset_heuristics_dict():
    # When assigning a global variable to a new value we need the global keyword otherwise we create a new local variable
    global CELLS
    CELLS = {}


def particular_model_test(content: str, tag: str):
    print(content)
    classifier = xgb.XGBClassifier()
    classifier.load_model(
        "./notebook_labeling.nlp/resources/new_trained_models/model_"
        + TAG_MAPPINGS[tag].replace("-", "_").replace(" ", "_")
        + "_boost-"
        + "2023-09-30"
        + ".json"
    )
    vectorizer = joblib.load(
        "./notebook_labeling.nlp/resources/new_trained_models/vectorizer_"
        + TAG_MAPPINGS[tag].replace("-", "_").replace(" ", "_")
        + "_boost-"
        + "2023-09-30"
        + ".joblib"
    )
    prediction = classifier.predict(vectorizer.transform([content]))
    print(prediction)
