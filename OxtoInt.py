# -*- coding: utf-8 -*-
import datetime
import json
import sys, pyperclip
import time
import re
import requests
import webbrowser
import platform
from urllib import request
from urllib.parse import urlparse
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPen, QBrush, QMovie, QFont, QCursor
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, QDir, QRect, Qt, QFileInfo, QThreadPool, QObject, pyqtSlot
from change_ui import Ui_MainWindow

class test_Form(QMainWindow,Ui_MainWindow):
#class test_Form(QMainWindow):
     def __init__(self):

        super(test_Form, self).__init__()
        self.setupUi(self)
        self.signal_init()
#        self.threadpool = QThreadPool()
        self.setFixedSize(self.width(), self.height())

     def signal_init(self):
          self.all_btn_HEXtoINT.clicked.connect(self.HextoInt)
          self.all_btn_HEXtoINT.setShortcut(Qt.Key_Return)


          self.all_btn_INTtoHEX.clicked.connect(self.IntToHex)
          self.all_btn_INTtoHEX.setShortcut(Qt.Key_Return)
          self.btn_del.clicked.connect(self.del_data)

          

#定义一个函数把十六进制转换成10进制
     def HextoInt(self):
          self.log_info_HEXtoINT.clear()
          #self.log_info_HEXtoINT.setDisabled(True)
          QApplication.processEvents()
          try:
               getArgs = self.serial_line_HEXtoINT.text()
    
               if getArgs == '' or len(str(getArgs).strip()) == 0:
#                      print("没有输出任何数据！！！！")
                      self.log_info_HEXtoINT.append("<font color='red' size='6'><red>没有输出任何数据！！</font>")
               else:

                      #输入的数据不为空，数据先转换成字符串str
                      getArgs1= str(getArgs).strip()
                      #去除全部空格根据正则判断输入的是否是十六进制字符
                      getArgs2 = getArgs1.replace(" ", "")
                      if re.match('^[0-9a-fA-F]+$', getArgs2):
                              #空格分割数据存入一个列表。数据进行转换十进制
                              getArgs3 = getArgs1.split(" ")
                              
                              arrList = []
                              #循环列表getArgs3中的数据
                              for item in getArgs3:
                               #转换的数据加入新建的列表中
                                  arrList.append(int('0x'"" + item + "", 16))
                                  #读取列表中的数据使用空格拼接
                                  results = ' '.join(map(str, arrList))
                              self.log_info_HEXtoINT.append("<font color='green' size='6'><red>" + results+ "</font>")
                              
#                              print(results)

                      else:
#                          print("输入的不是十六进制数据！！")
                          self.log_info_HEXtoINT.append("<font color='red' size='6'><red>输入的不是十六进制数据！！</font>")
          except Exception as e:
#                   print(e)
                   self.log_info_HEXtoINT.append("<font color='green' size='6'><red>" + e + "</font>")
          #self.all_btn_16to10.setDisabled(False)

     def IntToHex(self):
              self.log_info_INTtoHEX.clear()
              #self.log_info_INTtoHEX.setDisabled(True)
              QApplication.processEvents()
              try:
                  getArgs = self.serial_line_INTtoHEX.text()

                  if getArgs == '' or len(str(getArgs).strip()) == 0:
                      #                      print("没有输出任何数据！！！！")
                      self.log_info_INTtoHEX.append("<font color='red' size='6'><red>没有输出任何数据！！</font>")
                  else:
                   try:
                      # 输入的数据不为空，数据先转换成字符串str
                      getArgs1 = str(getArgs).strip()
                      # 去除全部空格根据正则判断输入的是否是十六进制字符
                      getArgs2 = getArgs1.replace(" ", "")
                      if re.match('^[0-9]+$', getArgs2):
                          # 空格分割数据存入一个列表。数据进行转换十进制
                          getArgs3 = getArgs1.split(" ")

                          arrList = []
                          # 循环列表getArgs3中的数据
                          for item in getArgs3:
                              # 转换的数据加入新建的列表中
                              arrList.append(hex( int(item) )[2:].upper())
                              # 读取列表中的数据使用空格拼接
                              results = ' '.join(map(str, arrList))
                          self.log_info_INTtoHEX.append("<font color='green' size='6'><red>" + results + "</font>")

                      #                              print(results)

                      else:

                          #                          print("输入的不是十六进制数据！！")
                          self.log_info_INTtoHEX.append("<font color='red' size='6'><red>输入的不是十进制数据！！</font>")
                   except Exception as e:
                       print(e)

              except Exception as e:
                  self.log_info_INTtoHEX.append("<font color='green' size='6'><red>" + e + "</font>")
              #self.log_info_INTtoHEX.setDisabled(False)


     def del_data(self):
        self.log_info_INTtoHEX.clear()
        self.serial_line_INTtoHEX.clear()


        self.log_info_HEXtoINT.clear()
        self.serial_line_HEXtoINT.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QFileInfo(__file__).absolutePath() 
    ex = test_Form()
    ex.show()
    sys.exit(app.exec_())
#    OxtoInt1()
