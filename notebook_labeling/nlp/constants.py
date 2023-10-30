REGEX = r"(?u)[a-zA-Z]{1,}|[=[\]_]"
DEBUG_MODE = [False]
INSERT_HEADERS = [True]
VECTORIZERS = {}
CLASSIFIERS = {}

PATH_TO_MODELS = "./notebook_labeling/resources/models/"


class ACTIVITY:
    SETUP_NOTEBOOK = "setup_notebook"
    INGEST_DATA = "ingest_data"
    PROCESS_DATA = "process_data"
    TRAIN_MODEL = "train_model"
    EVALUATE_MODEL = "evaluate_model"
    TRANSFER_RESULTS = "transfer_results"
    VISUALIZE_DATA = "visualize_data"
    VALIDATE_DATA = "validate_data"


ALL_TAGS = {
    ACTIVITY.SETUP_NOTEBOOK: "setup_notebook",
    ACTIVITY.INGEST_DATA: "ingest_data",
    ACTIVITY.PROCESS_DATA: "process_data",
    ACTIVITY.TRAIN_MODEL: "train_model",
    ACTIVITY.EVALUATE_MODEL: "evaluate_model",
    ACTIVITY.TRANSFER_RESULTS: "transfer_results",
    ACTIVITY.VISUALIZE_DATA: "visualize_data",
    ACTIVITY.VALIDATE_DATA: "validate_data",
}

EXPLICIT_MODELS = {
    ACTIVITY.INGEST_DATA: "ingest_data",
    ACTIVITY.PROCESS_DATA: "process_data",
    ACTIVITY.TRAIN_MODEL: "train_model",
    ACTIVITY.EVALUATE_MODEL: "evaluate_model",
    ACTIVITY.TRANSFER_RESULTS: "transfer_results",
}


class KEYWORDS:
    VALIDATION = "VALIDATION"
    SETUP = "SETUP"
    ASSIGN = "ASSIGN"
    SLICE = "SLICE"
