# HesapMakineleri


hesapList = []
myList = []


islem = input("islemi giriniz:")

def start(islem,x):
    global myList
    global hesapList
    myList.append(islem[x])
    if len(islem) -1 == x:
        hesapList.append(myList)
        myList = []
        return
    return start(islem, x+1)

def sayiBelirleme(x):
    global myList
    global hesapList
    try :
        float(hesapList[0][x])
        float(hesapList[0][x+1])

        hesapList[0][x] = str(hesapList[0][x]) + str(hesapList[0][x+1])
        hesapList[0].pop(x+1)

        if len(hesapList[0]) -1 == x:
            return

        return sayiBelirleme(x)
        

    except:
        if len(hesapList[0]) -1 == x:
            return
        return sayiBelirleme(x+1)

    if len(hesapList[0]) -1 == x:
        returns

def parantezislemleri(x):
    global myList
    global hesapList
    parantezCount = hesapList[0].count("(")
    if x == 0:
        global sayac
        sayac = 0

        

    if hesapList[0][x] == "(":
        sayac += 1
        if sayac == parantezCount:
            parantezleriekleme(x)
            parantezcikarma(x)
            sayac -=1
            return parantezislemleri(0)

    if hesapList[0].count("(") == 0 or len(hesapList[0])-1 == x:
        return

    return parantezislemleri(x+1)
    
            

def parantezleriekleme(x):
    global myList
    global hesapList

    if hesapList[0][x+1] == ")":
        # myList.append(hesapList[0][x])
        
        hesapList.append(myList)
        myList = []
        return

    myList.append(hesapList[0][x+1])

    return parantezleriekleme(x+1)

def parantezcikarma(x):
    global myList
    global hesapList

    if hesapList[0][x] == ")":
        hesapList[0].pop(x)
        hesapList[0].insert(x, "parantez")
        return

    hesapList[0].pop(x)

    return parantezcikarma(x)

def parantezici(x):
    parantezyerlestirme(x,0)
    # print(hesapList)
    carpmabolme(x, 0)
    toplamacikarma(x, 0)

    if x +1 == len(hesapList):
        return

    return parantezici(x+1)

def carpmabolme(p,x):
    
    if hesapList[p].count("*") == 0 and hesapList[p].count("/") == 0:
        return

    if hesapList[p][x] == "*":
        hesapList[p][x-1] = float(hesapList[p][x-1]) * float(hesapList[p][x+1])
        hesapList[p].pop(x)
        hesapList[p].pop(x)
        return carpmabolme(p,x)

    elif hesapList[p][x] == "/":
        hesapList[p][x-1] = float(hesapList[p][x-1]) / float(hesapList[p][x+1])
        hesapList[p].pop(x)
        hesapList[p].pop(x)
        return carpmabolme(p,x)

    if len(hesapList[p]) -1 == x:
        return

    carpmabolme(p, x+1)

def toplamacikarma(p,x):

    if hesapList[p].count("+") == 0 and hesapList[p].count("-") == 0:
        return


    if hesapList[p][x] == "+":
        hesapList[p][x-1] = float(hesapList[p][x-1]) + float(hesapList[p][x+1])
        hesapList[p].pop(x)
        hesapList[p].pop(x)
        return toplamacikarma(p, x)

    elif hesapList[p][x] == "-":
        hesapList[p][x-1] = float(hesapList[p][x-1]) - float(hesapList[p][x+1])
        hesapList[p].pop(x)
        hesapList[p].pop(x)
        return toplamacikarma(p, x)

    if len(hesapList[p]) -1 == x:

        return

    return toplamacikarma(p, x+1)

def parantezyerlestirmeyardım(p):
    if len(hesapList[p]) == 1 :
        sayi = hesapList[p][0]
        hesapList[p].clear()
        return sayi
    

    return parantezyerlestirmeyardım(p-1)

def parantezyerlestirme(p,x):
    if hesapList[p].count("parantez") == 0:
        return

    if hesapList[p][x] == "parantez":
        hesapList[p][x] = parantezyerlestirmeyardım(p-1)
            
    # print(hesapList[p][x],x)
    if len(hesapList[p]) -1 == x:
        return

    return parantezyerlestirme(p,x+1)

def sonparantez(x):
    if hesapList[0].count("parantez") == 0:
        return

    if hesapList[0][x] == "parantez":
        hesapList[0][x] = sonparantezNumber(len(hesapList)-1)

    if len(hesapList[0]) -1 == x:
        return

    return sonparantez(x+1)
    
def sonparantezNumber(p):
    if len(hesapList[p]) == 1:
        sayi = hesapList[p][0]
        hesapList[p].clear()
        return sayi

    return sonparantezNumber(p-1)
start(islem, 0)
sayiBelirleme(0)
parantezislemleri(0)
parantezici(1)
# print(hesapList)
sonparantez(0)
carpmabolme(0, 0)
toplamacikarma(0, 0)
print(int(hesapList[0][0]))
