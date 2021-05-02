#Normal Hesap Makinesi
hesapList = []

myList = []
islem = input("işlemi giriniz :")

for i in islem:
    myList.append(i)
hesapList.append(myList)
myList = []
parantezCount = hesapList[0].count("(")
basamakT = False
pSayac = 0
# print(hesapList)

while True:
    for i in range(len(hesapList[0])):
        try :
            float(hesapList[0][i])
            float(hesapList[0][i+1])
            hesapList[0][i] = str(hesapList[0][i]) + str(hesapList[0][i+1])
            hesapList[0].pop(i+1)
        except :
            basamakT = False

    if True:
        for i in range(len(hesapList[0])):
            try:
                float(hesapList[0][i])
                float(hesapList[0][i+1])
                hesapList[0][i] = str(hesapList[0][i]) + str(hesapList[0][i+1])
                hesapList[0].pop(i+1)
                basamakT = True
            except :
                pass
        if not basamakT:
            break

    
# print(hesapList)


while True :
    for i in range(0,len(hesapList[0]),1):
        if hesapList[0][i] == "(":
            pSayac += 1
            if pSayac == parantezCount:
                for j in range(i,len(hesapList[0]),1):
                    myList.append(hesapList[0][j])
                    if hesapList[0][j] == ")":
                        break

                hesapList.append(myList)

                ustparantezCount = hesapList[0].count(")")
                while True:
                    for j in range(i,len(hesapList[0]),1):
                        hesapList[0].pop(j)
                        break
                    if ustparantezCount != hesapList[0].count(")"):
                        break

                    
                
                hesapList[0].insert(j,"parantez")
                parantezCount -= 1
                pSayac = 0
                myList = []
                break
            
    if hesapList[0].count("(") == 0:
        break

# myList = hesapList[0].copy()
# hesapList.append(myList)
# print(hesapList)


for i in range(1,len(hesapList)):

    for k in range(len(hesapList[i])):
        if hesapList[i][k] == "parantez":
            for j in range(i-1,0,-1):
                if len(hesapList[j]) == 1:
                    hesapList[i][k] = hesapList[j][0]
                    hesapList[j].clear()
                    break


    while True :
        for j in range(len(hesapList[i])):
            if hesapList[i][j] == "*":
                hesapList[i][j-1] = float(hesapList[i][j-1]) * float(hesapList[i][j+1])
                hesapList[i].pop(j)
                hesapList[i].pop(j)
                break
            elif hesapList[i][j] == "/":
                hesapList[i][j-1] = float(hesapList[i][j-1]) / float(hesapList[i][j+1])
                hesapList[i].pop(j)
                hesapList[i].pop(j)
                break
        if hesapList[i].count("*") == 0 and hesapList[i].count("/") == 0:
            break

    while True:
        for j in range(len(hesapList[i])):
            if hesapList[i][j] == "+":
                hesapList[i][j-1] = float(hesapList[i][j-1]) + float(hesapList[i][j+1])
                hesapList[i].pop(j)
                hesapList[i].pop(j)
                break
            elif hesapList[i][j] == "-":
                hesapList[i][j-1] = float(hesapList[i][j-1]) - float(hesapList[i][j+1])
                hesapList[i].pop(j)
                hesapList[i].pop(j)
                break
        if hesapList[i].count("+") == 0 and hesapList[i].count("-") == 0:
            # print(i)
            hesapList[i].pop(0)
            hesapList[i].pop(1)
            # print(hesapList)
            break

    
for i in range(len(hesapList[0])):
    if hesapList[0][i] == "parantez":
        for j in range(len(hesapList)-1,-1,-1):
            if len(hesapList[j]) == 1:
                hesapList[0][i] = hesapList[j][0]
                break
        hesapList[j].clear()

# print(hesapList)

while True:
    while True:
        for i in range(len(hesapList[0])):
            if hesapList[0][i] == "*":
                hesapList[0][i-1] = float(hesapList[0][i-1]) * float(hesapList[0][i+1])
                hesapList[0].pop(i)
                hesapList[0].pop(i)
                break

            elif hesapList[0][i] == "/":
                hesapList[0][i-1] = float(hesapList[0][i-1]) / float(hesapList[0][i+1])
                hesapList[0].pop(i)
                hesapList[0].pop(i)
                break
        if hesapList[0].count("*") == 0 and hesapList[0].count("/") == 0:
            break
    while True:
        for i in range(len(hesapList[0])):
            if hesapList[0][i] == "+":
                hesapList[0][i-1] = float(hesapList[0][i-1]) + float(hesapList[0][i+1])
                hesapList[0].pop(i)
                hesapList[0].pop(i)
                break
            elif hesapList[0][i] == "-":
                hesapList[0][i-1] = float(hesapList[0][i-1]) - float(hesapList[0][i+1])
                hesapList[0].pop(i)
                hesapList[0].pop(i)
                break
        if hesapList[0].count("+") == 0 and hesapList[0].count("-") == 0:
            break
        

    if hesapList[0].count("+") == 0 and hesapList[0].count("-") == 0 and hesapList[0].count("*") == 0 and hesapList[0].count("/") == 0:
        break    

print(int(hesapList[0][0]))
