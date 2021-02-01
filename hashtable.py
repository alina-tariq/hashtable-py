def hashFunc(key):
    pos = ((3 * key) + 5) % 11

    return pos

def secHash(key):
    pos = 7 - (key % 7)

    return pos

def sepChain(values):
    hashTable = [[],] * len(values)
    pos = [hashFunc(value) for value in values]

    for a in range(len(pos)):
        if not hashTable[pos[a]]:
            hashTable[pos[a]] = [values[a]]
        else:
            hashTable[pos[a]].append(values[a])

    return hashTable

def linProbe(values):
    hashTable = [[], ] * len(values)
    pos = [hashFunc(value) for value in values]

    for a in range(len(pos)):
        if not hashTable[pos[a]]:
            hashTable[pos[a]] = values[a]
        else:
            pos[a] = newPosLin(hashTable, pos[a])
            hashTable[pos[a]] = values[a]

    return hashTable

def newPosLin(hashTable, startPos):
    totInd = len(hashTable)
    startPos += 1

    for a in range(totInd - 1):
        newPos = (startPos + a) % totInd
        if not hashTable[newPos]:
            return newPos

def dblHash(values):
    hashTable = [[], ] * len(values)
    pos = [hashFunc(value) for value in values]

    for a in range(len(pos)):
        if not hashTable[pos[a]]:
            hashTable[pos[a]] = values[a]
        else:
            pos[a] = newPosDbl(hashTable, pos[a], secHash(values[a]))
            hashTable[pos[a]] = values[a]

    return hashTable

def newPosDbl(hashTable, firstHash, secondHash):
    totInd = len(hashTable)
    secondHash = secondHash % totInd

    for i in range(totInd):
        newPos = (firstHash + (i * secondHash)) % totInd
        if not hashTable[newPos]:
            return newPos


def hashSequence(hashTable):
    for a in range(len(hashTable)):
        if hashTable[a]:
            vals = hashTable[a]
        else:
            vals = [None]
        print("{0} -> \t {1}".format(a, vals))

values = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
print("Hash Tables:")
print(" ")

print("Separate Chaining:")
print("-"*22)
hT = sepChain(values)
hashSequence(hT)
print(" ")

print("Linear Probing:")
print("-"*15)
hT = linProbe(values)
hashSequence(hT)
print(" ")

print("Double Hashing:")
print("-"*15)
hT = dblHash(values)
hashSequence(hT)
