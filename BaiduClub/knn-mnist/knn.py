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
trainImage = Image(readFile.loadImages('train-images.idx3-ubyte'))
trainLable = Lable(readFile.loadLables('train-labels.idx1-ubyte'))
testImage = Image(readFile.loadTmages('t10k-images.idx3-ubyte'))
testLable = Lable(readFile.loadLables('t10k-labels.idx1-ubyte'))

def calcDist(test, train) :
	ans = 0
	for i in range(trainImage.length) :
		ans += abs(test[i] - train[i])
	return ans

def calcMinplc(dist) :
	minplc = 0
	for i in range(1, len(dist)) :
		if (dist[minplc][0] > dist[i][0]) :
			minplc = i
	return minplc

def main() :
	for i in range(testImage.num) :
		dist = []
		test = testImage.data[i]
		for j in range(trainImage.num) :
			train = trainImage.data[j]
			tmp = calcDist(test, train)
			if (len(dist) < K) :
				dist.append(list(tmp, trainLable.data[j]))
			else :
				minplc = calcMinplc(dist)
				if (tmp < dist[minplc][0]) :
					dist[minplc] = list(tmp, trainLable.data[j])
		cnt = [0] * K
		maxplc = 1
		for j in dist :
			cnt[j[1]] += 1
			if (cnt[j[1]] > cnt[maxplc]) :
				maxplc = j[1]
		if (maxplc == testLable.data[i]) :
			cntSucceed += 1
	print(float(cntSucceed / testImage.num))

main()
