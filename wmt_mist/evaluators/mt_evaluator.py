import pandas as pd

import json
from .base_evaluator import BaseEvaluator

class MTEvaluator(BaseEvaluator):
    """
    Evaluator for machine translation
    """

    def __init__(self, config=None):
        self.config = config

    def score(self, prompts, outputs):
        """
        - `prompts`: list of prompt dicts
        - `outputs`: list of output dicts or a single dict with answers
        - Perform minimal checks: e.g., line count vs. prompt count
        - Return a skeleton result that can be expanded later.
        """

        # Basic validation: number of prompts vs. outputs
        if len(prompts) != len(outputs):
            print(f"Warning: mismatch between prompts ({len(prompts)}) and outputs ({len(outputs)})")

        results = {}

        # dummy answers
        results["MODEL"] = {
            "aggregate": 67.4,
            "translation": 38.2,
            "reasoning": 71.0,
            "generation": 89.6
        }
        
        results["Aya Expanse"] = {
            "aggregate": 69.3,
            "translation": 42.1,
            "reasoning": 74.5,
            "generation": 88.1
        }
        
        results["Llama 7B"] = {
            "aggregate": 65.1,
            "translation": 34.9,
            "reasoning": 75.6,
            "generation": 84.8
        }

        df = pd.DataFrame(results).T
        df = df.sort_values("aggregate", ascending=False)
        return df
