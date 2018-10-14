#include <bits/stdc++.h>
using namespace std;

const int N = 6e4 + 10;
const int M = 1e4 + 10;
const int L = 800;
const int K = 20;

int n, m, len;
char ate[M], atr[N];
char ste[M][L], str[N][L];

void init() {
	freopen("testImage.in", "r", stdin);
	scanf("%d", &m);
	for (int i = 1; i <= m; ++i)
		scanf("%s", ste[i]);
	freopen("testLable.in", "r", stdin);
	scanf("%d %s", &m, ate + 1);

	freopen("trainImage.in", "r", stdin);
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
		scanf("%s", str[i]);
	freopen("trainLable.in", "r", stdin);
	scanf("%d %s", &n, atr + 1);
	len = strlen(ste[1]);
}

struct nodeHeap {
	int dist, ans;
	nodeHeap() {}
	nodeHeap(int a, int b) : dist(a), ans(b) {}
	inline bool operator < (const nodeHeap &a) const {
		return dist < a.dist;
	}
};
priority_queue <nodeHeap> H;

#define id(a) (a - '0')
inline int calcDist(int a, int b) {
	int ans = 0;
	for (int i = 1; i <= len; ++i)
		ans += abs(ste[a][i] - str[b][i]);
	return ans;
}
bool judge(int a) {
	while (!H.empty()) H.pop();
	for (int i = 1; i <= n; ++i) {
		nodeHeap tmp = nodeHeap(calcDist(a, i), id(atr[i]));
		if (H.size() < K) H.push(tmp);
		else if (tmp < H.top()) {
			H.pop(), H.push(tmp);
		}
	}
	int cnt[10], maxn = 0;
	memset(cnt, 0, sizeof(cnt));
	while (!H.empty()) {
		int ans = H.top().ans; H.pop();
		if (++cnt[ans], cnt[ans] > cnt[maxn])
			maxn = ans;
	}
	return maxn == id(ate[a]);
}

int main() {
	init();
	int cntS = 0, cntF = 0;
	for (int i = 1; i <= m; ++i) {
		if (judge(i))
			++cntS;
		else ++cntF;
		printf("Succeed %d, Fail %d\n", cntS, cntF);
	}
	printf("%lf\n", (double)cntS / (cntS + cntF));
	return 0;
}

