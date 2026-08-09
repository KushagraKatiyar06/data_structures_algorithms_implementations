# hash table implementation with separate chaining collision handling

class HashTable:
    def __init__(self, size = None):
        self.size = size
        self.array = [[] for i in range(self.size)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size
    
    def __setitem__(self, key, val):
        h = self.getHash(key)
        found = False

        for index, pair in enumerate(self.array[h]):
            if len(self.array[h][index]) == 2 and pair[0] == key:
                self.array[h][index][1] = val
                found = True
                break
        if not found:
            self.array[h].append([key, val])


    def __getitem__(self, key):
        h = self.getHash(key)

        if (len(self.array[h]) == 1):
            return self.array[h][0][1]
        else:
            for i in range(len(self.array[h])):
                if self.array[h][i][0] == key:
                    return self.array[h][i][1]
    
    
    def remove(self, key):
        h = self.getHash(key)
        self.array[h] = None

    def printArray(self):
        for i in range(len(self.array)):
            print(self.array[i])

if __name__ == '__main__':
    t = HashTable(10)

    t['march 6'] = 120
    t['march 6'] = 78
    t['march 8'] = 67
    t['march 9'] = 4
    t['march 17'] = 459

    print()
    t.printArray()

    print(t['march 6'])
    print(t['march 8'])
    print(t['march 17'])


    


