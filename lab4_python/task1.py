import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QSlider,
    QSpinBox,
    QProgressBar,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторна робота №4 — PyQt6")
        self.setMinimumSize(650, 500)

        # Основний вертикальний layout
        main_layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Графічний інтерфейс PyQt6")
        title.setToolTip("Заголовок головного вікна")
        main_layout.addWidget(title)

        # Форма з віджетами
        form_layout = QFormLayout()

        # 1. QLineEdit
        name_input = QLineEdit()
        name_input.setPlaceholderText("Введіть ваше ім'я")
        name_input.setToolTip("Поле для введення імені")
        form_layout.addRow("Ім'я:", name_input)

        # 2. QComboBox
        combo_box = QComboBox()
        combo_box.addItems(["Python", "C++", "Java", "JavaScript"])
        combo_box.setToolTip("Оберіть мову програмування")
        form_layout.addRow("Мова:", combo_box)

        # 3. QSpinBox
        spin_box = QSpinBox()
        spin_box.setRange(1, 100)
        spin_box.setValue(10)
        spin_box.setToolTip("Числове значення від 1 до 100")
        form_layout.addRow("Число:", spin_box)

        # 4. QCheckBox
        check_box = QCheckBox("Я погоджуюсь")
        check_box.setChecked(False)
        check_box.setToolTip("Прапорець підтвердження")
        form_layout.addRow("Згода:", check_box)

        # 5. QRadioButton
        radio_button = QRadioButton("Режим перегляду")
        radio_button.setChecked(True)
        radio_button.setToolTip("Вибір режиму роботи")
        form_layout.addRow("Режим:", radio_button)

        main_layout.addLayout(form_layout)

        # Горизонтальна група з кнопкою та повзунком
        controls_layout = QHBoxLayout()

        # 6. QPushButton
        button = QPushButton("Натиснути")
        button.setToolTip("Кнопка демонстрації")
        controls_layout.addWidget(button)

        # 7. QSlider
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setToolTip("Повзунок від 0 до 100")
        controls_layout.addWidget(slider)

        main_layout.addLayout(controls_layout)

        # 8. QTextEdit
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Введіть додатковий текст...")
        text_edit.setToolTip("Багаторядкове текстове поле")
        main_layout.addWidget(text_edit)

        # 9. QProgressBar
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        progress_bar.setValue(50)
        progress_bar.setToolTip("Індикатор прогресу")
        main_layout.addWidget(progress_bar)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())