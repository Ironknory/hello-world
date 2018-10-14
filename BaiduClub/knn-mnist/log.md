### 2018-10-14

KNN完成，采用较为简单的$calcDist$函数

``` python
	def calcDist(test, train) :
	ans = 0
	for i in range(trainImage.length) :
		ans += abs((test[i] != 0) ^ (train[i] != 0))
	return ans
	
```

**由于我还不知道怎么用GPU跑，程序极其慢，所以样本极少，正确率可信度不高**
当训练数据在$6e3$个时，正确率大概在$97\%$(succeed 34, fail 1)
当训练数据在$6e2$个时，正确率大概在$77\%$(succeed 37, fail 11)

C++实现KNN，原理相同，速度快了不止一个档次，但是仍然不够快
当训练数据在$6e4$个时，正确率$95.86\%$(succeed 9586, fail 414)，耗时31min
但是代码实现原理是一样的，所以说样本少的时候正确率是真的不可信
**不过我不知道C++如何直接处理二进制文件，所以用文件加工了再给cpp读的**
