import time
import math

from trainer import Trainer


def main():
    useless_but_cool_oneliner()
    total_with_start_measuring()
    using_contexts()
    full_package_badass_trainer()


def useless_but_cool_oneliner():
     metrics = Trainer().round().start_measuring().add_total().metrics
     print('\nuseless_but_cool_oneliner:\n', metrics)


def total_with_start_measuring():
    trainer = Trainer().start_measuring()

    time.sleep(math.pi / 10)

    trainer.add_total('total')

    time.sleep(math.pi / 10)

    print('\ntotal_with_start_measuring:\n', trainer.metrics)


def using_contexts():
    trainer = Trainer().round(2)

    with trainer('sleeping'):
       time.sleep(math.pi / 10)

    with trainer('sleeping_again'):
        time.sleep(math.pi / 10)

    print('\nusing_contexts:\n', trainer.metrics)


def full_package_badass_trainer():
    badass_trainer = Trainer().round(4)

    with badass_trainer('run'):
        time.sleep(math.pi / 10)

    with badass_trainer('gym'):
        time.sleep(math.pi / 10)

    with badass_trainer('stretching'):
        time.sleep(math.pi / 10)

    metrics = badass_trainer.add_total('03.07.2022').metrics
    print('\nfull_package_badass_trainer:\n', metrics)


if __name__ == '__main__':
    main()
