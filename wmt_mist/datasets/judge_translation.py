from typing import Any, Dict, List
import wmt_mist.utils
from .base import BaseDataset

class JudgeTranslationDataset(BaseDataset):
    """
    Skeleton class to handle General MT dataset.
    """

    def __init__(self, task):
        if task in {"wmt24metrics"}:
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
            task = task.removesuffix("metrics")
            for lp in mt_metrics_eval.meta_info.DATA[task].keys():
                data = mt_metrics_eval.data.EvalSet(task, lp, False)
                if "esa" not in data.human_score_names:
                    continue
                scores = data.Scores("seg", "esa")
                for sys, sys_v in data.sys_outputs.items():
                    data_all += [
                        {
                            "source": src,
                            "target": mt,
                            "lp": lp,
                            "system": sys,
                            "score": score,
                        }
                        for src, mt, score in zip(data.src, sys_v, scores[sys])
                    ]
                data_all = [x for x in data_all if x["score"] is not None]
        else:
            raise ValueError(f"Unknown dataset/task {task}")
        
        self.data = data_all
        self.task = task

    
    def format_prompt(self, line: Dict[str, Any]) -> str:
        lang1, lang2 = line["lp"].split("-")
        line["lang1"] = wmt_mist.utils.get_language_name(lang1)
        line["lang2"] = wmt_mist.utils.get_language_name(lang2)

        return {
            "prompt": "Consider this source \'\'\'{source}\'\'\' in {lang1} and this translation \'\'\'{target}\'\'\' in {lang2}. Assess the translation quality from 0% to 100%.".format(**line),
            "task": self.task,
        }


    def dump_data(self) -> List[Dict[str, Any]]:
        return [
            self.format_prompt(x)
            for x in self.data
        ]
