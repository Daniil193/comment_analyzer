"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from comment_moder.pipelines import data_preprocess as dp
from comment_moder.pipelines import comment_toxic_label as toxic_e
from comment_moder.pipelines import url_extract as url_e
from comment_moder.pipelines import searching_calls_to_join as search_ctj
from comment_moder.pipelines import searching_crypto_wallet as search_wlt
from comment_moder.pipelines import aggregate_comment_info as agg_info


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_preprocessing_pipeline = dp.create_pipeline()
    toxic_extractor_pipeline = toxic_e.create_pipeline()
    urls_extractor_pipeline = url_e.create_pipeline()
    search_calls_to_join_pipeline = search_ctj.create_pipeline()
    search_wallets_pipeline = search_wlt.create_pipeline()
    aggregation_info_pipeline = agg_info.create_pipeline()

    return {"__default__": data_preprocessing_pipeline +
                           toxic_extractor_pipeline +
                           urls_extractor_pipeline +
                           search_calls_to_join_pipeline +
                           search_wallets_pipeline +
                           aggregation_info_pipeline,
            "dp": data_preprocessing_pipeline,
            "toxic_e": toxic_extractor_pipeline,
            "url_e": urls_extractor_pipeline,
            "search_ctj": search_calls_to_join_pipeline,
            "search_wlt": search_wallets_pipeline,
            "agg_info": aggregation_info_pipeline
            }
