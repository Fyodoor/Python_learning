a=int(input())
hour=int(a/3600)
hour1=float(a/3600)
minute=hour1-hour
minute1=minute*60
minute2=int(minute1)
sec=minute1-minute2
sec1=int(sec*60)
print(a, "секунд - это", hour, "час", minute2, "минут", sec1, "сек")