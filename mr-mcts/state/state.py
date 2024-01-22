import numpy as np

from state.abstract_state import AbstractState


class State(AbstractState):
    def __init__(self, pos: np.ndarray, diameter: float):
        self.pos = pos
        self.diameter = diameter
