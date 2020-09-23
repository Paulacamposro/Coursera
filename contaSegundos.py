contaSeg = int(input("Por favor, entre com o número de segundos que deseja converter:"))

a = contaSeg//86400
restase = contaSeg%86400
b = restase//3600
restho = restase%3600
c = restho//60
d = restho%60

print(a,"dias,",b,"horas,",c,"minutos","e",d,"segundos.")
