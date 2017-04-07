# uma fila cinco quatro operações básicas
# enqueue, dequeue, first, isEmpty, isFull,
# enqueue - acrescenta um item na parte da frente da fila
# dequeue - remove um item da parte da trás da fila
# first - retorna o primeiro da fila
# isEmpty - retorna true se a fila se esta vazia; caso contrário, False
# isFull - retorna True se a fila esta cheia; caso contrário, False

import random # for tests purposes

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty (self):
        return len(self.items) == 0

    def first (self):
        if self.is_empty():
            raise RuntimeError ("Attempt to get the first item of an empty line")
        else:
            return self.items[0]

    def enqueue (self, item):
        self.items.append(item)

    def dequeue (self):
        if self.is_empty():
            raise RuntimeError ("Attempt to dequeue an item from a full queue")
        else:
            # just deleting the first item of the list
            # the rest is shifted along, so the indexes are fine
            del self.items[0]

    def __str__ (self):
        info  = "Items of the queue: " + str(self.items)
        info += "\nSize of the queue: " + str(len(self.items))
        return info

# ---------- TESTS ------------ #
def main ():
    f = Queue()
    print ("------PRINTING INSERTION-------")
    for i in range (10):
        f.enqueue(random.randint(1,10))
        print (f.first())

    print (f)

    print ("------PRINTING REMOVAL-------")
    for i in range (10):
        print (f.first())
        f.dequeue()

    print (f)

if __name__ == "__main__":
    main()
