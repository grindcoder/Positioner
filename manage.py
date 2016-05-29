import os
import shutil
from logger import logger
from positioner import Positioner


def run():
    # Istanzio la classe
    positioner = Positioner()

    # Lancio un metodo della classe per fare il parsing delle directory
    positioner.run_on_dirs()


if __name__ == '__main__':
    logger.info("Start positioning..")
    run()
