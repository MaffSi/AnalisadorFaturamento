import sys
from PyQt5.QtWidgets import QApplication
from componentes.interface import MainInterface

def main():

    app = QApplication(sys.argv)
    window = MainInterface()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()