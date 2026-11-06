import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QSpinBox,
)


class InputComponent(QWidget):
    name_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я")

        self.send_button = QPushButton("Передати ім'я")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Компонент введення"))
        layout.addWidget(self.name_input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_name)

    def send_name(self):
        name = self.name_input.text().strip()

        if name:
            self.name_changed.emit(name)


class NumberComponent(QWidget):
    number_changed = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()

        self.number_input = QSpinBox()
        self.number_input.setRange(0, 100)
        self.number_input.setValue(10)

        self.send_button = QPushButton("Передати число")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Компонент числа"))
        layout.addWidget(self.number_input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_number)

    def send_number(self):
        number = self.number_input.value()
        self.number_changed.emit(number, "Число отримано")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторна робота №4 — Завдання 4")
        self.resize(600, 450)

        self.input_component = InputComponent()
        self.number_component = NumberComponent()

        self.result_label = QLabel("Результат:")
        self.number_label = QLabel("Значення числа:")

        self.disconnect_button = QPushButton(
            "Від'єднати сигнал імені"
        )

        self.connect_button = QPushButton(
            "Під'єднати сигнал імені"
        )

        layout = QVBoxLayout()

        layout.addWidget(self.input_component)
        layout.addWidget(self.number_component)
        layout.addWidget(self.result_label)
        layout.addWidget(self.number_label)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

        # З'єднання компонентів здійснюється зовні
        self.input_component.name_changed.connect(
            self.show_name
        )

        self.number_component.number_changed.connect(
            self.show_number
        )

        self.disconnect_button.clicked.connect(
            self.disconnect_name_signal
        )

        self.connect_button.clicked.connect(
            self.connect_name_signal
        )

    def show_name(self, name):
        self.result_label.setText(
            f"Результат: Отримано ім'я — {name}"
        )

    def show_number(self, number, message):
        self.number_label.setText(
            f"{message}: {number}"
        )

    def disconnect_name_signal(self):
        try:
            self.input_component.name_changed.disconnect(
                self.show_name
            )

            self.result_label.setText(
                "Результат: сигнал імені від'єднано"
            )

        except TypeError:
            self.result_label.setText(
                "Результат: сигнал уже від'єднано"
            )

    def connect_name_signal(self):
        try:
            self.input_component.name_changed.connect(
                self.show_name
            )

            self.result_label.setText(
                "Результат: сигнал імені під'єднано"
            )

        except TypeError:
            self.result_label.setText(
                "Результат: сигнал уже під'єднано"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())