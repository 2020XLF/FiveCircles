from PyQt5.Qt import *


'''
    重写按钮 不然一直接受键盘事件，
    事件再次接受后 就不往上传递了 这导致蛇没有办法控制
'''
class myButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
    def keyPressEvent(self, ev):
        ev.ignore()
        #忽略键盘事件，这样会网上传递到父控件