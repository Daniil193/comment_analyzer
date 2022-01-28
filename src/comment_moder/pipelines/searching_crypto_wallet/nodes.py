import re
import pandas as pd
from typing import Dict, List


def search_hash_address_wallet(comment: str) -> str:
    """
    Regular expression for search 3 types of hash-addresses

    :param comment: User comment
    :return: List found wallets
    """
    regx = r"0x[a-fA-F0-9]{40}|[13][a-km-zA-HJ-NP-Z1-9]{25,34}|X[1-9A-HJ-NP-Za-km-z]{33}|4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}"
    wallets = re.findall(regx, comment)
    return ' ]|[ '.join(wallets)


def search_crypto_wallet(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """
    Search crypto-wallets in comment

    :param df: DataFrame with [comment_identifier, comment] columns
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: DataFrame where comment has a crypto wallet
    """
    comment_col_name = parameters["comment_col_name"]
    wallet_address_col_name = parameters["wallet_address_col_name"]

    df[wallet_address_col_name] = df[comment_col_name].map(search_hash_address_wallet)

    return df[df[wallet_address_col_name].str.len() > 5]


