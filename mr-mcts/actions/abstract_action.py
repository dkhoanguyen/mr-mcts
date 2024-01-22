from abc import ABC, abstractmethod
from state.abstract_state import AbstractState

class AbstractAction(ABC):
    @abstractmethod
    def get_cost(self, initial_state: AbstractState) -> float:
        """
        Get the cost of performing the action at the given state
        """

    @abstractmethod
    def perform(self, initial_state: AbstractState) -> AbstractState:
        """
        Perform the action at the given state and return the end state
        """ 

