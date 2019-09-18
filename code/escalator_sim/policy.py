"""
Different Policies of how individuals move through the escalator
"""
from abc import ABC
from abc import abstractmethod

class Policy(ABC):

    @abstractmethod
    def get_lane(self):
        """
        :return: Left or Right (Walking vs Standing) Lane selected
        """
        pass

    @abstractmethod
    def advance_amount(self, lane_steps):
        """
        :return: For the given policy, returns amount of spots to advance
        """
        pass


class Standers(Policy):

    def __init__(self, proportion_evil =0):
        self.proportion_evil = proportion_evil

    def get_lane(self):
        """Returns Right for most. It will set proportion of of the standers to
         stand in the walking lane as evil individuals"""

        pass

    def advance_amount(self, lane_steps):
        """Always returns 1, they aren't walking"""
        return 1


class Walkers(Policy):

    def __init__(self, stairs_between):
        self.stairs_between = stairs_between
        pass

    def get_lane(self):
        """Return left for walking"""
        return "left"

    def advance_amount(self, lane_steps):
        """calculates how many steps they can advance based upon the occupancy of the lane
        and how the stairs_between"""

        pass