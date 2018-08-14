def test1():
	tS = "testing this string"
	print(tS[:-3])
	print(tS[-3:])
	

def test2():
	ts = "This is a string!"
	tslen = len(ts)
	tslhalf = tslen // 2
	print(str(tslen) + " half: " + str(tslhalf)) 
	
def test3():
	"""A docstring for test 3"""
	list1 = ["This", "is", "a", "list"]
	print(list1[0][1])


def main():
	print (test3.__doc__)
	test3()



if __name__ == '__main__':
	main()
