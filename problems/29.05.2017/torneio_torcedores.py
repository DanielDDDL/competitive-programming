# 1 para o primeiro time
# 2 para o segundo
def quem_vence (info_time_1, info_time_2):
    if (info_time_1[0] + info_time_1[1] >= info_time_2[0] + info_time_2[1]):
        return 1
    else:
        return 2

times = []
for i in range(1,5):
    time = [int(x) for x in input().rstrip().split(" ")]
    time.append(i) #identifcador
    times.append(time)

#semifinais
final = []
if (quem_vence(times[0], times[1]) == 1):
    times[0][1] -= times[1][1] #contando o peso contra da torcida rival na final
    final.append(times[0])
else:
    times[1][1] -= times[0][1]
    final.append(times[1])

if (quem_vence(times[2], times[3]) == 1):
    times[2][1] -= times[3][1]
    final.append(times[2])
else:
    times[3][1] -= times[2][1]
    final.append(times[3])

# final
if (quem_vence(final[0], final[1]) == 1):
    print(final[0][2])
else:
    print(final[1][2])
