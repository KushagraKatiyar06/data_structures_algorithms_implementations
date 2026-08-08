# basic hash table implementation with no collision handling

class HashTable:
    def __init__(self, size = None):
        self.size = size
        self.array = [None for i in range(self.size)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size
    
    def __setitem__(self, key, val):
        h = self.getHash(key)
        self.array[h] = val
        return

    def __getitem__(self, key):
        return self.array[self.getHash(key)]
    
    def remove(self, key):
        h = self.getHash(key)
        self.array[h] = None
        return

    def printArray(self):
        for i in range(len(self.array)):
            print(self.array[i])
        return

if __name__ == '__main__':
    t = HashTable(10)
    print(t.getHash('march 6'))

    t['march 6'] = 310
    print(t['march 6'])

    print()
    t.printArray()

    print()
    t.remove('march 6')
    print(t['march 6'])
    t.printArray()

    


