# external imports which need to be installed
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton

# internal python libraries
import sys


class SimulationGUI(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        QMainWindow.__init__(self)

        self.setGeometry(600, 300, 640, 480)
        self.setWindowTitle('Corona Simulator')

        self.default_config = {'Inkubationszeit in Tagen:': 5,
                               'Dauer der Krankheit in Tagen:': 14,
                               'Sterblichkeitsrate in Dezimal:': 0.0275,
                               'Größe des erweiterten Freundeskreises:': 42,
                               'Simulationsdauer in Tagen:': 200,
                               'Anzahl Infektionen am Anfange:': 8,
                               'Bevölkerungszahl exakt:': 80000000
                               }

        self.input_config = {}

        y_pos = 60

        self.labels = []
        self.inputs = []
        # initialize Labels  and LineEdits
        for _ in range(len(self.default_config)):
            self.labels.append(QLabel(self))
            self.labels[-1].move(70, y_pos)
            self.labels[-1].resize(300, 30)

            self.inputs.append(QLineEdit(self))
            self.inputs[-1].move(350, y_pos)
            self.inputs[-1].resize(150, 30)
            print(self.inputs[-1].text())
            y_pos += 40

        self.fill_text()

        start_sim = QPushButton('Simulation start_simen', self)
        start_sim.move(320, y_pos + 40)
        start_sim.resize(200, 30)
        start_sim.clicked.connect(self.on_click)

        default = QPushButton('default settings', self)
        default.move(100, y_pos + 40)
        default.resize(170, 30)
        default.clicked.connect(self.fill_text)

        self.show()
        sys.exit(app.exec_())

    def fill_text(self):
        for i, (key, value) in enumerate(self.default_config.items()):
            self.labels[i].setText(key)
            self.inputs[i].setText(str(value))

    def on_click(self):
        print('Simulation started.')
        for i in range(len(self.labels)):
            self.input_config[self.labels[i].text()] = self.inputs[i].text()
        print(self.input_config)


if __name__ == '__main__':
    SimulationGUI()
