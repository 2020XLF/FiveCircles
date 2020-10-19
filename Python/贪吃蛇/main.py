

from MainUI import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUi()
    main.show()
    sys.exit(app.exec_())

