tc = int(input())
res = []

for _ in range(tc):
    row = input()

    cnt=0
    for a in row:
        if a =='(':
            cnt+=1
        else:
            if cnt >0:
                cnt-=1
            elif cnt ==0:
                cnt=-1
                break

    res.append("YES" if cnt == 0 else "NO")

for r in res:
    print(r)
