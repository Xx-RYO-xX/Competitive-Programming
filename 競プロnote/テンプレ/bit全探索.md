### コード
```python
lst = [0]*n ## 長さnのリストに対してbit全探索をする
ans = [] ## 結果を格納するためのリスト
for i in range(2 ** n):
	anst = []
	for j in range(n):
		bit = (2 ** j)
		if (i // bit) % 2 == 1:
			anst.append(lst[j])
	ans.append(anst)
```
#### 解説
長さ $n$ のリストに対するbit全探索（すべての部分集合の列挙）を行う実装です。 整数 `i` を二進数と見立てることで、各要素を「選ぶ / 選ばない」の全組み合わせ（$2^n$ 通り）を効率的に列挙しています。