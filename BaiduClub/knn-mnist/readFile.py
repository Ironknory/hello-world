import numpy
import struct

def loadImages(filename) :
	with open(filename, 'rb') as imageFile :
		buf = imageFile.read()	
		readPlc = struct.calcsize('>IIII')
		fileSize = struct.unpack_from('>IIII', buf, 0)
		num, row, col = fileSize[1 : 4]
		cnt = num * row * col
		ans = struct.unpack_from('>' + str(cnt) + 'B', buf, readPlc)
	ans = numpy.reshape(ans, [num, row * col])
	return num, row * col, ans

def loadLables(finlename) :
	with open(filename, 'rb') as lableFile :
		buf = lableFile.read()
		readPlc = struct.calcsize('>II')
		fileSize = struct.unpack_from('>II', buf, 0)
		num = fileSize[1]
		ans = struct.unpack_from('>' + str(cnt) + 'B', buf, readPlc)
	ans = numpy.reshape(ans, [num])
	return num, ans

#print(loadImages('train-images.idx3-ubyte'))
#print(loadLables('train-labels.idx1-ubyte'))

