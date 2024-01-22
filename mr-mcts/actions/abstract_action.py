from abc import ABC, abstractmethod
from state.abstract_state import AbstractState

class AbstractAction(ABC):
    @abstractmethod
    def is_feasible(self, state: AbstractState) -> bool:
        """
        Return whether the action is feasible given the current state
        """

    @abstractmethod
    def simulate(self, initial_state: AbstractState) -> AbstractState: 
        """
        Perform simulation with the action at the given state and return the end state
        """

    @abstractmethod
    def get_cost(self, initial_state: AbstractState) -> float:
        """
        Get the cost of performing the action at the given state
        """

    @abstractmethod
    def get_final_state(self) -> AbstractState:
        """
        Get the final state after performing the action
        """
    