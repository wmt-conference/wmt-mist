from typing import Any, Dict, List
import tqdm
import wmt_mist.utils
from .base import BaseDataset

class TranslationDataset(BaseDataset):
    """
    Skeleton class to handle General MT dataset.
    """

    def __init__(self, dataset):
        if dataset in {"wmt24", "wmt24++", "wmt24pp"}:
            # import here to avoid importing by default
            import mt_metrics_eval.data
            import mt_metrics_eval.meta_info
            
            try:
                mt_metrics_eval.data.EvalSet("wmt24", "en-de", False)
            except FileNotFoundError:
                # run `python3 -m mt_metrics_eval.mtme --download` from here
                import subprocess
                subprocess.run(
                    ["python3", "-m", "mt_metrics_eval.mtme", "--download"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True,
                )
                
            data_all = []
            for lp in mt_metrics_eval.meta_info.DATA["wmt24pp"].keys():
                data = mt_metrics_eval.data.EvalSet("wmt24pp", lp, False)
                data_all += [
                    {
                        "source": src,
                        "lp": lp,
                    }
                    for src in data.src
                ]
        else:
            raise ValueError(f"Unknown dataset {dataset}")
        
        self.data = data_all

    
    def format_prompt(self, line: Dict[str, Any]) -> str:
        lang1, lang2 = line["lp"].split("-")
        line["lang1"] = wmt_mist.utils.get_language_name(lang1)
        line["lang2"] = wmt_mist.utils.get_language_name(lang2)

        return "Translate \'\'\'{source}\'\'\' from {lang1} to {lang2}. Output only the translation and nothing else.".format(**line)


    def dump_data(self) -> List[Dict[str, Any]]:
        return [
            self.format_prompt(line)
            for line in self.data
        ]
