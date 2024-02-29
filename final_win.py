from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()


        # создаём и настраиваем графические элементы:
        self.initUI()


        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()
print("zxc")


print('Hello World!!')
