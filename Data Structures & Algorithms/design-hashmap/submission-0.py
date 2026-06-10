class MyHashMap:

    def __init__(self):
        self.map =[]

    def put(self, key: int, value: int) -> None:
        for pair in self.map:
            if pair[0] == key:
                pair[1] = value
                return
        self.map.append([key, value])

    def get(self, key: int) -> int:
        for pair in self.map:
            if pair [0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:

        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)
                return
