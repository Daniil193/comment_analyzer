import re
import pandas as pd
from typing import Dict, List, Any


def get_urls_from_text(text: str) -> str:
    """
    Regular expression for extracting urls from comment, url not contain "your_website.com/"

    :param text: User's comment
    :return: List urls from comment
    """
    regx = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(regx, text)
    filtered_urls = [i for i in urls if "your_website.com/" not in i]
    return ' ]|[ '.join(filtered_urls)


def extract_urls(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """
    Extracting all urls from comment

    :param df: DataFrame with [comment_identifier, comment] columns
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: DataFrame with new column of extracted urls
    """
    comment_col_name = parameters["comment_col_name"]
    urls_col_name = parameters["urls_col_name"]

    df[urls_col_name] = df[comment_col_name].map(get_urls_from_text)

    return df[df[urls_col_name].str.len() > 5]
