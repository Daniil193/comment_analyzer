from kedro.pipeline import Pipeline, node
from .nodes import find_call_to_join


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for searching calls of join to another platform

    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=find_call_to_join,
                            inputs=["urls_extracted_data", "parameters"],
                            outputs="find_calls_to_join_data",
                            name="find_calls_to_join_node"
                    )]
                         )