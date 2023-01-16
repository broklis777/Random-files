#1,000,000,000,000,000,000
# 10, 100, 1000 (a ir 1 un b ir 0)
# 10 (a ir 0 un b ir 1)
import json
saraksts = []
for a in range(0,10):
    for b in range(0,10):
        if a != b:
            saraksts.append(f"{a}{b}")
            saraksts.append(f"{b}{a}")#2
            saraksts.append(f"{a}{b}{b}")
            saraksts.append(f"{b}{a}{b}")
            saraksts.append(f"{b}{b}{a}")#3
            saraksts.append(f"{a}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{a}")#4
            saraksts.append(f"{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}")#5
            saraksts.append(f"{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}")#6
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}")#7
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}")#8
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}")#9
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#10
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#11
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#12
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#13
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#14
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#15
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#16
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#17
            saraksts.append(f"{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}{b}")
            saraksts.append(f"{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{a}")#18
for i in range(1, 10):
            saraksts.append(f"{i}0")#2
            saraksts.append(f"{i}00")#3
            saraksts.append(f"{i}000")#4
            saraksts.append(f"{i}0000")#5
            saraksts.append(f"{i}00000")#6
            saraksts.append(f"{i}000000")#7
            saraksts.append(f"{i}0000000")#8
            saraksts.append(f"{i}00000000")#9
            saraksts.append(f"{i}000000000")#10
            saraksts.append(f"{i}0000000000")#11
            saraksts.append(f"{i}00000000000")#12
            saraksts.append(f"{i}000000000000")#13
            saraksts.append(f"{i}0000000000000")#14
            saraksts.append(f"{i}00000000000000")#15
            saraksts.append(f"{i}000000000000000")#16
            saraksts.append(f"{i}0000000000000000")#17
            saraksts.append(f"{i}00000000000000000")#18
saraksts2 = []
for kk in saraksts:
    saraksts2.append(int(kk))
saraksts2.sort()
for n in range(0, len(saraksts2)):
    if  str(saraksts2[n])[0] == "0":
        saraksts2.pop(n)
saraksts = []
for m in saraksts2:
    if m not in saraksts:
        saraksts.append(m)
saraksts.sort()
def vai_neder(number1v):
    first_num = str(number1v)[0]
    allnums = 0
    list_ = []
    for k in str(number1v):
        list_.append(k)
    for g in list_:
        if g == first_num:
            allnums +=1
    #print(f"All numbers are = {allnums}")
    #print(f"First num is = {first_num}")
    #print(list_)
    #print(f" len(str(number)) [{len(str(number))}]    ==     allnums  [{allnums}]")
    if len(str(number1v)) == allnums:
        return True
print(saraksts)
delete = []
for t in saraksts:
    if vai_neder(t):
        saraksts.remove(t)


with open('new_file.json', 'w') as f:
    json.dump(saraksts, f, indent=2)
    print("New json file is created from data.json file")

