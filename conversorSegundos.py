conversorseg = int(input("Entre com o numero de segundos que deseja converter: "))

horas = conversorseg//3600
restsegh = conversorseg % 3600

minutos = restsegh/60
restsegm = restsegh % 60

print(horas, "horas", minutos, "minutos", restsegm, "segundos")
