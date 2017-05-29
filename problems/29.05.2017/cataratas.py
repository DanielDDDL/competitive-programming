def calcula_quantidade_maiores_menores(valor,valores_vazao):
    maiores = 0
    menores = 0
    for i in range(len(valores_vazao)):
        if (valor >= valores_vazao[i]):
            maiores += 1
        if (valor <= valores_vazao[i]):
            menores += 1

    #tirando o proprio valor
    maiores -= 1
    menores -= 1
    return [maiores,menores]

def calcular_quantidade_balanceamento(valor_necessario, vasao_vigente):
    maiorB = 0
    for i in range(len(vasao_vigente)):
        consulta_aparicoes = calcula_quantidade_maiores_menores(vasao_vigente[i],vasao_vigente)
        if (valor_necessario <= consulta_aparicoes[0] and valor_necessario <= consulta_aparicoes[1]):
            if (vasao_vigente[i] > maiorB):
                maiorB = vasao_vigente[i]

    return maiorB

#inicio do processamento
info_dias = [int(x) for x in input().rstrip().split(" ")]
info_vazao = [int(x) for x in input().rstrip().split(" ")]

ultimo_dia_possivel = info_dias[0] - info_dias[1] + 1

valor_necessario = (info_dias[1] - 1) / 2

#valores iniciais
info_vazao_utilizada = info_vazao[:info_dias[1]]
qnt_bal = calcular_quantidade_balanceamento(valor_necessario,info_vazao_utilizada)
maior = qnt_bal

for i in range(1,ultimo_dia_possivel):

    del info_vazao_utilizada[0]
    info_vazao_utilizada.append(info_vazao[i + info_dias[1] - 1])

    qnt_bal = calcular_quantidade_balanceamento(valor_necessario, info_vazao_utilizada)
    if (qnt_bal > maior):
        maior = qnt_bal

print (maior)
