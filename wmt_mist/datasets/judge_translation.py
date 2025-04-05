from typing import Any, Dict, List
import tqdm
import wmt_mist.utils
from .base import BaseDataset

class JudgeTranslationDataset(BaseDataset):
    """
    Skeleton class to handle General MT dataset.
    """

    def __init__(self, dataset):
        if dataset in {"wmt24pp", "wmt24++"}:
            # import here to avoid importing by default

            # TODO: use the dataset for which we have human scores: https://github.com/google-research/mt-metrics-eval/tree/main?tab=readme-ov-file#wmt24-data
            import datasets
            datasets.logging.disable_progress_bar()
            data = []
            for config in tqdm.tqdm(datasets.get_dataset_config_names("google/wmt24pp"), desc="Loading WMT24++ dataset"):
                data += list(datasets.load_dataset("google/wmt24pp", config, split="train"))
        else:
            raise ValueError(f"Unknown dataset {dataset}")
        
        self.data = [
            self.format_prompt(line)
            for line in data
        ]

    
    def format_prompt(self, line: Dict[str, Any]) -> str:
        lang1, lang2 = line["lp"].split("-")
        line["lang1"] = wmt_mist.utils.get_language_name(lang1)
        line["lang2"] = wmt_mist.utils.get_language_name(lang2)

        return "Consider this source \'\'\'{source}\'\'\' in {lang1} and this translation \'\'\'{target}\'\'\' in {lang2}. Assess the translation quality from 0% to 100%.".format(**line)


    def dump_data(self) -> List[Dict[str, Any]]:
        return self.data
