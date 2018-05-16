# -*- coding:utf-8 -*-
"""
 * @file MyServer
 * @author 党智腾
 * mail 642212607@qq.com
 * WeChat dangzhiteng
 * @date 2018-05-14
 * @version V 1.0
"""
import source_rc
import numpy as np
from PIL import Image
from configwin import Ui_Config
from wordcloud import WordCloud
from mainwindow import Ui_Mainwin
import sys, time, os, re, requests
from PyQt5.QtGui import QIcon, QMovie, QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QFile, QTextCodec, QTextStream, QIODevice, QFile, pyqtSignal

class Mainwindow(QWidget, Ui_Mainwin):
    # 默认配置信息
    font_path = './source/方正小标宋.TTF'
    margin = 5
    width = 3216
    height = 2184
    max_words = 150
    background_color = 'white'
    mask = './source/mask.jpg'
    random_state = 60
    min_font_size = 10
    max_font_size = 80
    def __init__(self,parent = None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.config = Configwin()
        self.config.sendconfig_signal.connect(self.configset)
        self.setAcceptDrops(True)
        self.setWindowIcon(QIcon(':/source/wordcloud.ico'))
        self.show_pic.setStyleSheet("border-image: url(:/source/cloud.png);")
        self.load_text.clicked.connect(self.load)
        self.begin.clicked.connect(self.create_pic)
        self.save_pic.clicked.connect(self.save)
        self.changeset.clicked.connect(self.config.show)
        if os.path.exists('./wordcloud'):
            pass
        else:
            os.mkdir('./wordcloud')
        if os.path.exists('./source'):
            pass
        else:
            os.mkdir('./source')
        try:
            info = requests.get('http://139.199.163.147/cloudversion.txt')
            if info.content.decode() != 'V1.0':
                QMessageBox.information(self, '信息', '新版本{0}已经发布！'.format(info.content.decode()),QMessageBox.Yes)
        except:
            QMessageBox.information(self, '警告', '无法检测新版本,以离线方式启动...', QMessageBox.Yes)
    def configset(self, font_path, max_word, backcolor, mask_path_line, color_random, min_size, max_size):
        self.font_path = font_path
        self.max_words = max_word
        self.background_color = backcolor
        self.mask = mask_path_line
        self.random_state = color_random
        self.min_font_size = min_size
        self.max_font_size = max_size
    def save(self):
        self.show_pic.grab().save('./wordcloud/'+str(time.time())+'.jpg')
        QMessageBox.information(self, '提示', '词云保存成功！', QMessageBox.Yes)
    def load(self):
        self.path, ok = QFileDialog.getOpenFileName(self, 'Load file', ':/source/', 'Text Files (*.txt)')
        if ok:
            self.text_path.setText(str(self.path))
    def create_pic(self):
        if os.path.exists(self.text_path.text()):
            if self.mask != None:
                try:
                    image = Image.open(self.mask)
                    self.mask = np.array(image)
                except:
                    self.mask = None
            self.wordcloud = WordCloud(font_path = self.font_path,
                                  margin = self.margin,
                                  width = self.width,
                                  height = self.height,
                                  max_words = self.max_words,
                                  background_color = self.background_color,
                                  mask = self.mask,
                                  random_state = self.random_state,
                                  min_font_size = self.min_font_size,
                                  max_font_size = self.max_font_size)
            self.thread = Create_thread(self.path, self.wordcloud)
            self.thread.finish_signal.connect(self.setpixmap)
            self.thread.start()
            self.show_pic.clear()
            movie = QMovie(':/source/loading.gif')
            self.show_pic.setMovie(movie)
            movie.start()
            self.begin.setEnabled(False)
            self.load_text.setEnabled(False)
            self.begin.setText('正在生成')
        else:
            QMessageBox.warning(self, '警告!', '路径非法!', QMessageBox.Yes)
    def setpixmap(self,pic_name):
        self.load_text.setEnabled(True)
        self.begin.setEnabled(True)
        self.begin.setText('开始生成')
        self.show_pic.clear()
        print('设置图片')
        self.show_pic.setStyleSheet("border-image:url({0})".format(pic_name))
        print('删除缓存')
        os.remove(pic_name)
    #重写拖拽事件
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.TargetMoveAction)
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            path = str(event.mimeData().urls()[0].toLocalFile())
            if path[-3:] == 'txt':
                self.text_path.setText(path)
                self.path = path
            else:
                QMessageBox.warning(self, "警告!", '你拖的不是txt格式的文本文件吧？', QMessageBox.Yes)
        else:
            event.ignore()
class Configwin(QWidget, Ui_Config):
    sendconfig_signal = pyqtSignal(str, int, str, str, int, int, int)
    background_color = 'white'
    i = 0
    def __init__(self, parent = None):
        super(Configwin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/source/wordcloud.ico'))
        self.configbtn.clicked.connect(self.sendconfig)
        self.configbtn.clicked.connect(self.hide)
        self.mask_path.clicked.connect(self.setmaskpath)
        self.font_path.clicked.connect(self.setfontpath)
        self.color.clicked.connect(self.setcolor)
    def setcolor(self):
        self.i += 1
        if self.i == 0:
            self.color.setStyleSheet("background-color: white;;")
            self.background_color = 'white'
        elif self.i == 1:
            self.color.setStyleSheet("background-color: black;")
            self.background_color = 'black'
        elif self.i == 2:
            self.color.setStyleSheet("background-color: red;")
            self.background_color = 'red'
        elif self.i == 3:
            self.color.setStyleSheet("background-color: pink;")
            self.background_color = 'pink'
        elif self.i == 4:
            self.color.setStyleSheet("background-color: green;")
            self.background_color = 'green'
        elif self.i == 5:
            self.color.setStyleSheet("background-color: magenta;")
            self.background_color = 'magenta'
        elif self.i == 6:
            self.color.setStyleSheet("background-color: gray;")
            self.background_color = 'gray'
            self.i = -1
    def setfontpath(self):
        path, ok = QFileDialog.getOpenFileName(self, '选择Font', './source', 'Files (*.ttf *.TTF)')
        if ok:
            self.font_path_line.setText(str(path))
    def setmaskpath(self):
        path, ok = QFileDialog.getOpenFileName(self, '选择Mask', './source', 'Files (*.jpg *.png)')
        if ok:
            self.mask_path_line.setText(str(path))
    def sendconfig(self):
        self.sendconfig_signal.emit(self.font_path_line.text(),
                             self.max_word.value(),
                             self.background_color,
                             self.mask_path_line.text(),
                             self.color_random.value(),
                             self.min_size.value(),
                             self.max_size.value()
                             )
class Create_thread(QThread):
    finish_signal = pyqtSignal(str)
    def __init__(self, path, wordcloud):
        super(Create_thread, self).__init__()
        self.path = path
        self.wordcloud = wordcloud
    def run(self):
        print('正在生成词云...')
        try:
            with open(self.path, 'rb') as file:
                self.text = str(file.read().decode())
            self.text = re.sub("[a-zA-Z0-9]+", "", self.text)
            self.wordcloud.generate(self.text)
        except:
            with open(self.path, 'rb') as file:
                self.text = str(file.read().decode('gbk', 'ignore'))
                print(self.text)
            self.text = re.sub("[a-zA-Z0-9]+", "", self.text)
            self.wordcloud.generate(self.text)
        pic_name = './wordcloud/' + str(time.time()) + '.png'
        self.wordcloud.to_file(pic_name)
        print('词云生成完毕...')
        self.finish_signal.emit(pic_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mainwindow()
    #file = QFile(':/source/qss/black.qss')
    #file.open(QIODevice.ReadOnly)
    #qss = QTextStream(file)
    #qss.setCodec(QTextCodec.codecForName('UTF-8'))
    #style = qss.readAll()
    #win.setStyleSheet(style)
    win.show()
    sys.exit(app.exec_())
