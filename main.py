import sys
import translator
import googletrans
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *


class Translator(QtWidgets.QMainWindow, translator.Ui_mainWindow):
    def __init__(self, parent=None):
        super(Translator, self).__init__(parent)
        self.setupUi(self)
        self.output_translation.clear()
        self.init_UI()
        self.add_langs()
        self.translate_button.clicked.connect(self.translate)

    def init_UI(self):
        self.setWindowIcon(QIcon('images/icon.png'))

        self.input_text.setPlaceholderText('Введите текст')
        self.output_translation.setPlaceholderText('...')

    def add_langs(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    def translate(self):
        try:
            input_text = self.input_text.text()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            translator = googletrans.Translator()
            translate = translator.translate(input_text, src=lang_1, dest=lang_2)
            self.output_translation.setText(translate.text)

        except Exception as ex:
            self.input_text.setText('Что-то пошло не так..')

#    def error_message(self, text):
#        msg = QMessageBox()
#        msg.setIcon(QMessageBox.Critical)
#        msg.setWindowTitle('Ошибка')
#        msg.setText(str(text))
#        msg.exec_()
#        msg.setWindowIcon('images/icon.png')


app = QtWidgets.QApplication([])
application = Translator()
application.show()

sys.exit(app.exec_())

