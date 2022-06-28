s_str=input("Por favor, entre com o número de segundos que deseja converter:" )
s_int=int(s_str)
a=s_int//86400
diasr=s_int%86400
b=diasr//3600
horasr=diasr%3600
c=horasr//60
d=horasr%60
print(a,"dias,",b,"horas,",c,"minutos","e",d,"segundos.")