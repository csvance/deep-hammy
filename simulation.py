import csv
import argparse

from hammy import Hammy
from hammy_nn import HammyDQN


def main(args):
    max_age = 0
    headers = ['age', 'epsilon', 'gamma']
    log_file = open('log.csv', 'w')
    log_writer = csv.DictWriter(log_file, fieldnames=headers)
    log_writer.writeheader()

    hammy = Hammy()
    dqn = HammyDQN(epsilon_start=args.epsilon_start, epsilon_end=args.epsilon_end, epsilon_steps=args.epsilon_steps,
                   gamma_start=args.gamma_start, gamma_end=args.gamma_end, gamma_steps=args.gamma_steps)

    lives = 0

    for episode in range(0, args.episodes):
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

    dqn.save(args.weights_file)

    print("Hammy's longest life: %d days" % int(max_age / 24))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights-file', type=str, default="weights.h5")
    parser.add_argument('--episodes', type=int, default=1000)

    parser.add_argument('--epsilon-start', type=float, default=1.)
    parser.add_argument('--epsilon-steps', type=int, default=10000)
    parser.add_argument('--epsilon-end', type=float, default=0.)

    parser.add_argument('--gamma-start', type=float, default=0.)
    parser.add_argument('--gamma-steps', type=int, default=0)
    parser.add_argument('--gamma-end', type=float, default=0.9)

    args = parser.parse_args()

    main(args)
