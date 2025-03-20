from abc import ABC, abstractmethod

class BaseDataset(ABC):
    """
    Abstract base class for dataset handling. 
    """

    @abstractmethod
    def load_data(self):
        """
        Loads the dataset into memory or sets up access. 
        """
        pass

    @abstractmethod
    def get_prompts(self):
        """
        Returns a list (or dict) of prompts in a consistent format.
        """
        pass
