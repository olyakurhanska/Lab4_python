import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QInputDialog,
    QDialog,
    QFormLayout,
    QDialogButtonBox,
    QSpinBox,
)


class CustomDialog(QDialog):
    """Власне модальне діалогове вікно."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Власне діалогове вікно")
        self.setModal(True)

        self.name_input = QLineEdit()
        self.age_input = QSpinBox()
        self.age_input.setRange(1, 100)
        self.age_input.setValue(18)

        form_layout = QFormLayout()
        form_layout.addRow("Ім'я:", self.name_input)
        form_layout.addRow("Вік:", self.age_input)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_data(self):
        """Повертає дані, введені користувачем."""
        return self.name_input.text(), self.age_input.value()


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Завдання 5 — Діалогові вікна та QSS")
        self.resize(500, 400)

        self.title_label = QLabel("Діалогові вікна та стилізація QSS")
        self.title_label.setObjectName("titleLabel")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введіть ім'я")

        self.result_label = QLabel("Результат буде відображено тут")
        self.result_label.setObjectName("resultLabel")

        self.message_button = QPushButton("QMessageBox")
        self.input_button = QPushButton("QInputDialog")
        self.custom_button = QPushButton("Власний QDialog")
        self.clear_button = QPushButton("Очистити")

        self.message_button.setObjectName("messageButton")
        self.clear_button.setObjectName("clearButton")

        self.message_button.clicked.connect(self.show_message_box)
        self.input_button.clicked.connect(self.show_input_dialog)
        self.custom_button.clicked.connect(self.show_custom_dialog)
        self.clear_button.clicked.connect(self.clear_data)

        layout = QVBoxLayout()

        layout.addWidget(self.title_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.result_label)

        layout.addWidget(self.message_button)
        layout.addWidget(self.input_button)
        layout.addWidget(self.custom_button)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

        self.apply_styles()

    def apply_styles(self):
        """Застосування глобального QSS."""

        self.setStyleSheet("""
            QWidget {
                background-color: #202124;
                color: #f1f3f4;
                font-size: 14px;
            }

            QLabel {
                color: #e8eaed;
                padding: 5px;
            }

            QLineEdit {
                background-color: #303134;
                color: white;
                border: 2px solid #5f6368;
                border-radius: 6px;
                padding: 8px;
            }

            QLineEdit:focus {
                border: 2px solid #8ab4f8;
            }

            QPushButton {
                background-color: #3c4043;
                color: white;
                border: 1px solid #5f6368;
                border-radius: 6px;
                padding: 9px;
            }

            QPushButton:hover {
                background-color: #5f6368;
            }

            QPushButton:pressed {
                background-color: #8ab4f8;
                color: #202124;
            }

            #titleLabel {
                color: #8ab4f8;
                font-size: 22px;
                font-weight: bold;
                padding: 12px;
            }

            #resultLabel {
                background-color: #303134;
                border: 1px solid #5f6368;
                border-radius: 6px;
                padding: 12px;
            }

            #messageButton {
                background-color: #4a90e2;
            }

            #clearButton {
                background-color: #8b3a3a;
            }
        """)

    def show_message_box(self):
        """Стандартне діалогове вікно QMessageBox."""

        name = self.name_input.text().strip()

        if not name:
            name = "користувачу"

        QMessageBox.information(
            self,
            "Вітаю!",
            f"Вітаю, {name}!"
        )

        self.result_label.setText(
            f"QMessageBox: виконано привітання для {name}"
        )

    def show_input_dialog(self):
        """Стандартне діалогове вікно QInputDialog."""

        text, ok = QInputDialog.getText(
            self,
            "QInputDialog",
            "Введіть своє місто:"
        )

        if ok and text.strip():
            self.result_label.setText(
                f"QInputDialog: ваше місто — {text}"
            )

    def show_custom_dialog(self):
        """Відкриває власний модальний QDialog."""

        dialog = CustomDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            name, age = dialog.get_data()

            if name.strip():
                self.result_label.setText(
                    f"QDialog: ім'я — {name}, вік — {age}"
                )
            else:
                self.result_label.setText(
                    f"QDialog: вік — {age}"
                )

    def clear_data(self):
        """Очищення введених даних."""

        self.name_input.clear()
        self.result_label.setText(
            "Результат буде відображено тут"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())