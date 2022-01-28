from kedro.pipeline import Pipeline, node
from .nodes import extract_urls


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for extracting urls from comments, that not contain tradingview.com domain name

    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=extract_urls,
                            inputs=["preprocessed_input_data", "parameters"],
                            outputs="urls_extracted_data",
                            name="extract_urls_node"
                    )]
                         )