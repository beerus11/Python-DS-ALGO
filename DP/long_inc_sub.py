def lis(array):
	data=[1]*len(array)
	for i in range(1,len(array)):
		for j in range(0,i):
			if array[i]>array[j] and data[i]<data[j]+1:
				data[i]=data[j]+1
	return max(data)

print lis([10, 22, 9, 33, 21, 50, 41, 60])