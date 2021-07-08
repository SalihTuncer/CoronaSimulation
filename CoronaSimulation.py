# -*- coding: utf-8 -*-

# imports which need to be installed externally
from PyQt5.QtWidgets import QApplication

# internal python libraries
import sys
import argparse

# package imports
import Main
from ConfigViewer import ConfigGUI

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # Required positional argument
    parser.add_argument('--mode', type=str,
                        help='--mode=gui | --mode=cmd')
    args = parser.parse_args()

    config = {}

    if args.mode == 'gui':
        config_app = QApplication(sys.argv)
        config_gui = ConfigGUI()
        config_gui.show()
        sys.exit(config_app.exec_())
    else:
        for line in open("corona_simulation.cfg", "r"):
            # remove spaces at the beginning and the end of the line
            line = line.strip()
            # we want to ignore the comments in the configuration-file
            if not line.startswith("#"):
                setting = line.split('=')
                config[setting[0].strip()] = float(setting[1])

        Main.main(config)
    '''
    TODOS
    
    - Anzahl Bevoelkerung vernuentig parsen z.b.: 80 Millionen statt 80000000.0
    - gleitende Mittelwerte ( running means ) -> am Ende auch extrapolieren
    - Konfiguration in GUI
    - 7-Tage Inzidenz GUI
    - vielleicht Legende/Beschreibungen in GUI
    
    '''
