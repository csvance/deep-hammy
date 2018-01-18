from typing import Tuple

HammyReward = float
HammyHealth = float


class HammyCondition(object):
    def __init__(self):
        self.value = 1.

    # Returns a tuple with a reward and health modifier
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class FoodCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class DrinkCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class SleepCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class ThingsCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class AttentionCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass


class DrugsCondition(HammyCondition):
    def step(self) -> Tuple[HammyReward, HammyHealth]:
        pass
