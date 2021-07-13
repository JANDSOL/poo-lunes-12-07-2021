class Order:
    def __init__(self, ls):
        self._list = ls
    
    def bubble(self):
        for i in range(len(self._list)):
            for j in range(i+1, len(self._list)):
                if self._list[i] > self._list[j]:
                    aux = self._list[i]
                    self._list[i] = self._list[j]
                    self._list[j] = aux
    
    def insert(self, value):
        self.bubble()

ord1 = Order([0, 2, 6, 8])
ord1.insert(5)
ord1.bubble()
print(ord1._list)
