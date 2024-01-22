import numpy as np

from actions.abstract_action import AbstractAction
from state.exploration_state import ExplorationState


class RandomWalkAction(AbstractAction):
    def __init__(self, angle: float, displacement: float):
        # Parameters
        self.angle = angle
        self.displacement = displacement

    def get_cost(self, initial_state: ExplorationState) -> float:
        """
        Get the cost of performing the action at the given state. The cost here is 
        defined as the time required to traverse between the initial state to the 
        end state at the maximum speed of the robot.
        """
        return self.displacement / initial_state.max_speed

    def perform(self, initial_state: ExplorationState) -> ExplorationState:
        """
        Perform the action at the given state and return the end state
        """
        return self._perform_random_walk(displacement=self.displacement,
                                         angle=self.angle,
                                         start=initial_state)

    def _perform_random_walk(self, displacement: float,
                             angle: float, start: ExplorationState) -> ExplorationState:
        """
        Apply a random walk with a given displacement and angle to the given state
        and return the end state after the action
        """
        start_pos = start.pose
        # Assume an omnidirectional robot
        end_pos = start_pos + \
            np.array([displacement*np.cos(angle),
                     displacement*np.sin(angle), 0])
        end_pose = ExplorationState(pose=end_pos, max_speed=start.max_speed)
        return end_pose
