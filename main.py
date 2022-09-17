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
        self.output_currency.clear()
        self.init_UI()
        self.translate_button.clicked.connect(self.translate)

    def init_UI(self):
        self.setWindowIcon(QIcon('images/icon.png'))

        self.input_text.setPlaceholderText('Введите текст')
        self.output_currency.setPlaceholderText('...')

    def translate(self):
        try:
            input_text = self.input_text.text()
            lang_1 = 'ru'
            lang_2 = 'en'
            translator = googletrans.Translator()
            translate = translator.translate(input_text, src = lang_1, dest = lang_2)
            self.output_currency.setText(translate.text)
        except Exception as ex:
            pass

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

