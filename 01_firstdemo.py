import sys

# 注意这里导包的时候不是原仓库作者写的PyQt5.Qt，这个已经找不到了，删除了，采用下面的import方式
from PyQt5.QtWidgets import *

# 几乎所有qt程序都要先创建一个应用
app = QApplication(sys.argv)

# 创建一个页面窗口
window = QWidget()
# 设置窗口名称
window.setWindowTitle("第一个PyQt程序")
# 窗口大小
window.resize(600, 600)
# 窗口弹出的初始位置（即我们电脑界面上看到的位置）
window.move(800, 250)

label = QLabel(window)     # 一个文本标签，需要绑定窗口才能显示
label.setText("Hello world")
label.move(250, 250)       # 相对于window的位置
button = QPushButton(window)
button.setText("按压")
button.move(220, 300)

window.show()

sys.exit(app.exec_())