### 2018-10-14

KNN完成，采用较为简单的$calcDist$函数

``` python
	def calcDist(test, train) :
	ans = 0
	for i in range(trainImage.length) :
		ans += abs((test[i] != 0) ^ (train[i] != 0))
	return ans
	
```

**由于我还不知道怎么用GPU跑，程序特别慢，所以样本极少，正确率可信度不高**
当训练数据在$6e3$个时，正确率大概在$97\%$(succeed 34, fail 1)
当训练数据在$6e2$个时，正确率大概在$77\%$(succeed 37, fail 11)


