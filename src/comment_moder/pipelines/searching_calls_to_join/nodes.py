import functools
import pandas as pd
from typing import  Dict


def calls_to_join_by_url(urls: str, parameters: Dict) -> str:
    """
    Find urls which contain templates of calls to join -> "t.me/joinchat"

    :param urls: List of extracted urls
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: List with urls which contain templates
    """
    features_to_join = parameters["features_to_join"]
    urls_ = urls.split(' ]|[ ')
    calls = [url for feat in features_to_join for url in urls_ if feat in url]
    return ' ]|[ '.join(calls)


def find_call_to_join(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """
    Extract urls which contain calls to join

    :param df: DataFrame with [comment_identifier, comment, urls_from_comment] columns
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: DataFrame where comment has urls of calls
    """
    urls_col_name = parameters["urls_col_name"]
    calls_to_join_col_name = parameters["calls_to_join_col_name"]

    df[calls_to_join_col_name] = df[urls_col_name].map(functools.partial(calls_to_join_by_url, parameters=parameters))

    return df[df[calls_to_join_col_name].str.len() > 5]
