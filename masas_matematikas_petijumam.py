import random
def mest():
    skaitlis1 = random.randint(1, 6)
    skaitlis2 = random.randint(1, 6)
    skaitlis3 = random.randint(1, 6)
    print(f"""
    
    Pirmais kauliņš: {skaitlis1}
    Otrais kauliņš: {skaitlis2}
    Trešais kauliņš: {skaitlis3}
    Summa = {skaitlis1 + skaitlis2 + skaitlis3}
    """)
    turpinat = input()
    if turpinat != "gehrgioeroih":

        mest()
#mest()
summa3vai18 = []
summa4vai17 = []
summa5vai16 = []
summa6vai15 = []
summa7vai14 = []
summa8_9_10_11_12_13 = []
for i in range(1, 7):
    for u in range(1, 7):
        for m in range(1, 7):
            summa =  i + u + m
            print(f"{i} {u} {m} == {summa}")
            if summa == 3 or summa == 18:
                summa3vai18.append(f"{i}.{u}.{m}")
            elif summa == 4 or summa == 17:
                summa4vai17.append(f"{i}.{u}.{m}")
            elif summa == 5 or summa == 16:
                summa5vai16.append(f"{i}.{u}.{m}")
            elif summa == 6 or summa == 15:
                summa6vai15.append(f"{i}.{u}.{m}")
            elif summa == 7 or summa == 14:
                summa7vai14.append(f"{i}.{u}.{m}")
            else: 
                summa8_9_10_11_12_13.append(f"{i}.{u}.{m}")
kopejaisgaddaudzums = len(summa3vai18) + len(summa4vai17) + len(summa5vai16) + len(summa6vai15) + len(summa7vai14) + len(summa8_9_10_11_12_13)
print(f"""
Iespējamie varianti = {kopejaisgaddaudzums}
Uzmetās 3 vai 18, gadījumu skaits ({len(summa3vai18)}) kas ir apmēram {len(summa3vai18) * 100 /kopejaisgaddaudzums}
Uzmetās 4 vai 17, gadījumu skaits ({len(summa4vai17)}) kas ir apmēram {len(summa4vai17) * 100 /kopejaisgaddaudzums}
Uzmetās 5 vai 16, gadījumu skaits ({len(summa5vai16)}) kas ir apmēram {len(summa5vai16) * 100 /kopejaisgaddaudzums}
Uzmetās 6 vai 15, gadījumu skaits ({len(summa6vai15)}) kas ir apmēram {len(summa6vai15) * 100 /kopejaisgaddaudzums}
Uzmetās 7 vai 14, gadījumu skaits ({len(summa7vai14)}) kas ir apmēram {len(summa7vai14) * 100 /kopejaisgaddaudzums}
Uzmetās 8 - 13, gadījumu skaits ({len(summa8_9_10_11_12_13)}) kas ir apmēram {len(summa8_9_10_11_12_13) * 100 /kopejaisgaddaudzums}

""")
