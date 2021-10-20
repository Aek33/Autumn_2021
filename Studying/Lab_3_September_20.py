# Lab 3: Date, Time and numbers

# Lab 4: List generator

import time
import calendar
import datetime

print("---%s---" % "Date")
print(time.gmtime())  # 1
print(float(time.time()))  # 2
print(time.time())  # 3

today = time.gmtime()  # 4
print(today)
print("Year: ", today.tm_year)
print("Month: ", today.tm_mon)
print("Day: ", today.tm_mday)

print(time.struct_time)  # 5

s = int(time.time())  # 6
s %= 86400
h = s // 3600
s %= 3600
m = s // 60
s %= 60
print("# 6: ", h, ":", m, ":", s)

time_7 = 1632123639.31302 + (84600 * 42)  # 7
new_t = time.localtime(time_7)
print(new_t)

print(calendar.timegm(time.gmtime()))  # 8

print(time.localtime())  # 9

print(time.localtime(s))  # 10

today_2 = datetime.date(today.tm_year, today.tm_mon, today.tm_mday)  # 11
print(today_2.strftime('%d/%m/%Y'))

time_1 = "14:50:59"
print(datetime.datetime.strptime(time_1, '%H:%M:%S').time())  # 12

print("---%s---" % "Numbers")
print("---%s---" % "task 1")

l_1 = [1, 3, 4, 7, 8, 5, 9]  # 1
l_1.sort()
l_2 = []
l_3 = []
for i in range(l_1[0], l_1[-1] + 1):
    l_2.append(i)
l_2.sort()
for i in range(len(l_2)):
    if l_2[i] not in l_1:
        l_3.append(l_2[i])
print(l_3)

print("---%s---" % "task 2")

print(set(range(l_1[0], l_1[-1])) - set(l_1))  # 2

print("---%s---" % "task 3")

l_4 = [11, 8, 78, 25, 654, 13, 57]  # 3
odd = []
add = []
for i in range(len(l_4)):
    if l_4[i] % 2 == 0:
        add.append(l_4[i])
    else:
        odd.append(l_4[i])
s = 0
for i in range(len(odd)):
    s += odd[i]
print("Add: " + " ".join(str(i) for i in add))
print("Odd: " + " ".join(str(i) for i in odd))
print("Sum of odd: ", s)

print("---%s---" % "task 4")

n = 2  # 4
num_sum = 0
while n != 0:
    num_sum += n
    n -= 1
print(num_sum)

print("---%s---" % "task 5")


def Num_bits(n):
    count_bits = 0
    while n > 0:
        if n & 1 == 1:
            count_bits += 1
        n >>= 1
    return count_bits


def invert_sum(x, y):
    invert_bit = []
    i = Num_bits(x) + Num_bits(y)
    print('Sum:', bin(i)[2:])
    while i > 0:
        invert_bit.append(i & 1)
        i >>= 1
    print('Invert sum:', ("".join(map(str, invert_bit))))
    return int(("".join(map(str, invert_bit))), 2)


print(invert_sum(5, 6), "\n")

print("---%s---" % "Dates")

print("---%s---" % "task 1")


def defineDays(date_1, date_2):  # 1 (days between)
    if date_1 > date_2:
        defined_date = date_1 - date_2
    else:
        defined_date = date_2 - date_1
    return defined_date.days


def defineDate(date_1, date_2):  # 1 (dates between)
    date_1 = date_1.timetuple()
    date_2 = date_2.timetuple()
    year = date_1.tm_year - date_2.tm_year
    month = date_1.tm_mon - date_2.tm_mon
    day = date_1.tm_mday - date_2.tm_mday
    return [str(abs(year)), str(abs(month)), str(abs(day))]


birth_day = datetime.date(1998, 1, 13)
print(defineDays(today_2, birth_day), "days")
print(defineDate(today_2, birth_day)[0],
      "years ", defineDate(today_2, birth_day)[1],
      "months ", defineDate(today_2, birth_day)[2], "days")

print("---%s---" % "task 2")

print("---%s---" % "task 3")


def addDate(date_1, date_2):  # 3
    date_1 = calendar.timegm(date_1.timetuple())
    date_2 = calendar.timegm(date_2.timetuple())
    add_Date = date_1 + date_2
    return time.gmtime(add_Date)


def subtractDate(date_1, date_2):
    date_1 = calendar.timegm(date_1.timetuple())
    date_2 = calendar.timegm(date_2.timetuple())
    subtract_Date = date_1 - date_2
    return time.gmtime(subtract_Date)


date_1 = datetime.date(2050, 7, 25)
date_2 = datetime.date(1975, 3, 30)
print(addDate(date_1, date_2).tm_year, addDate(date_1, date_2).tm_mon, addDate(date_1, date_2).tm_mday)
print(subtractDate(date_1, date_2).tm_year, subtractDate(date_1, date_2).tm_mon, subtractDate(date_1, date_2).tm_mday)
