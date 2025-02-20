import json
from .base_dataset import BaseDataset

class GeneralMTDataset(BaseDataset):
    """
    Skeleton class to handle General MT dataset.
    """

    def __init__(self, config=None):
        self.config = config
        self.data = None  # place to store data once loaded

    def load_data(self):
        # TODO: Actually load data
        self.data = [
            {"id": "mt_1", "prompt": "Translate into Czech: 'Hello, world!'"},
            {"id": "reasoning_1", "prompt": "What is 1+1? Reason step by step, separate answer with ==="},
            {"id": "generation_1", "prompt": "Summarize in a single Czech word: 'Once in a blue moon'"}
        ]

    def get_prompts(self):
        return self.data
