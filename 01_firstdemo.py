import sys

from PyQt5.Qt import *

# 几乎所有qt程序都要先创建一个应用
app = QApplication(sys.argv)

# 创建一个页面窗口
window = QWidget()
# 设置窗口名称
window.setWindowTitle("第一个PyQt程序")
# 窗口大小
window.resize(500, 500)
# 窗口弹出的初始位置（即我们电脑界面上看到的位置）
window.move(800, 250)

label = QLabel(window)
label.setText("Hello world")
label.move(200, 240)

window.show()

sys.exit(app.exec_())