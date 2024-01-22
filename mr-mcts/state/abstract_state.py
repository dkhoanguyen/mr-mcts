from abc import ABC, abstractmethod
import numpy as np


class AbstractState(ABC):

    @abstractmethod
    def __str__(self):
        """"""
