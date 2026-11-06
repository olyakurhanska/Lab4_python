import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QSlider,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторна робота №4 — Завдання 2")
        self.resize(600, 450)

        # Поле введення імені
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ваше ім'я")
        self.name_input.setToolTip("Введіть ім'я користувача")

        # Вибір мови
        self.language_combo = QComboBox()
        self.language_combo.addItems(["Python", "C++", "Java"])
        self.language_combo.setToolTip("Оберіть мову програмування")

        # Числове значення
        self.number_spin = QSpinBox()
        self.number_spin.setRange(1, 100)
        self.number_spin.setValue(10)
        self.number_spin.setToolTip("Оберіть число від 1 до 100")

        # Прапорець
        self.agreement_check = QCheckBox("Я погоджуюсь")
        self.agreement_check.setToolTip("Підтвердіть згоду")

        # Повзунок
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)

        self.slider_label = QLabel("Значення повзунка: 50")

        # Результат
        self.result_label = QLabel("Результат: ")

        # Кнопки
        self.confirm_button = QPushButton("Підтвердити")
        self.reset_button = QPushButton("Скинути")

        self.confirm_button.setEnabled(False)

        # Основне компонування
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Ім'я:"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Мова:"))
        layout.addWidget(self.language_combo)

        layout.addWidget(QLabel("Число:"))
        layout.addWidget(self.number_spin)

        layout.addWidget(self.agreement_check)

        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.confirm_button)
        buttons_layout.addWidget(self.reset_button)

        layout.addLayout(buttons_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # 1. Вбудований сигнал textChanged
        self.name_input.textChanged.connect(self.check_form)

        # 2. Сигнал valueChanged змінює інший віджет
        self.slider.valueChanged.connect(
            lambda value: self.slider_label.setText(
                f"Значення повзунка: {value}"
            )
        )

        # 3. Сигнал стану прапорця
        self.agreement_check.stateChanged.connect(
            lambda: self.confirm_button.setEnabled(
                bool(self.name_input.text().strip())
                and self.agreement_check.isChecked()
            )
        )

        # 4. Сигнал кнопки
        self.confirm_button.clicked.connect(self.validate_form)

        # Додатковий сигнал вибору зі списку
        self.language_combo.currentTextChanged.connect(
            self.update_language
        )

        # Кнопка скидання
        self.reset_button.clicked.connect(self.reset_form)

    def check_form(self):
        """Перевірка можливості підтвердження форми."""
        self.confirm_button.setEnabled(
            bool(self.name_input.text().strip())
            and self.agreement_check.isChecked()
        )

    def update_language(self, language):
        """Оновлення результату при виборі мови."""
        self.result_label.setText(
            f"Обрана мова: {language}"
        )

    def validate_form(self):
        """Валідація введених даних."""
        name = self.name_input.text().strip()
        number = self.number_spin.value()

        if not name:
            QMessageBox.warning(
                self,
                "Помилка",
                "Будь ласка, введіть ім'я."
            )
            return

        if not 1 <= number <= 100:
            QMessageBox.warning(
                self,
                "Помилка",
                "Число має бути в діапазоні від 1 до 100."
            )
            return

        if not self.agreement_check.isChecked():
            QMessageBox.warning(
                self,
                "Помилка",
                "Потрібно підтвердити згоду."
            )
            return

        self.result_label.setText(
            f"Результат: {name}, "
            f"{self.language_combo.currentText()}, "
            f"число {number}"
        )

        QMessageBox.information(
            self,
            "Успішно",
            "Дані введено правильно!"
        )

    def reset_form(self):
        """Повернення форми до початкового стану."""
        self.name_input.clear()
        self.language_combo.setCurrentIndex(0)
        self.number_spin.setValue(10)
        self.agreement_check.setChecked(False)
        self.slider.setValue(50)
        self.slider_label.setText("Значення повзунка: 50")
        self.result_label.setText("Результат: ")
        self.confirm_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())