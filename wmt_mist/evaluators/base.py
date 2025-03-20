from abc import ABC, abstractmethod

class BaseEvaluator(ABC):
    """
    Abstract base class for evaluating outputs given prompts.
    """

    @abstractmethod
    def score(self, prompts, outputs):
        """
        Evaluate outputs against prompts and return some form of results.
        """
        pass
