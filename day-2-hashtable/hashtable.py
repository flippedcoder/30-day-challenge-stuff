class HashTable:
    def __init__(self, size):
        self._size = 0
        self._table = [None] * size

    def _hash(self, key):
        hash = 0
        key_str = str(key)

        for char in key_str:
            hash += ord(char)
        
        return hash % len(self._table)
    
    def set(self, key, value):
        index = self._hash(key)

        if self._table[index] is not None:
            for pair in self._table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self._table[index].append([key, value])
        else:
            self._table[index] = []
            self._table[index].append([key, value])

        self._size += 1

    def get(self, key):
        index = self._hash(key)

        if self._table[index] is not None:
            for pair in self._table[index]:
                if pair[0] == key:
                    return pair[1]
        
        return None
    
    def remove(self, key):
        index = self._hash(key)

        if self._table[index] is not None:
            for i, pair in enumerate(self._table[index]):
                if pair[0] == key:
                    self._table[index].pop(i)

                    self._size -= 1

                    return True
        else:
            return False
        
    def display(self):
        for ind, values in enumerate(self._table):
            if values:
                chained_values = [f"[{key}: {value}]" for key, value in values]

                print(f"{ind}: {chained_values}")

hashtable = HashTable(127)

hashtable.set('Tony', 111)
hashtable.set('Toni', 192)
hashtable.set('Tone', 150)

hashtable.display()

hashtable.remove('Tone')
hashtable.display()
