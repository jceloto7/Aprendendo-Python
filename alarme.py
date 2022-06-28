hora0=int(input("Por favor, digite o horário atual:"))
alarme=int(input("Agora digite em quantas horas deseja que o alarme toque:"))
hora1=alarme%24
hora_final=hora0+hora1
print("Seu alarme tocará ás",hora_final,"horas.")