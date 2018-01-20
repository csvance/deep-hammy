from typing import Tuple

HammyReward = float
HammyHealth = float

MAX_LEVEL = 5.


class HammyCondition(object):
    def __init__(self):
        self.level = 1.

    def skip(self) -> Tuple[HammyReward, HammyHealth]:
        self.level -= 0.1

        if self.level < 0.:
            return -0.1, -0.01

        return 0., 0.

    def act(self) -> Tuple[HammyReward, HammyHealth]:
        self.level += 1.

        if self.level > MAX_LEVEL:
            return 0., -0.1

        return 1., 0.0

    def reset(self):
        self.level = 1.

    def cod_message_act(self) -> str:
        raise NotImplementedError

    def cod_message_skip(self) -> str:
        raise NotImplementedError


class FoodCondition(HammyCondition):
    def cod_message_act(self) -> str:
        return "Exploded from eating too much food"

    def cod_message_skip(self) -> str:
        return "Starved to death"


class DrinkCondition(HammyCondition):
    def cod_message_act(self) -> str:
        return "Turned into a Tsunami"

    def cod_message_skip(self) -> str:
        return "Died of thirst"


class SleepCondition(HammyCondition):
    def cod_message_act(self) -> str:
        return "Died in his sleep"

    def cod_message_skip(self) -> str:
        return "Lack of sleep"


class AttentionCondition(HammyCondition):
    def cod_message_act(self) -> str:
        return "Turned into a pancake from all the attention"

    def cod_message_skip(self) -> str:
        return "Lack of love"
