gameTree = []
winNodes = []

class Node:
    def __init__(self, virkne, level):
        self.minimaxVal = None
        self.childN = []
        self.virkne = virkne
        self.level = level


def saskaite(a, b):
    if int(a) + int(b) <= 6:
        return str(int(a) + int(b))
    else:
        if (int(a) + int(b) == 12):
            return str(6)
        else:
            return str((int(a) + int(b)) % 6)


def createTree(sVirkne):
    print("Tree generation in process...")
    sakumaN = Node(sVirkne, 0)
    gameTree.append(sakumaN)
    n = 0
    while len(gameTree[n].virkne) != 3:
        for i in range(0, len(gameTree[n].virkne), 2):
            # print("n: %d, childN: %s" % (n, str(gameTree[n].childN)))
            # print("test = %d" % i)
            dup = False
            if i == len(gameTree[n].virkne) - 1 and len(gameTree[n].virkne) % 2 == 1:
                # print("nepāra moments")
                for chld in range(n + 1, len(gameTree)):
                    if gameTree[chld].virkne == (gameTree[n].virkne[0:len(gameTree[n].virkne) - 1]):
                        gameTree[n].childN.append(chld)
                        dup = True
                        break
                if dup == False:
                    gameTree.append(Node(gameTree[n].virkne[0:len(gameTree[n].virkne) - 1], gameTree[n].level + 1))
                    gameTree[n].childN.append(len(gameTree) - 1)
            else:
                # print("pāra moments")
                for chld in range(n + 1, len(gameTree)):
                    if gameTree[chld].virkne == (
                            gameTree[n].virkne[0:i] + saskaite(gameTree[n].virkne[i], gameTree[n].virkne[i + 1]) +
                            gameTree[n].virkne[i + 2:len(gameTree[n].virkne)]):
                        gameTree[n].childN.append(chld)
                        dup = True
                        break
                if dup == False:
                    gameTree.append(Node(
                        gameTree[n].virkne[0:i] + saskaite(gameTree[n].virkne[i], gameTree[n].virkne[i + 1]) + (
                        gameTree[n].virkne[i + 2:len(gameTree[n].virkne)]), gameTree[n].level + 1))
                    gameTree[n].childN.append(len(gameTree) - 1)
        n += 1
    print("Done!")


def printTree():
    print('\n--------------------| START - 0 |--------------------')
    print(gameTree[0].virkne, end="")
    for j in range(1, len(gameTree)):
        if gameTree[j].level != gameTree[j - 1].level:
            print('\n--------------------------' + str(gameTree[j].level) + '--------------------------')
        print("%s(%d)" % (gameTree[j].virkne,j), end=" ")
    print('\n-------------------------END-------------------------')

def getMiniMax(virkne, start):
    if (float(virkne)%2 == 1):
        return int(-1*start)
    else:
        return int(1*start)

def getMin(i):
    min = 1
    for j in gameTree[i].childN:
        #print("%d līmenis, %d elements: %d" % (gameTree[i].level, i, j))
        if gameTree[j].minimaxVal < min:
            min = gameTree[j].minimaxVal
    return min

def getMax(i):
    max = -1
    for j in gameTree[i].childN:
        #print("%d līmenis, %d elements: %d" % (gameTree[i].level, i, j))
        if gameTree[j].minimaxVal > max:
            max = gameTree[j].minimaxVal
    return max

def createMiniMax(start):
    bottomLvl = gameTree[len(gameTree) - 1].level
    for i in range(len(gameTree)-1,-1,-1):
        if (gameTree[i].level == bottomLvl):
            gameTree[i].minimaxVal = getMiniMax(gameTree[i].virkne, start)
        else:
            if start == 1:
                if gameTree[i].level%2 == 1:
                    gameTree[i].minimaxVal = getMin(i)
                else:
                    gameTree[i].minimaxVal = getMax(i)
            else:
                if gameTree[i].level%2 == 1:
                    gameTree[i].minimaxVal = getMax(i)
                else:
                    gameTree[i].minimaxVal = getMin(i)
    for i in range(0, len(gameTree)):
        if gameTree[i].minimaxVal == -1:
            winNodes.append(i)

def printMiniMaxVal():
    print('\n--------------------| START - 0 |--------------------')
    print(("%d(%d)") % (gameTree[0].minimaxVal, 0), end="")
    for j in range(1, len(gameTree)):
        if gameTree[j].level != gameTree[j - 1].level:
            print('\n--------------------------' + str(gameTree[j].level) + '--------------------------')
        print("%s(%d)" % (gameTree[j].minimaxVal, j), end=" ")
    print('\n-------------------------END-------------------------')

def AIdecide(avirkne):
    print("AI decide...")
    for i in range(0, len(gameTree)):
        if gameTree[i].virkne == avirkne:
            break
    print(gameTree[i].childN)
    for j in range(0, len(gameTree[i].childN)):
        for uzv in winNodes:
            if gameTree[i].childN[j] == uzv:
                index = gameTree[i].childN[j]
                return gameTree[index].virkne
    for j in range(0, len(gameTree[i].childN)):
        print("Can't find optimal route")
        index = gameTree[i].childN[0]
        return gameTree[index].virkne

# Spēles izveide pirms interfeisa izveidošanas, lai varētu pārbaudīt procesu
def startGame(svirkne, start):
    createTree(svirkne)
    createMiniMax(start)
    printTree()
    printMiniMaxVal()
    print(winNodes)
    avirkne = svirkne
    print(avirkne)
    while len(avirkne) >= 3:
        if start == -1:
            avirkne = AIdecide(avirkne)
            print(avirkne)
            if len(avirkne) == 3:
                break
        izv = int(input("Izvēlies pāri: ")) - 1
        izv = izv * 2
        if izv == len(avirkne) - 1 and len(avirkne) % 2 == 1:
            avirkne = avirkne[0:len(avirkne) - 1]
        else:
            avirkne = avirkne[0:izv] + saskaite(avirkne[izv], avirkne[izv + 1]) + (avirkne[izv + 2:len(avirkne)])
        print(avirkne)
        if start == 1:
            if len(avirkne) == 3:
                break
            avirkne = AIdecide(avirkne)
            print(avirkne)
    if int(avirkne)%2 == 0:
        if start == 1:
            print("Cilvēks uzvarēja!")
        else:
            print("Programma uzvarēja!")
    else:
        if start == 1:
            print("Programma uzvarēja!")
        else:
            print("Cilvēks uzvarēja!")

def createRandomStart():
    import random
    x = ""
    for _ in range(random.randint(8, 12)):
        x += str(random.randint(1, 6))
    return x

def checkVirkne(virkne):
    try:
        for i in range(0, len(virkne)):
            if int(virkne[i]) < 1 or int(virkne[i]) > 6:
                return False
        return True
    except:
        return False

#startGame("1234134512", -1)

if __name__ == '__main__':
    import GUI
    GUI.vp_start_gui()

# TODO Min/Max funkction (sākumā dabūt bottomLvl // gnjau bottomLvl = gameTree[len(gameTree)-1].level
# TODO Grafiskais interfeiss
