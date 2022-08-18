import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.move(400, 250)


# window.setCursor(Qt.ForbiddenCursor)
# window.setCursor(Qt.OpenHandCursor)

label = QLabel(window)
label.setText("Roger大帅B")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan;")

# label.setCursor(Qt.ForbiddenCursor)  # 进入控件范围内，鼠标变化

pixmap = QPixmap("./python_96px.ico")  # 图片路径，QPixmap类用于在标签或按钮上显示图像
pixmap = pixmap.scaled(100, 100)  # 重新设置大小
cursor = QCursor(pixmap, 0, 0)  # 0, 0 为初始位置，QCursor类用来获取和设置鼠标光标的位置
label.setCursor(cursor)
# label.unsetCursor()  # 恢复鼠标

current_cursor = label.cursor()
# print(current_cursor.pos())  # 获取光标位置（相对于整个电脑屏幕）
current_cursor.setPos(500, 500)  # 设置光标位置，当窗口打开时光标会自动定位到指定位置

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())