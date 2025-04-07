from typing import Any, Dict, List
from abc import ABC, abstractmethod

class BaseDataset(ABC):
    """
    Base class for dataset handling. 
    """

    @abstractmethod
    def dump_data(self) -> List[Dict[str, Any]]:
        """
        Returns a list (or dict) of prompts in a consistent format.
        """
        pass