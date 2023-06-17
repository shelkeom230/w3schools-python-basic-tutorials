# python datetime 
import datetime

x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x=datetime.datetime(2020,5,17)
print(x)
print(x.strftime("%B"))