from kedro.pipeline import Pipeline, node
from .nodes import search_crypto_wallet


def create_pipeline(**kwargs):
    """
    Initial part of pipeline for searching cryptocurrency wallets

    :param kwargs:
    :return:
    """
    return Pipeline([node(
                            func=search_crypto_wallet,
                            inputs=["preprocessed_input_data", "parameters"],
                            outputs="find_wallet_data",
                            name="find_wallets_node"
                    )]
                         )