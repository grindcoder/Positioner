# -*- coding: utf-8 -*-
from logger import Logger
import settings

import os
import shutil


class Positioner(Logger):
    def __init__(self, configurations=settings):
        self.configurations = configurations

    def get_destination_dir(self, type):
        return os.path.join(self.configurations.DESTINATION_DIR,
                            self.configurations.FILES_MAPPING[type]['destination'])

    def position_dir(self, location):
        self.debug("Position dir")
        # ciclo i file della cartella
        for file in os.listdir(os.path.join(location)):
            # ciclo i tipi di file configurati
            for type in self.configurations.FILES_MAPPING.keys():
                # se la sua estensione è tra quelle configurate
                if file.endswith(self.configurations.FILES_MAPPING[type]['exts']):
                    shutil.move(os.path.join(location), self.get_destination_dir(type))

    def position_file(self, location):
        self.debug("Position file")
        for type in self.configurations.FILES_MAPPING.keys():
            # se la sua estensione è tra quelle configurate
            if location.endswith(self.configurations.FILES_MAPPING[type]['exts']):
                shutil.move(os.path.join(location), self.get_destination_dir(type))

    def run_on_dirs(self):
        self.info("Running on target dirs")
        self.debug("Dirs\n{}".format("\n".join(self.configurations.DOWNLOAD_DIRS)))

        for target_dir in self.configurations.DOWNLOAD_DIRS:
            self.info("Parsing\t->\t{}".format(target_dir))
            download_list = os.listdir(target_dir)

            for file in download_list:

                location = os.path.join(target_dir, file)
                self.debug("Parsing\t->\t{}".format(file))

                self.debug("Check if is dir")
                if os.path.isdir(location):
                    # Se e' una directory  effettua un position dir

                    self.position_dir(location)

                # Altrimenti se e' un cazzo di file fai questo questo e questo
                self.position_file(location)
