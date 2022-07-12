import os
import re

from PySide6 import QtWidgets

from PySide6.QtWidgets import QFileDialog

from ui import search


class MyWidgetsForm(QtWidgets.QWidget):
    """
    Класс инициализации виджета
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = search.Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        """
        Подключение кнопок
        :return:
        """
        self.ui.pushButton_search.clicked.connect(self.onPBStartSearch)
        self.ui.pushButtonGoOver.clicked.connect(self.onPBOpenWya)
        self.ui.pushButton_Open.clicked.connect(self.browse_folder)

    def browse_folder(self):
        """
        Открытие диалогового окна
        :return:
        """
        # TODO  Не могу понять, как передать в lineEdit_way ссылку на файлы :((
        self.ui.lineEdit_way.clear()
        directory = QFileDialog.getExistingDirectory(self, "Select one or more files to open", "D:\Учёба\TEST_QT")
        # directory = QFileDialog.getOpenFileNames(self, "Select one or more files to open", "D:\Учёба\TEST_QT")
        self.ui.lineEdit_way.setText(directory)

    def onPBStartSearch(self):
        """
        Функия - активатор кнопки поиска
        :return:
        """
        self.file_way = self.ui.lineEdit_way.text()
        self.search_bar = self.ui.lineEdit_choice.text()

        if self.ui.comboBox.currentText() == 'Построчный поиск':
            self.searchStr()
        elif self.ui.comboBox.currentText() == 'Бинарный поиск':
            self.searchBinary()
        elif self.ui.comboBox.currentText() == 'Поиск по байтам':
            self.searchByte()

    def onPBOpenWya(self):
        """
        # TODO не работает, не понимаю, как передавать ссылку на директорию(файл)
        :return:
        """
        directory_way = self.ui.listWidget.currentItem().text()
        open_directory = QFileDialog.getOpenFileName(self, directory_way)

    def searchStr(self):
        """
        Построчный поиск
        :return: Путь к файлу
        """

        self.ui.listWidget.clear()

        for root, dirs, files in os.walk(self.file_way):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if self.search_bar in f.read():
                        self.catalog = os.path.abspath(file_path)
                        print(self.catalog)
                        self.ui.listWidget.addItem(self.catalog)

    def searchByte(self):
        """
        Поиск по байтам
        :return: Путь к файлу
        """

        self.ui.listWidget.clear()

        for root, dirs, files in os.walk(self.file_way):
            for file in files:
                file_path: str = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    if self.search_bar.encode('utf-8') in f.read():
                        self.catalog = os.path.abspath(file_path)
                        print(self.catalog)
                        self.ui.listWidget.addItem(self.catalog)

    def searchBinary(self):
        """
        поиск по бинарным сигнатурам
        :return: Путь к файлу
        """

        self.ui.listWidget.clear()

        for root, dirs, files in os.walk(self.file_way):
            for file in files:
                file_path: str = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    search_file = re.compile(self.search_bar)
                    search_file.findall(file)
                    if search_file.findall(file) is not None:
                        self.catalog = os.path.abspath(file_path)
                        print(self.catalog)
                        self.ui.listWidget.addItem(self.catalog)


def main():
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec()


if __name__ == '__main__':
    main()
