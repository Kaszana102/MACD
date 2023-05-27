import csv
from re import sub
from decimal import Decimal
from EMA import *
import math
from Plots import *



file = open("dane2.csv")
csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
cena = []
dates = []
price = []
rows = []
for row in csvreader:
	rows.append(row)
	for i in range(1,len(row)):
		money = row[i]
		row[i] = Decimal(sub(r'[^\d.]', '', money))
	cena.append(row[5])
	dates.append(row[0]) #data
	price.append(row[1]) #kwota
	
	#print(row)
	

dates.reverse()
price.reverse()

act_money=0
shares=1000
sharesAmount=[]
money=[]
ema12=[]
ema26=[]
signal=[]
macd=[]
for i in range(len(price)):
	ema12.append(EMA(price, i, 12))
	ema26.append(EMA(price, i, 26))
	macd.append(ema12[i]-ema26[i])
	signal.append(EMA(macd, i, 9))


# symulacja strategii
BUY_FRACTION=14  #14
SELL_FRACTION=3

sharesAmount.append(shares)
money.append(act_money)
for i in range(1,len(dates)):
	if(macd[i]>=signal[i] and act_money>=price[i]):
		#kupuj
		amount=math.floor(act_money/price[i] /BUY_FRACTION)
		act_money-= amount*price[i]
		shares+=amount

	elif macd[i]<=signal[i]:
		#sprzedawaj
		amount = math.ceil(shares/SELL_FRACTION)
		act_money += amount * price[i]
		shares -= amount

	money.append(act_money)
	sharesAmount.append(shares)


print(shares,price[len(price)-1],act_money,price[0])
print("Income= ",(shares*price[len(price)-1]+act_money)/(1000*price[0]))

PlotAll(dates,price,macd,signal,money,sharesAmount)
#Plot2(dates,price,macd,signal)



	
file.close()

