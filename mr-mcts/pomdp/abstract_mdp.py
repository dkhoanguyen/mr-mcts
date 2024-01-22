from abc import ABC, abstractmethod

from typing import Dict

from state.abstract_state import AbstractState
from actions.abstract_action import AbstractAction


class AbstractMDP(ABC):
    @abstractmethod
    def get_potential_feasible_actions(self, state: AbstractState) -> Dict[str, AbstractAction]:
        """
        Get all possible feasible actions from the given state
        """

    @abstractmethod
    def simulate(self, state: AbstractState, action: AbstractAction) -> AbstractState:
        """
        Perform the given action on the given state and return the end state
        """

    @abstractmethod
    def get_reward(self, state: AbstractState, action: AbstractAction) -> float:
        """
        Return the reward for executing the action from an initial state
        """

    @abstractmethod
    def is_feasible(self, state: AbstractState, action: AbstractAction) -> bool:
        """
        Return whether the action is feasible given the current state
        """

