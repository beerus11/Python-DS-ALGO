import time
start=time.time()
data=[0,1]
def fib(no):
	if len(data)>=no:
		return data[no-1]
	else:
		data.append(fib(no-2)+fib(no-1))
		return data[no-1]
fib(1000)
print 'Execution Time => {:04.3f}'.format(time.time()-start)