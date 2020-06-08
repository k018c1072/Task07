hoge = int(input('数値> '))
ans = 1
for h in range(1, hoge + 1):
    ans *= h

print(hoge, 'の階乗:', ans)
