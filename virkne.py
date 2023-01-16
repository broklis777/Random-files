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
while True:
    skaitlis = int(input("Ievadi skaitli: "))
    if vai_neder(skaitlis):
        print("Skaitlis neder!!!!!")
    else:
        print("der")
