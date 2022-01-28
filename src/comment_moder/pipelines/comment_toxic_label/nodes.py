import pandas as pd
from detoxify import Detoxify
from tqdm import tqdm
from typing import Dict


def get_toxic_label(df: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """
    Check if the comment contains toxicity content

    :param df: DataFrame with [comment_identifier, comment] columns
    :param parameters: Dictionary which contains info from parameters.yml file
    :return: DataFrame filtered by comment with toxic content
    """

    score_thresh = parameters["score_thresh"]
    id_col_name = parameters["id_col_name"]
    comment_col_name = parameters["comment_col_name"]
    toxic_level_col_name = parameters["toxic_level_col_name"]
    interested_toxic_label = parameters["interested_toxic_label"]
    device_for_preparing = parameters["device_for_preparing"]
    detox = Detoxify('multilingual', device=device_for_preparing)
    full_result = {'toxicity': [],
                   'severe_toxicity': [],
                   'obscene': [],
                   'identity_attack': [],
                   'insult': [],
                   'threat': [],
                   'sexual_explicit': []}

    for comment in tqdm(df[comment_col_name].values):
        results = detox.predict([comment])

        for k_res in results.keys():
            full_result[k_res].append(results[k_res][0])

    res_df = pd.DataFrame(full_result, index=df[id_col_name].values)[interested_toxic_label].reset_index()
    res_df.rename({res_df.columns[0]: id_col_name}, inplace=True, axis=1)
    res_df[toxic_level_col_name] = res_df[interested_toxic_label].sum(axis=1, numeric_only=True)

    return res_df[res_df[toxic_level_col_name] >= score_thresh]


