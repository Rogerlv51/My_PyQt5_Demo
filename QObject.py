import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 注释或取消注释即可测试下面的各种方法。使用中文函数名仅为阅读方便，是不好的做法，切勿在自己的代码中出现非ASCII函数名！
        self.qObject_show_parents()
        self.test_Objects_NameAttributes()
        self.test_QObject_style()
        self.test_QObject_ParentsAndChildrens()
        self.test_QObject_del()

    def qObject_show_parents(self):    # 这个函数的意思是打印出当前class的所有继承关系
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def test_Objects_NameAttributes(self):
        # 测试API
        obj = QObject()
        obj.setObjectName("notice")  # 给一个Qt对象设置一个名称，一般是唯一的，当做对象的ID使用
        print(obj.objectName())  # 获取一个Qt对象的名称

        obj.setProperty("notice_level", "error")  # 给一个Qt对象动态的添加一个属性与值
        obj.setProperty("notice_level2", "warning")

        print(obj.property("notice_level"))  # 获取一个对象的属性值
        print(obj.dynamicPropertyNames())  # 获取一个对象中所有通过setProperty()设置的属性名称

    def test_QObject_style(self):
        with open("QObject.qss", "r") as f:    
            # .qss文件是我们提前写好保存的一个样式表，在里面指定了名为notice的label的样式
            qApp.setStyleSheet(f.read())  # QSS样式表

        label = QLabel(self)
        label.setText("muzing")
        label.setObjectName("notice")  # 根据QSS中设置的规则，只有ObjectName为notice的QLabel才会改变样式
        label.setProperty("notice_level", "warning")

        label2 = QLabel(self)
        label2.move(0, 60)
        label2.setText("https://github.com/muziing")
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "normal")   # 根据不同的属性选择qss中不同的样式

    def test_QObject_ParentsAndChildrens(self):
        # 测试API
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        print("obj0", obj0)
        print("obj1", obj1)
        print("obj2", obj2)
        print("obj3", obj3)
        print("obj4", obj4)
        print("obj5", obj5)

        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName("2")

        # label = QLabel()
        # label.setParent(obj0)

        obj3.setParent(obj1)
        obj3.setObjectName("3")
        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # print(obj4.parent())
        # print(obj0.children())
        print(obj0.findChild(QObject))     # 可以看到通过findChild方法只能找到没有名字的孩子
        print(obj0.findChild(QObject, "2"))   # 想找到有对象名称的只能指定名字
        print(obj0.findChild(QObject, "3"))
        print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly)) #仅找直接关联的孩子
        print(obj0.findChildren(QObject))   # 返回所有孩子，不管有没有指定名字和直接关联
        # print(obj0.findChild(QLabel))  # 会报错

    def test_QObject_del(self):
        obj1 = QObject()
        self.obj1 = obj1  # 把obj1设置为self的属性，则obj1不会被自动释放
        obj2 = QObject()

        obj2.setParent(obj1)
        # 父控件被删除时子控件自动被删除
        # 监听obj2对象被释放
        obj2.destroyed.connect(lambda: print("obj2对象被释放了"))
        del self.obj1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())