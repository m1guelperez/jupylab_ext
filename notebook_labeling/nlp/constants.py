DEBUG_MODE = [True]
INSERT_HEADERS = [True]


# Phases and activities
class ACTIVITIY:
    DATA_INGESTION_ACTIVITY = "Data Ingestion"
    DATA_VALIDATION_ACTIVIY = "Data Validation"
    DATA_PRE_PROCESSING_ACTIVITY = "Data Pre-Processing"
    MODEL_TRAINING_ACTIVITY = "Model Training"
    MODEL_EVALUATION_ACTIVITY = "Model Evaluation"
    CHECKPOINT_ACTIVITY = "Checkpoint Activity"
    SETUP_ACTIVITY = "Setup Activity"


class PHASE:
    POST_DEVELOPMENT_PHASE = "Post Development Phase"
    DATA_VISUALIZATION_PHASE = "Data Visualization Phase"


class HEURISTIC_NAMES:
    SETUP_ACTIVITY = "setup_activity"
    DATA_INGESTION_ACTIVTIY = "data_ingestion_activity"
    DATA_VALIDATION = "data_validation_activity"
    DATA_PRE_PROCESSING_ACTIVITY = "data_pre_processing_activity"
    MODEL_TRAINING_ACTIVITY = "model_training_activity"
    MODEL_EVALUATION_ACTIVITY = "model_evaluation_activity"
    CHECKPOINT_ACTIVITY = "checkpoint_activity"
    POST_DEVELOPMENT_PHASE = "post_development_phase"
    DATA_VISUALIZATION_PHASE = "data_visualization_phase"


class HEURISTIC_NAMES_HYBRID:
    SETUP_ACTIVITY = "Setup Activity"
    DATA_INGESTION_ACTIVTIY = "Data Ingestion"
    DATA_VALIDATION = "Data Validation"
    DATA_PRE_PROCESSING_ACTIVITY = "Data Pre-Processing"
    MODEL_TRAINING_ACTIVITY = "Model Training"
    MODEL_EVALUATION_ACTIVITY = "Model Evaluation"
    CHECKPOINT_ACTIVITY = "Checkpoint Activity"
    POST_DEVELOPMENT_PHASE = "Post Development Phase"
    DATA_VISUALIZATION_PHASE = "Data Visualization Phase"


DICT_NAMES = {
    "Setup Activity": "setup_activity",
    "Data Ingestion": "data_ingestion_activity",
    "Data Validation": "data_validation_activity",
    "Data Pre-Processing": "data_pre_processing_activity",
    "Model Training": "model_training_activity",
    "Model Evaluation": "model_evaluation_activity",
    "Checkpoint Activity": "checkpoint_activity",
    "Post Development Phase": "post_development_phase",
    "Data Visualization Phase": "data_visualization_phase",
}

# LookUp Table for labeling:
LABELS = {
    "setup_activity": ACTIVITIY.SETUP_ACTIVITY,
    "data_ingestion_activity": ACTIVITIY.DATA_INGESTION_ACTIVITY,
    "data_validation_activity": ACTIVITIY.DATA_VALIDATION_ACTIVIY,
    "data_pre_processing_activity": ACTIVITIY.DATA_PRE_PROCESSING_ACTIVITY,
    "model_training_activity": ACTIVITIY.MODEL_TRAINING_ACTIVITY,
    "model_evaluation_activity": ACTIVITIY.MODEL_EVALUATION_ACTIVITY,
    "checkpoint_activity": ACTIVITIY.CHECKPOINT_ACTIVITY,
    "post_development_phase": PHASE.POST_DEVELOPMENT_PHASE,
    "data_visualization_phase": PHASE.DATA_VISUALIZATION_PHASE,
}

FILE_NAME_MAPPINGS = {
    "setup_activity": "Setup_Activity",
    "data_ingestion_activity": "Data_Ingestion_Activity",
    "data_validation_activity": "Data_Validation_Activity",
    "data_pre_processing_activity": "Data_Pre_Processing_Activity",
    "model_training_activity": "Model_Training_Activity",
    "model_evaluation_activity": "Model_Evaluation_Activity",
    "checkpoint_activity": "Checkpoint_Activity",
    "post_development_phase": "Post_Development_Phase",
    "data_visualization_phase": "Data_Visualization_Phase",
}
