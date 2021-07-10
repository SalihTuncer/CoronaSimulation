# package imports
import Main
from ConfigViewer import ConfigGUI

# imports which need to be installed externally
from PyQt5.QtWidgets import QApplication

# internal python libraries
import sys
import argparse

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
