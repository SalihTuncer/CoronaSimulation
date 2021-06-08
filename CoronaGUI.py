import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        QMainWindow.__init__(self)

        self.setGeometry(600, 300, 640, 480)
        self.setWindowTitle('Corona Simulator')

        config = {'Inkubationszeit in Tagen:': 5,
                  'Dauer der Krankheit in Tagen:': 14,
                  'Sterblichkeitsrate in Dezimal:': 0.0275,
                  'Größe des erweiterten Freundeskreises:': 42,
                  'Simulationsdauer in Tagen:': 200,
                  'Anzahl Infektionen am Anfange:': 8,
                  'Bevölkerungszahl exakt:': 80000000
                  }

        y_pos = 60

        for key, value in config.items():
            label = QLabel(self)
            label.setText(key)
            label.move(70, y_pos)
            label.resize(300, 30)

            input = QLineEdit(self)
            input.move(350, y_pos)
            input.resize(150, 30)
            input.setText(str(value))
            print(input.text())
            y_pos += 40

        start = QPushButton('Simulation starten', self)
        start.move(220, y_pos + 40)
        start.resize(200, 30)
        start.clicked.connect(self.on_click)

        self.show()
        sys.exit(app.exec_())

    def on_click(self):
        print('Simulation started.')


if __name__ == '__main__':
    MainWindow()
