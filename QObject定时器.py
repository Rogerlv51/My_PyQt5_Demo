import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")        # 默认显示的text为10
        self.move(200, 200)
        self.setStyleSheet("font-size: 25px;")

    def set_sec(self, sec):     # 可以修改控制label上显示的数字
        self.setText(str(sec))

    def start_my_timer(self, ms):
        self.timer_id = self.startTimer(ms)   # 开启定时器

    def timerEvent(self, *args, **kwargs):
        # print('XXX')
        # 1.获取标签内容
        current_sec = int(self.text())
        current_sec -= 1     # 每次减1显示
        self.set_sec(current_sec)     # 调用set_sec函数改变text值

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)    # 停止计时


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QObject定时器案例")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.set_sec(5)
label.start_my_timer(1000)    # 1秒打印一次

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())