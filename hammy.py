from enum import Enum, unique
from hammy_conditions import *


@unique
class HammyEmotion(Enum):
    # 🤔
    NEUTRAL = 0
    # 😃
    HAPPY = 1
    # 🔥👌👪
    LITAF = 2
    # 😭
    SAD = 3
    # 🤬
    ANGRY = 4
    # 😫
    WEAK = 5


@unique
class HammyNeeds(object):
    # Hunger is a natural need
    HUNGRY = 0
    # Thirst is a natural need
    THIRSTY = 1
    # Sleep is a natural need
    SLEEPY = 2
    # Things are a learned need
    THINGS = 3
    # Attention is a learned need
    ATTENTION = 4
    # Drugs are a learned need
    DRUGS = 5


HammyReward = float


class Hammy(object):
    def __init__(self):
        self.needs = {}
        self._init_needs()

        self.conditions = {}
        self._init_conditions()

        self.health = 1.

        self.emotion = HammyEmotion.NEUTRAL

    def _init_needs(self):
        self.needs[HammyNeeds.HUNGRY] = 0.
        self.needs[HammyNeeds.THIRSTY] = 0.
        self.needs[HammyNeeds.SLEEPY] = 0.
        self.needs[HammyNeeds.THINGS] = 0.
        self.needs[HammyNeeds.ATTENTION] = 0.
        self.needs[HammyNeeds.DRUGS] = 0.

    def _init_conditions(self):
        self.conditions[HammyNeeds.HUNGRY] = FoodCondition()
        self.conditions[HammyNeeds.THIRSTY] = DrinkCondition()
        self.conditions[HammyNeeds.SLEEPY] = SleepCondition()
        self.conditions[HammyNeeds.THINGS] = ThingsCondition()
        self.conditions[HammyNeeds.ATTENTION] = AttentionCondition()
        self.conditions[HammyNeeds.DRUGS] = DrugsCondition()

    def action(self, need: HammyNeeds) -> HammyReward:
        reward = 0.

        for key in self.conditions:
            r, h = self.conditions[key].step()
            reward += r
            self.health += h

        if need == HammyNeeds.HUNGRY:
            pass
        elif need == HammyNeeds.THIRSTY:
            pass
        elif need == HammyNeeds.SLEEPY:
            pass
        elif need == HammyNeeds.THINGS:
            pass
        elif need == HammyNeeds.ATTENTION:
            pass
        elif need == HammyNeeds.DRUGS:
            pass

        return reward
