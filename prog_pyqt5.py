import sys
from PyQt5 import QtWidgets, uic
from post import PostMachine, Tape

# Загрузка интерфейса из файла PostMachine.ui
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("PostMachine.ui", self)
        self.pushButton.clicked.connect(self.start_machine)

    def start_machine(self):
        machine = PostMachine()
        machine.add_command(">")
        machine.add_command("<")
        machine.add_command("1")
        machine.add_command("? 6, 5")
        machine.add_command("0")
        machine.add_command(">")
        machine.add_command("1")
        machine.add_command(".")

        machine.run()
        result = machine.get_tape()
        QtWidgets.QMessageBox.warning(self, "Результат", result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())