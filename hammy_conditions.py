from typing import Tuple


class HammyCondition(object):
    def __init__(self):
        self.value = 1.

    # Returns a tuple with a reward and health modifier
    def step(self) -> Tuple[float, float]:
        pass


class FoodCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass


class DrinkCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass


class SleepCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass


class ThingsCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass


class AttentionCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass


class DrugsCondition(HammyCondition):
    def step(self) -> Tuple[float, float]:
        pass
