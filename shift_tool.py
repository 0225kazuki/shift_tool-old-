import calendar
import jholiday
import sqlite3

conn = sqlite3.connect('./day_data.db')
cur = conn.cursor()

# 0:mon 1:tue 2:wed 3:thu 4:fri 5:sat 6:sun
'''
for ele in calendar.Calendar().itermonthdays2(2016,5):
    print ('({0} and {1})'.format(ele[0],ele[1]))
    if ele[0] == 0:
        continue
    print(jholiday.holiday_name(2016,5,ele[0]))
    print(type(jholiday.holiday_name(2016,5,ele[0])))
'''

cur.execute("""CREATE TABLE day_data(month int,day int,date int,worktime text,name1 text,name2 text,name3 text,primary key (month,day));""")
for ele in calendar.Calendar().itermonthdays2(2016,5):
    if ele[0] == 0:
        continue
    cur.execute("""INSERT INTO day_data(month,day,date) VALUES(5,{0},{1});""".format(ele[0],ele[1]))

cur.execute("""SELECT month,day,date FROM day_data;""")
for month,day,date in cur.fetchall():
    print("month {0}, day {1}".format(month,day))
    if (jholiday.holiday_name(2016,month,day)) != None or date == 5 or date == 6:
        print('{0}-{1} = holiday'.format(month,day))
        cur.execute("""UPDATE day_data SET worktime="holiday" WHERE day={0};""".format(day))

conn.commit()
conn.close()
