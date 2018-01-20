import csv

from hammy import Hammy
from hammy_nn import HammyDQN


def main(episodes=1000):
    max_age = 0
    headers = ['age', 'epsilon', 'gamma']
    log_file = open('log.csv', 'w')
    log_writer = csv.DictWriter(log_file, fieldnames=headers)
    log_writer.writeheader()

    hammy = Hammy()
    dqn = HammyDQN()

    lives = 0

    for episode in range(0, episodes):
        while hammy.age < hammy.max_age:
            action = dqn.predict(hammy.state())
            if not hammy.action(action):
                break
            if hammy.age % 24 == 0:
                print("Hammy is %d days old" % int(hammy.age / 24))

        log_writer.writerow({'age': hammy.age, 'epsilon': dqn.epsilon.value, 'gamma': dqn.gamma.value})
        log_file.flush()

        max_age = max(hammy.age, max_age)

        if hammy.health <= 0.:
            print("Hammy is dead. Cause of death: %s" % hammy.cod)
            print("Hammy lived %d days" % int(hammy.age / 24))
            for e in hammy.e.sample():
                dqn.train(e)
        else:
            print("Hammy died of old age!")
            break

        hammy.reset()
        lives += 1.

    dqn.save()

    print("Hammy's longest life: %d days" % int(max_age / 24))


if __name__ == '__main__':
    main()
