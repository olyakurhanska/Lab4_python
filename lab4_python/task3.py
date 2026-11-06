import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QToolBar,
)

from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторна робота №4 — Завдання 3")
        self.resize(800, 500)

        # Центральний віджет
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Введіть текст...")
        self.setCentralWidget(self.text_edit)

        # Рядок стану
        self.statusBar().showMessage("Готово")

        # =========================
        # Дії меню
        # =========================

        self.new_action = QAction("Новий", self)
        self.open_action = QAction("Відкрити", self)
        self.save_action = QAction("Зберегти", self)
        self.exit_action = QAction("Вихід", self)

        self.about_action = QAction("Про програму", self)
        self.clear_action = QAction("Очистити", self)

        # Клавіатурні скорочення
        self.new_action.setShortcut("Ctrl+N")
        self.open_action.setShortcut("Ctrl+O")
        self.save_action.setShortcut("Ctrl+S")
        self.exit_action.setShortcut("Ctrl+Q")

        # =========================
        # Меню
        # =========================

        file_menu = self.menuBar().addMenu("Файл")
        help_menu = self.menuBar().addMenu("Довідка")

        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        help_menu.addAction(self.about_action)
        help_menu.addAction(self.clear_action)

        # =========================
        # Панель інструментів
        # =========================

        toolbar = QToolBar("Панель інструментів", self)
        self.addToolBar(toolbar)

        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.clear_action)

        # =========================
        # Обробники дій
        # =========================

        self.new_action.triggered.connect(self.new_document)
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.exit_action.triggered.connect(self.close)

        self.about_action.triggered.connect(self.show_about)
        self.clear_action.triggered.connect(self.clear_text)

        self.text_edit.textChanged.connect(self.update_status)

    def new_document(self):
        self.text_edit.clear()
        self.statusBar().showMessage("Створено новий документ")

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Відкрити файл",
            "",
            "Текстові файли (*.txt);;Усі файли (*)"
        )

        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    self.text_edit.setPlainText(file.read())

                self.statusBar().showMessage(
                    f"Відкрито файл: {file_name}"
                )
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Помилка",
                    f"Не вдалося відкрити файл:\n{error}"
                )

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Зберегти файл",
            "",
            "Текстові файли (*.txt);;Усі файли (*)"
        )

        if file_name:
            try:
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(self.text_edit.toPlainText())

                self.statusBar().showMessage(
                    f"Файл збережено: {file_name}"
                )
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Помилка",
                    f"Не вдалося зберегти файл:\n{error}"
                )

    def clear_text(self):
        self.text_edit.clear()
        self.statusBar().showMessage("Текст очищено")

    def show_about(self):
        QMessageBox.about(
            self,
            "Про програму",
            "Лабораторна робота №4 — PyQt6\n"
            "Завдання 3"
        )

    def update_status(self):
        count = len(self.text_edit.toPlainText())
        self.statusBar().showMessage(
            f"Кількість символів: {count}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())