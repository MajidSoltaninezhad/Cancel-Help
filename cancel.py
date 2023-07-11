import sys
import pyautogui

import ctypes

# Load the user32.dll library
user32 = ctypes.windll.LoadLibrary("user32.dll")

# Send the WM_INPUTLANGCHANGEREQUEST message to change the keyboard layout
user32.SendMessageW(
    ctypes.c_void_p(0xffff), # HWND_BROADCAST
    0x0050, # WM_INPUTLANGCHANGEREQUEST
    0, # wParam (not used)
    ctypes.c_long(0x04090409).value # lParam: 0x0409 = English (United States)
)



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon,QDoubleValidator,QValidator

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar
from qt_material import apply_stylesheet


from turtle import delay
import time
from pynput import mouse , keyboard             

from pynput.keyboard import Key, Controller

import pyautogui
import time
import os





def window():
  m=mouse.Controller()
  kb = Controller()

  




  
  app = QApplication(sys.argv)
  win = QMainWindow()
  win.setGeometry(300,500,350,100)
  win.setWindowTitle("Cancel-Pack-Helper")
  win.setToolTip("CPH")
  win.setWindowIcon(QIcon("cancel-logo.ico"))
  win.setFixedSize(350,100)

# m=mouse.Controller()
# kb = Controller()


  def ctr_delet():

    print("alt-delet")
    kb.press(Key.ctrl)
    kb.press("a")
    kb.release("a")
    kb.release(Key.ctrl)
    time.sleep(1)
    kb.press(Key.delete)
    kb.release(Key.delete)
    time.sleep(0.1)

  def helper():

    confidence_help = 0.9
    condition_help = False
    while not condition_help :
      ex_location = pyautogui.locateOnScreen("excel.png",confidence = confidence_help)
      nunpack_location = pyautogui.locateOnScreen("nunpack.png",confidence = confidence_help)
      other_location = pyautogui.locateOnScreen("other.png",confidence = confidence_help)
      print("nashod")
      if ex_location or nunpack_location or other_location is not None:
        print("delet")
        ctr_delet()    



    





    

  
  btn_save = QtWidgets.QPushButton(win)
  btn_save.setText("Run Helper")
  btn_save.setGeometry(105, 15, 140, 30)
  btn_save.clicked.connect(helper)
  

  # btn_save = QtWidgets.QPushButton(win)
  # btn_save.setText('End')
  # btn_save.clicked.connect(end)
  # btn_save.move(125,55)
  font_size = QFont()
  font_size.setPointSize(10)
  font_size.setBold(True)

  font_metrics = QFontMetrics(font_size)
  text_width = font_metrics.width("لطفا سایز صفحه را روی 200% قرار دهید!!")
  lbl_cancel = QtWidgets.QLabel(win)
  lbl_cancel.setFont(font_size)
  lbl_cancel.setFixedWidth(text_width + 5)
  
  lbl_cancel.move(35, 55)
  lbl_cancel.setText("لطفا zoom صفحه را روی 200% قرار دهید!!")


  

  apply_stylesheet(app, theme='dark_blue.xml')
  win.show()
  sys.exit(app.exec_())

window()