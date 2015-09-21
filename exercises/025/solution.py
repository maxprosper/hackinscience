import datetime
b = datetime.datetime.now()
c = b.strftime("%Y-%m-%d")
d = b.strftime("%H:%M:%S")
print('Today is', c, 'and it is', d)
