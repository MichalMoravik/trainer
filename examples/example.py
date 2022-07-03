import time
import math

from trainer import Trainer


def main():
    useless_but_cool_oneliner()


def useless_but_cool_oneliner():
     metrics = Trainer().round().start_measuring().add_total().metrics
     print('\nuseless:\n', metrics)


if __name__ == '__main__':
    main()
