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
        aux_list = []
        enc = False
        for pos, ele in enumerate(self._list):
            if ele > value:
                aux_list.append(value)
                enc = True
                break
        if enc: self._list = self._list[0:pos] + aux_list + self._list[pos:]
        else: self._list.append(value)
        return self._list

    def insert2(self, value):
        self.bubble()
        aux_list = []
        enc = False
        for pos, ele in enumerate(self._list):
            if ele > value:
                enc = True
                break
        if enc:
            for i in range(pos):
                aux_list.append(self._list[i])
            aux_list.append(value)
            for j in range(pos, len(self._list)):
                aux_list.append(self._list[j])
            self._list = aux_list
            self._list = self._list[0:pos] + aux_list + self._list[pos:]
        else:
            self._list.append(value)
        return self._list


ord1 = Order([10, 15, 20, 70, 80])
ord1.insert(5)
ord1.bubble()
print(ord1._list)
