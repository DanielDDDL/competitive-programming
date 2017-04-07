# uma pilha tem quatro operações básicas
# push, pop, top, isEmpty, isFull,
# push - acrescentar um item no topo da pilha
# pop - remove o item do topo da pilha
# top - retorna o item no topo da pilha
# isEmpty - retorna true se a pilha se esta vazia; caso contrário, False
# isFull - retorna True se a pilha esta cheia; caso contrário, False
import random #usado na inseração

class Stack:
    def __init__ (self, qnt_items):
        self.qnt_items = qnt_items
        self.items = [None] * qnt_items
        self.top = -1

    def is_empty (self):
        return self.top == -1

    def is_full (self):
        return self.top == self.qnt_items - 1

    def top_item (self):
        if self.is_empty():
            raise RuntimeError("Attempt to get the top of an Empty stack")
        else:
            return self.items[self.top]

    def pop (self):
        if self.is_empty():
            raise RuntimeError("Attempt to pop on an empty stack")
        else:
            self.items[self.top] = None
            self.top -= 1

    def push (self, item):
        if self.is_full():
            raise RuntimeError("Attempt to push an item on a full stack")
        else:
            self.top += 1
            self.items [self.top] = item

    def __str__ (self):
        info  = "Vetor em si:" + str(self.items)
        info = info + "\nQuantidade de items permitidos:" + str(self.qnt_items)
        info = info + "\nValor do topo:" + str(self.top)
        return info

def main ():
    # -------------- TESTS --------------- #
    size = int(input("Type in the size of the stack: "))
    p = Stack(size) # definindo que a pilha possui dez items
    print ("---- PRINTIN INSERTION ----")
    for i in range (size):
        #exibindo os itens da lista conforme eles sao adicinados
        p.push(random.randint(1,10))
        print (p.top_item())

    #printing all the items inserted
    print (p)

    print ("---- PRINTING REMOVAL ----")
    for i in range (size):
        print (p.top_item())
        p.pop()

    print (p)

if __name__ == "__main__":
    main()
