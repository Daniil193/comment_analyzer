import pandas as pd
from typing import Dict, List


def info_aggregation(df_base: pd.DataFrame,
                     wallet_df: pd.DataFrame,
                     calls_df: pd.DataFrame,
                     toxic_df: pd.DataFrame,
                     urls_df: pd.DataFrame,
                     parameters: Dict) -> pd.DataFrame:
    """
    Aggregate info from all extracted data

    :param df_base: initial
    :param wallet_df: with info about cryptocurrency wallet
    :param calls_df: with info about calls to join
    :param toxic_df: with info about toxicity level of comment
    :param urls_df: with info about urls from other platform
    :param parameters: from parameters.yml
    :return: aggregated df
    """
    id_col_name = parameters["id_col_name"]
    wallet_address_col_name = parameters["wallet_address_col_name"]
    toxic_level_col_name = parameters["toxic_level_col_name"]
    urls_col_name = parameters["urls_col_name"]
    calls_to_join_col_name = parameters["calls_to_join_col_name"]

    wallet_mapper = dict(wallet_df[[id_col_name, wallet_address_col_name]].values)
    calls_mapper = dict(calls_df[[id_col_name, calls_to_join_col_name]].values)
    toxic_mapper = dict(toxic_df[[id_col_name, toxic_level_col_name]].values)
    urls_mapper = dict(urls_df[[id_col_name, urls_col_name]].values)

    df_base[wallet_address_col_name] = df_base[id_col_name].map(wallet_mapper)
    df_base[calls_to_join_col_name] = df_base[id_col_name].map(calls_mapper)
    df_base[toxic_level_col_name] = df_base[id_col_name].map(toxic_mapper)
    df_base[urls_col_name] = df_base[id_col_name].map(urls_mapper)

    return df_base.dropna(subset=[wallet_address_col_name,
                                  calls_to_join_col_name,
                                  toxic_level_col_name,
                                  urls_col_name], how="all")


