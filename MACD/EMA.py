

#data tablica danych
#row - dzisiajeszy dzien
#N ile dni w wstecz
def EMA (data, row, N):
	numerator = 0  #licznik
	denominator = 0  #mianownik
	if(row - N < 0):
		a = 2/(row+1)
		b = 1-a
		for i in range(row+1):
			numerator += float(data[row-i])*(b**i)
			denominator += b**i
	else:
		a=2/(N+1)
		b=1-a
		for i in range(N):
			numerator += float(data[row-i])*(b**i)
			denominator += b**i
	return numerator / denominator




