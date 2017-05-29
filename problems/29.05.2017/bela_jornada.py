# leitura
qnt_checkpoints = int(input().rstrip())
valores = [int(x) for x in input().rstrip().split(" ")]

lado_esquerdo = []
lado_esquerdo.append(valores[0])
lado_direito = valores[1:]

#valores iniciais
soma_esquerda = sum(lado_esquerdo)
soma_direita = sum(lado_direito)
menor_diferenca = abs(soma_esquerda - soma_direita)

cand_esquerda = soma_esquerda
cand_direita = soma_direita
while len(lado_direito) >= 1 and menor_diferenca != 0:

    soma_esquerda += lado_direito[0]
    soma_direita -= lado_direito[0]
    del lado_direito[0]

    if (menor_diferenca > abs(soma_esquerda - soma_direita)):
        menor_diferenca = abs(soma_esquerda - soma_direita)
        cand_esquerda = soma_esquerda
        cand_direita = soma_direita

print(cand_esquerda * cand_direita)
