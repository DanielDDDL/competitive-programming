# uma fila cinco quatro operações básicas
# enqueue, dequeue, first, isEmpty, isFull,
# enqueue - acrescenta um item na parte da frente da fila
# dequeue - remove um item da parte da trás da fila
# first - retorna o primeiro da fila
# isEmpty - retorna true se a fila se esta vazia; caso contrário, False
# isFull - retorna True se a fila esta cheia; caso contrário, False

import random # for tests purposes

class Queue:
    def __init__(self, qnt_items):
        self.qnt_items = qnt_items
        self.items = [None] * qnt_items
        self.first_line = 0
        self.last_line  = -1
        self.size = 0

    def is_empty (self):
        return self.size == 0

    def is_full (self):
        return self.size == self.qnt_items

    def first (self):
        if self.is_empty():
            raise RuntimeError ("Attempt to get the first item of an empty line")
        else:
            return self.items[self.first_line]

    def enqueue (self, item):
        if self.is_full():
            raise RuntimeError ("Attempt to enqueue an item in a full queue")
        else:
            # because the queue is circular
            # index of the last item comes back to the start if there is room for it
            if self.last_line + 1 == self.qnt_items:
                self.last_line = 0
            else:
                self.last_line += 1

            self.items[self.last_line] = item
            self.size += 1

    def dequeue (self):
        if self.is_empty():
            raise RuntimeError ("Attempt to dequeue an item from a full queue")
        else:
            # because the queue is circular
            # index of the first item comes back to the start if there is room for it
            self.items[self.first_line] = None
            self.size -= 1
            if self.first_line == self.qnt_items - 1:
                self.first_line = 0
            else:
                self.first_line += 1



    def __str__ (self):
        info  = "Items of the queue: " + str(self.items)
        info += "\nIndex of the first item: " + str(self.first_line)
        info += "\nIndex of the last item:" + str(self.last_line)
        info += "\nSize of the queue: " + str(self.size)
        info += "\nMax quantity of items allowed: " + str(self.qnt_items)
        return info

# ---------- TESTS ------------ #
def main ():
    size = int(input("Type in the size of the queue: "))
    f = Queue(size)
    print ("------PRINTING INSERTION-------")
    for i in range (size):
        f.enqueue(random.randint(1,10))
        print (f.first())

    #printing all the items of queue
    print (f)

    print ("------PRINTING REMOVAL-------")
    for i in range (size):
        print (f.first())
        f.dequeue()

    #printing all the items of queue
    print (f)

if __name__ == "__main__":
    main()
