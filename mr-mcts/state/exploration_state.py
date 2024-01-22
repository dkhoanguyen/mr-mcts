import numpy as np

from state.abstract_state import AbstractState


class ExplorationState(AbstractState):
    def __init__(self, pose: np.ndarray, max_speed: float):
        self.pose = pose
        self.max_speed = max_speed

    def __str__(self):
        return "pose"
