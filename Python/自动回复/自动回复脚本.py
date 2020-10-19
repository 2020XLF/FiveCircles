from pykeyboard import PyKeyboard
import pyperclip
import requests
import time
import random

k = PyKeyboard()


def sendMsg(msg):
    # k.type_string(f"{msm}")
    pyperclip.copy(f"{msg}")
    time.sleep(1)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(1)
    k.tap_key(k.enter_key)


if __name__ == '__main__':
    time.sleep(3)
    mType = "love" # love 一句情话 / wu 你好污啊 / du 有毒吧你  /美句摘写 message
    while True:
        url = "http://toodo.fun/api/api.php?type={0}&skey=free".format(mType)  # 一句情话
        msm = requests.get(url).text
        sendMsg(msm)
        time.sleep(random.randint(0, 10) / 10)
