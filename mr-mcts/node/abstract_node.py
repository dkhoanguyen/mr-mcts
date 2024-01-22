from typing import List, Dict
from abc import ABC, abstractmethod

import numpy as np

from actions.abstract_action import AbstractAction
from state.abstract_state import AbstractState


class AbstractNode(ABC):
    """
    Abstract class to represent a simple node in MCTS. The class must be extended to describe
    more complex node structures (for example, node with discounted values, etc). 
    """

    def __init__(self,
                 parent,
                 end_state: AbstractState,
                 action: AbstractAction):
        """
        Args:
            `parent` (AbstractNode | None): the parent node of this node. For root node, set this value
                                          `None`
            `end_state` (AbstractState): the END STATE associated with this node
            `action` (AbstractAction): the action associated with this node
        """
        self._parent: AbstractNode = parent
        self._action: AbstractNode = action
        self._end_state: AbstractState = end_state

        self._potential_children: Dict[str, AbstractAction] = []
        self._children: List[AbstractNode] = []

        self._num_visit: int = 0
        self._value: float = 0.0

    @abstractmethod
    def get_value(self) -> float:
        """
        Return the overall value of this node. This method needs to be overridden to describe
        more sophisticated value evaluation strategies, for example UCT or discounted UCT.
        """

    def add_visit(self, value: float):
        self._num_visit += 1
        self._value += value

    def is_root(self) -> bool:
        """
        Return whether a node is a root node of the tree
        """
        return self._parent is None

    def is_expandable(self) -> bool:
        """
        Check to see if the current node has any unexpanded children, in order word, any 
        action that has not been simulated and added to the children list of the current
        node
        """
        return len(self._potential_children) > 0

    def _prune_infeasible_children(self,
                                   potential_children: Dict[str, AbstractAction]):
        for name, action in potential_children.items():
            if not action.is_feasible():
                del potential_children[name]
        return potential_children
