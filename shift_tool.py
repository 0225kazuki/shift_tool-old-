import calendar
import jholiday
import sqlite3
import sys

conn = sqlite3.connect('./day_data.db')
cur = conn.cursor()

# 0:mon 1:tue 2:wed 3:thu 4:fri 5:sat 6:sun
date_conv_dict = {0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}


i = 0
words = [['','']]

#単語読み込み
for line in open('config','r'):
    if len(line) > 1 and line[-2] == ',' :
        print('input format error:line ',i,':',line)
        continue
    else:
        words.append(line[:-1].split(','))
    i += 1


#is_ystday = 0;
cur.execute("""CREATE TABLE day_data(year int,month int,day int,date text,isholi int,ispreholi int,name1 text,name2 text,name3 text,primary key (month,day));""")

for ele in calendar.Calendar().itermonthdays2(2016,5):
    if ele[0] == 0:
        continue
    cur.execute("""INSERT INTO day_data(year,month,day,date,isholi,ispreholi) VALUES(2016,5,{0},"{1}",0,0);""".format(ele[0],date_conv_dict[ele[1]]))

cur.execute("""SELECT month,day,date FROM day_data;""")
for month,day,date in cur.fetchall():
    print("month {0}, day {1}".format(month,day))
    if (jholiday.holiday_name(2016,month,day)) != None or date == "Sat" or date == "Sun":
        #print('{0}-{1} = holiday'.format(month,day))
        cur.execute("""UPDATE day_data SET isholi=1 WHERE day={0};""".format(day))
        #if is_ystday == 0:
        cur.execute("""UPDATE day_data SET ispreholi=1 WHERE day={0};""".format(day-1))
        #elif is_ystday == 1:
        #cur.execute("""UPDATE day_data SET worktime="bef-hday-hday" WHERE day={0};""".format(day-1))
        #is_ystday = 1
        #else:
        #cur.execute("""UPDATE day_data SET worktime="weekday" WHERE day={0};""".format(day))
                #is_ystday = 0

conn.commit()
conn.close()
