import csv

from hammy import Hammy
from hammy_nn import HammyDQN


def main():
    headers = ['age', 'epsilon', 'gamma']
    log_file = open('log.csv', 'w')
    log_writer = csv.DictWriter(log_file, fieldnames=headers)
    log_writer.writeheader()

    hammy = Hammy()
    dqn = HammyDQN()

    lives = 0

    while True:
        while True:
            action = dqn.predict(hammy.state())
            if not hammy.action(action):
                break
            if hammy.age % 24 == 0:
                print("Hammy is %d days old" % int(hammy.age / 24))

        print("Hammy is dead. Cause of death: %s" % hammy.cod)
        print("Hammy lived %d days" % int(hammy.age / 24))

        log_writer.writerow({'age': hammy.age, 'epsilon': dqn.epsilon.value, 'gamma': dqn.gamma.value})
        for e in hammy.e.sample():
            dqn.train(e)
        hammy.reset()
        lives += 1.

        if lives % 10 == 0:
            log_file.flush()


if __name__ == '__main__':
    main()
