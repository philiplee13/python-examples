from observers.observers import ObserverOne, ObserverTwo
from subjects.subjects import ConcreteSubject


def main():
    subject = ConcreteSubject()
    obs_one = ObserverOne()
    obs_two = ObserverTwo()

    subject.add(obs_one)
    subject.add(obs_two)

    subject.random_number()

    subject.remove(obs_two)

    subject.random_number()


if __name__ == "__main__":
    main()
