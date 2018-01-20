from keras.layers import Dense, Input, concatenate
from keras.models import Model
from keras.optimizers import Adam
import numpy as np

from hammy import Needs, Experience, Action


class Ramp(object):
    def __init__(self, start: float, end: float, steps: int, delay: int = 0):
        self.value = start
        self.start = start
        self.end = end
        self.steps = steps
        self.delay = delay

        if steps == 0:
            self.value = end

        self._steps_processed = 0

    def step(self, steps: int) -> float:
        self._steps_processed += steps

        if self._steps_processed < self.delay:
            return self.value

        ramp_vertical = self.end - self.start
        ramp_horizontal = self.steps

        try:
            m = ramp_vertical / ramp_horizontal
        except ZeroDivisionError:
            self.value = self.end
            return self.end

        x = (self._steps_processed - self.delay)
        b = self.start
        y = m * x + b

        if self.start < self.end:
            self.value = min(self.end, y)
        elif self.start > self.end:
            self.value = max(self.end, y)

        return self.value


class HammyDQN(object):
    def __init__(self):

        self.gamma = Ramp(start=0., end=0.9, steps=0)
        self.epsilon = Ramp(start=1., end=0., steps=10000)

        input_needs = Input(shape=(len(Needs),))
        input_health = Input(shape=(1,))

        x = concatenate([input_needs, input_health])
        x = Dense(32, activation='relu')(x)
        x = Dense(32, activation='relu')(x)

        output_needs = Dense(len(Action), activation='linear')(x)

        model = Model(inputs=[input_needs, input_health], outputs=output_needs)

        self.optimizer = Adam()
        model.compile(optimizer=self.optimizer, loss='mse')

        self.model = model

    def train(self, experience: Experience):

        if not experience.terminal:
            future_rewards = self.model.predict(experience.next_state)[0]

            target = experience.reward + self.gamma.value * np.amax(future_rewards)
        else:
            target = experience.reward

        if target > 1.:
            target = 1.
        elif target < -1.:
            target = -1.

        next_rewards = self.model.predict(experience.original_state)
        next_rewards[0][experience.action.value] = target

        self.model.fit(experience.original_state, next_rewards, epochs=1, verbose=0)

        self.gamma.step(1)
        self.epsilon.step(1)

    def predict(self, state) -> Action:
        if np.random.rand() <= self.epsilon.value:
            return Action(np.random.choice([i for i in range(0, len(Action))]))

        return Action(np.argmax(self.model.predict(state)[0]))

    def save(self, path="weights.h5"):
        self.model.save_weights(filepath=path)

    def load(self, path="weights.h5"):
        self.model.load_weights(filepath=path)
