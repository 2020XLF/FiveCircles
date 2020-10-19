from PyQt5.Qt import *
import sys
from PyQt5.QtGui import *
from myButton import *
import random

begin_x, begin_y = 100,100
s_size = 10
class MainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,600)
        self.move(500,200)

        self.setUI()

        self.speed = 100
        self.s_length = 7

        self.initSnake()
        self.initFood()
        self.moveDirection = 0  # 0向上  1向下 2向左 3向右

        self.timer = QTimer()
        self.timer.start(self.speed) #定时器先关闭
        # 定时器开启后 会按设定时间，触发下面信号
        self.timer.timeout.connect(self.continue_go) #设置信号与槽

    def setUI(self):
        self.label_snack_length = QLabel("长度：7",self)
        self.label_snack_length.setStyleSheet("Font-size:24px;")
        self.label_snack_length.move(20,0)
        self.label_snack_length.resize(150,30)
        self.addSpeed = myButton(self)
        self.addSpeed.setText("+")
        self.addSpeed.move(250,5)
        self.subSpeed = myButton(self)
        self.subSpeed.setText("-")
        self.subSpeed.move(350,5)

        self.addSpeed.clicked.connect(self.addS)
        self.subSpeed.clicked.connect(self.subS)


    def paintEvent(self, event):
        #画分割线
        self.setLine()
        #画食物
        self.setFood()
        #画蛇
        self.setSnake()
    def setLine(self):
        painter = QPainter(self)
        painter.drawLine(0,30,600,30)
    def initFood(self):
        self.food_site = QRectF(50,50,10,10)
    def setFood(self):
        painter = QPainter(self)
        brush = QBrush(Qt.red,Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawEllipse(self.food_site)

    def initSnake(self):
        self.growing = 7    #蛇长度
        self.snack_head = QPointF(begin_x,begin_y) #蛇头位置
        self.snack = []     #蛇身子

        x = begin_x
        while self.growing:
            tail = QRectF(x,begin_y,s_size,s_size)
            self.snack.append(tail)
            x+=10
            self.growing-=1
    def setSnake(self):
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        for tail in self.snack:
            painter.drawRect(tail)


    def continue_go(self):
        if self.moveDirection%4 == 0:
            self.moveUp()
        if self.moveDirection%4 == 1:
            self.moveDown()
        if self.moveDirection%4 == 2:
            self.moveLeft()
        if self.moveDirection%4 == 3:
            self.moveRight()


        self.crash() #碰撞检测

        if self.growing == 0:
            self.snack.pop()
        else:
            self.growing-=1
        self.update()
    def keyPressEvent(self,ev):
        if(ev.key() == Qt.Key_Up):
            self.moveDirection = 0
        elif(ev.key() == Qt.Key_Down):
            self.moveDirection = 1
        elif(ev.key() == Qt.Key_Left):
            self.moveDirection = 2
        elif(ev.key() == Qt.Key_Right):
            self.moveDirection = 3

        self.continue_go()
        return

    def moveUp(self):

        self.snack_head.setY(self.snack_head.y()-10)
        if self.snack_head.y() < 30:
            self.snack_head.setY(600)
        h = QRectF(self.snack_head.x(),self.snack_head.y(),s_size,s_size)
        self.snack.insert(0,h)

    def moveDown(self):
        self.snack_head.setY(self.snack_head.y() + 10)
        if self.snack_head.y() > 600:
            self.snack_head.setY(30)
        h = QRectF(self.snack_head.x(), self.snack_head.y(), s_size, s_size)
        self.snack.insert(0, h)

    def moveLeft(self):
        self.snack_head.setX(self.snack_head.x() - 10)
        if self.snack_head.x() < 0:
            self.snack_head.setX(600)
        h = QRectF(self.snack_head.x(), self.snack_head.y(), s_size, s_size)
        self.snack.insert(0, h)

    def moveRight(self):
        self.snack_head.setX(self.snack_head.x() + 10)
        if self.snack_head.x() > 600:
            self.snack_head.setX(0)
        h = QRectF(self.snack_head.x(), self.snack_head.y(), s_size, s_size)
        self.snack.insert(0, h)



    #碰撞检测
    def crash(self):
        if self.food_site in self.snack:
            while True:
                x = random.randrange(10, 590,10)
                y = random.randrange(10, 590,10)
                if self.food_site.x()!=x and self.food_site.y()!=y:
                    break
            self.food_site = QRectF(x, y, 10, 10)
            self.growing+=1
            self.setGrade()
            print("crash")

    #分数设定
    def setGrade(self):
        self.s_length+=1
        info = "长度："+str(self.s_length)
        self.label_snack_length.setText(info)
    ###-----slot___
    def addS(self):
        self.timer.stop()
        if self.speed >20:
            self.speed-=20
        print(self.speed)
        self.timer.start(self.speed)
    def subS(self):
        self.timer.stop()
        if self.speed < 200:
            self.speed+=20
        print(self.speed)
        self.timer.start(self.speed)



