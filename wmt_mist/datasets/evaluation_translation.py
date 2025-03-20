import sys
from typing import Any, Dict, List
from .base import BaseDataset

class EvaluationTranslationDataset(BaseDataset):
    """
    Skeleton class to handle General MT dataset.
    """
    # import hidden in the class such that it's not impoted by default
    import subset2evaluate.utils

    def __init__(self, year, split):
        print("Loading translation data, might take a while", file=sys.stderr)

        year = {
            ("2025", "dev"): "wmt24",
        }[(year, split)]

        data = self.subset2evaluate.utils.load_data_wmt_all()
        # collect all langauges from the particular year
        data = [(data_name, data) for data_name, data in data.items() if data_name[0].split(".")[0] == year]
        data_new = []
        for data_name, data in data:
            lang1, lang2 = data_name[1].split("-")
            for line in data:
                # collect source and all translations
                for model, tgt in line["tgt"].items():
                    data_new.append({
                        "prompt": f'Given this source \'\'\'{line["src"]}\'\'\' in {lang1} and translation \'\'\'{tgt}\'\'\' in {lang2}, assign a score to the translation on a scale from 0 to 100. Output only the score and nothing else.',
                    })
        self.data = data_new

    def dump_data(self) -> List[Dict[str, Any]]:
        return self.data
