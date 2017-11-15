day_event_1  = int(input().rstrip().split(" ")[1])
info_event_1 = [int(x) for x in input().rstrip().split(" : ")]

day_event_2  = int(input().rstrip().split(" ")[1])
info_event_2 = [int(x) for x in input().rstrip().split(" : ")]

second = 1
minute = second * 60
hour   = minute * 60
day    = hour   * 24

units_day_1 = info_event_1[2] * second + info_event_1[1] * minute + info_event_1[0] * hour + day_event_1 * day
units_day_2 = info_event_2[2] * second + info_event_2[1] * minute + info_event_2[0] * hour + day_event_2 * day

difference = units_day_2 - units_day_1

dif_days = 0
while difference >= day:
    dif_days += 1
    difference -= day

dif_hours = 0
while difference >= hour:
    dif_hours += 1
    difference -= hour

dif_minutes = 0
while difference >= minute:
    dif_minutes += 1
    difference -= minute

dif_seconds = 0
while difference >= second:
    dif_seconds += 1
    difference -= second

print(dif_days, "dia(s)")
print(dif_hours, "hora(s)")
print(dif_minutes, "minuto(s)")
print(dif_seconds, "segundo(s)")

# time stamp sent their regards!
