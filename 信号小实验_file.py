import os
import sys
# 做一个点击打开文件夹的小实验

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号的操作_打开文件")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText("选择文件")
        btn.move(200, 200)

        def openFlie():
            path = os.getcwd()
            os.startfile(filepath=path)
            

        btn.clicked.connect(openFlie)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())