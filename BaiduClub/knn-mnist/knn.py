import readFile

class Image(object) :
	__slots__ = ('num', 'length', 'data')
	def __init__(self, num, length, data) :
		self.num = num
		self.length = length
		self.data = data

class Lable(object) :
	__slots__ = ('num', 'data')
	def __init__(self, num, data) :
		self.num = num
		self.data = data

K = 20
trainImage = Image(*readFile.loadImages('train-images.idx3-ubyte'))
trainLable = Lable(*readFile.loadLables('train-labels.idx1-ubyte'))
testImage = Image(*readFile.loadImages('t10k-images.idx3-ubyte'))
testLable = Lable(*readFile.loadLables('t10k-labels.idx1-ubyte'))

def calcDist(test, train) :
	ans = 0
	for i in range(trainImage.length) :
		ans += abs((test[i] != 0) ^ (train[i] != 0))
	return ans

def calcMinplc(dist) :
	minplc = 0
	for i in range(1, len(dist)) :
		if (dist[minplc][0] > dist[i][0]) :
			minplc = i
	return minplc

def main() :
	cntFail = 0
	cntSucceed = 0
	for i in range(testImage.num) :
		dist = []
		test = testImage.data[i]
		for j in range(trainImage.num // 10) :
			train = trainImage.data[j]
			tmp = calcDist(test, train)
			dist.append([tmp, trainLable.data[j]])
#			print("successfully compared with %s" %j)
		dist.sort(key = lambda x : x[0])
#		print(dist)
		cnt = [0] * 15
		maxplc = 1
		for j in range(K) :
			cnt[dist[j][1]] += 1
			if (cnt[dist[j][1]] > cnt[maxplc]) :
				maxplc = dist[j][1]
		if (maxplc == testLable.data[i]) :
			cntSucceed += 1
		else :
			cntFail += 1
		print("Succeed %d," %cntSucceed, "Fail %d" %cntFail)
	print(float(cntSucceed / testImage.num))

main()
