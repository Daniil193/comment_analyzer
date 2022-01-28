from kedro.pipeline import Pipeline, node
from .nodes import info_aggregation


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for search toxicity comments
    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=info_aggregation,
                            inputs=["preprocessed_input_data",
                                    "find_wallet_data",
                                    "find_calls_to_join_data",
                                    "toxic_labeled_data",
                                    "urls_extracted_data",
                                    "parameters"],
                            outputs="aggregated_data",
                            name="aggregated_data_node"
                    )]
                         )
