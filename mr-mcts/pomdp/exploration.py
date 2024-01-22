from typing import Dict
import numpy as np

from ..actions.abstract_action import AbstractAction
from ..actions.random_walk_action import RandomWalkAction
from ..state.abstract_state import AbstractState
from ..state.exploration_state import ExplorationState
from pomdp.abstract_mdp import AbstractMDP


class Exploration(AbstractMDP):
    """
    This class describes the MDP of an exploration problem. It has 2 types of actions (for now):
    - Random walk: Perform a random walk from the current state with a set displacement and angle
    - Frontier cluster: Move towards the closest cluster of frontier cells.
    """

    def __init__(self,
                 random_displacement_factor: int,
                 frontier_branching_factor: int,
                 random_displacement_length: float,
                 random_max_angle: float,
                 random_spread_angle: float):

        self._random_displacement_factor = random_displacement_factor
        self._frontier_branching_factor = frontier_branching_factor

        self._random_displacement_length = random_displacement_length
        self._random_max_angle = random_max_angle
        self._random_spread_angle = random_spread_angle

    def get_potential_feasible_actions(self, state: AbstractState) -> Dict[str, AbstractAction]:
        """
        """
        feasible_actions: Dict[str, AbstractAction] = dict()
        # Sample random walks
        sampled_angles = self._sample_displacement_angles(
            self._random_spread_angle, self._random_displacement_factor)
        sampled_random_walks = self._sample_random_walk(
            initial_state=state, sampled_angles=sampled_angles,
            displacement=self._random_displacement_length)
        # Verify all sampled random walks and remove unfeasible ones
        for angle,random_walk in sampled_random_walks:
            if not self._check_feasibility(random_walk=random_walk):
                del sampled_random_walks[angle]
        feasible_actions = sampled_random_walks
        return feasible_actions

    def _sample_displacement_angles(self, spread_angle: float, num: int) -> np.ndarray:
        """
        Return randomly sampled displacement angles from the given spread angle uniformly.
        For example, if the spread angle is 100 degree, then a 0 degree sampled angle 
        would mean that the robot moves forward. a 30 degree sampled angle would mean 
        the robot turns left 30 degrees and -40 means turning right 40 degree.

        It is also possible to modify the distribution to bias the process towards a 
        specific behavior. For example, a normal distribution would cause the sampled angle
        to be biased towards the previously direction

        For now, the distribution is a uniform distribution.
        """
        lower_bound = -spread_angle / 2
        upper_bound = spread_angle / 2
        return np.random.uniform(lower_bound, upper_bound, num)

    def _sample_random_walk(self, initial_state: ExplorationState,
                            sampled_angles: np.ndarray,
                            displacement: float) -> Dict[str, RandomWalkAction]:
        random_walk: Dict[str,RandomWalkAction] = {}
        offset_angle = initial_state.pose[2]
        for i in range(sampled_angles.shape[0]):
            sampled_angle = sampled_angles[i] + offset_angle
            random_walk.update({str(sampled_angles[i]),RandomWalkAction(angle=sampled_angle,
                                                displacement=displacement)})
        return random_walk
    
    def _check_feasibility(self, random_walk: RandomWalkAction) -> bool:
        """
        Check if the given walk is feasible
        Conditions for rejection are:
        - The path connecting between the initial state and end state collides with obstacles
        """
        return True
