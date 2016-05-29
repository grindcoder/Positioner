from logger import Logger
from settings import DEFAULT_POSITIONER_CONFIGURATIONS

class Positioner(Logger):
    def __init__(self, configurations=DEFAULT_POSITIONER_CONFIGURATIONS):
        self.configurations = configurations

