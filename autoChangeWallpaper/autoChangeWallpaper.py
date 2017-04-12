#!/usr/bin/python
#_*_coding:utf-8_*_

import os, os.path, sys
import random
import time

rootdir = "/home/jlan/Wallpaper/"

def changeWallpaper():
    for parent, dirnames, filenames in os.walk(rootdir):
        filename = random.choice(filenames)
        print u'正在设置壁纸'
        try:
            os.system("gsettings set org.gnome.desktop.background picture-uri file://"+os.path.join(parent,filename))
        except Exception, e:
            print 'erroe:', e
        else:
            print u'设置成功，壁纸文件为:'+os.path.join(parent, filename)

def autoChangeWallpaper():
    while True:
        for parent, dirnames, filenames in os.walk(rootdir):
            filename = random.choice(filenames)
            print u'正在设置壁纸'
            try:
                os.system("gsettings set org.gnome.desktop.background picture-uri file://"+os.path.join(parent,filename))
            except Exception, e:
                print 'error:', e
            else:
                print u'设置成功，壁纸文件为:'+os.path.join(parent, filename)
            time.sleep(300)

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        changeWallpaper()
    else:
        if arg == 'start':  #做成一个服务来启动
            autoChangeWallpaper()
        else:
            changeWallpaper()
