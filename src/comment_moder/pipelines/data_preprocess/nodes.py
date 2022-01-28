import pandas as pd
from typing import Dict


def preprocess_dataset(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """
    Drop NA-values by column with comments and typing it to string

    :param df: DataFrame with [comment_identifier, comment] columns
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: Prepared DataFrame
    """

    comment_col_name = parameters["comment_col_name"]
    id_col_name = parameters["id_col_name"]

    df = df[[comment_col_name, id_col_name]]
    df.dropna(subset=[comment_col_name], inplace=True)
    df[comment_col_name] = df[comment_col_name].astype(str)

    return df
