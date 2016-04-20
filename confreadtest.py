import calendar
import jholiday
import sqlite3
import sys
import configparser

# 0:mon 1:tue 2:wed 3:thu 4:fri 5:sat 6:sun
date_conv_dict = {0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}


config = configparser.SafeConfigParser()
config.read('setting.conf')
# セクション名、キー名を指定して値を取得
print(config.getfloat('worktime', 'weekday'))
print(config.getfloat('worktime', 'holiday'))
print(config.getfloat('worktime', 'weekday before holiday'))
print(config.getfloat('worktime', 'holiday before holiday'))
