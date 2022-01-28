from kedro.pipeline import Pipeline, node
from .nodes import get_toxic_label


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for search toxicity comments

    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=get_toxic_label,
                            inputs=["preprocessed_input_data", "parameters"],
                            outputs="toxic_labeled_data",
                            name="toxic_label_node"
                    )]
                         )