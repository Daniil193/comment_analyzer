from kedro.pipeline import Pipeline, node
from .nodes import preprocess_dataset


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for dataset preprocessing

    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=preprocess_dataset,
                            inputs=["input_data", "parameters"],
                            outputs="preprocessed_input_data",
                            name="preprocessing_input_data_node"
                    )]
                         )
