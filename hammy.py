from enum import Enum, unique
import numpy as np
from hammy_conditions import *
from collections import deque
import random


@unique
class Needs(Enum):
    HUNGRY = 0
    THIRSTY = 1
    SLEEPY = 2
    ATTENTION = 3


@unique
class Action(Enum):
    HUNGRY = 0
    THIRSTY = 1
    SLEEPY = 2
    ATTENTION = 3
    NONE = 4


class Experience(object):
    def __init__(self, original_state, action: Action, next_state, reward: float, terminal: bool = False):
        self.original_state = original_state
        self.action = action
        self.next_state = next_state
        self.reward = reward
        self.terminal = terminal


class ExperienceReplay(object):
    def __init__(self):
        self.buffer = deque(maxlen=1000)

    def sample(self, batch_size=32):
        if len(self.buffer) < batch_size:
            return []
        return random.sample(self.buffer, batch_size)

    def store(self, experience: Experience):
        self.buffer.append(experience)


class Hammy(object):
    def __init__(self):
        self.e = ExperienceReplay()

        self.conditions = {}
        self._init_conditions()

        self.health = 1.
        self.age = 0.
        self.cod = None

    def _init_conditions(self):
        self.conditions[Needs.HUNGRY] = FoodCondition()
        self.conditions[Needs.THIRSTY] = DrinkCondition()
        self.conditions[Needs.SLEEPY] = SleepCondition()
        self.conditions[Needs.ATTENTION] = AttentionCondition()

    def reset(self):
        self.age = 0.
        self.health = 1.

        for key in self.conditions:
            self.conditions[key].reset()

    def action(self, action: Action):

        r = 0.
        h = 0.

        old_state = self.state()

        if action.value == Action.NONE.value:
            for key in self.conditions:
                _r, _h = self.conditions[key].skip()
                r += _r
                h += _h

                if self.health + h <= 0.:
                    self.cod = self.conditions[key].cod_message_skip()
        else:
            r, h = self.conditions[Needs(action.value)].act()
            if self.health + h <= 0.:
                self.cod = self.conditions[Needs(action.value)].cod_message_act()

        # Apply new health values
        self.health += h

        new_state = self.state()

        if self.health > 0.:
            self.e.store(Experience(original_state=old_state, action=action, next_state=new_state, reward=r))
            self.age += 1
            return True
        else:
            self.e.store(
                Experience(original_state=old_state, action=action, next_state=new_state, reward=-1., terminal=True))
            return False

    def state(self) -> list:

        conditions = [self.conditions[Needs.HUNGRY].level, self.conditions[Needs.THIRSTY].level,
                      self.conditions[Needs.SLEEPY].level, self.conditions[Needs.ATTENTION].level]

        return [np.array([conditions]), np.array([self.health])]
