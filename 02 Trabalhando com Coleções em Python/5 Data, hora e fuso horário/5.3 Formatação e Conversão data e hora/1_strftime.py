import datetime

data_hora = datetime.datetime.now()

# Formatando data e hora
print(data_hora.strftime("%d/%m/%Y %H:%M"))

# Formatando data e hora com dia da semana
print(data_hora.strftime("%d/%m/%Y %a %H:%M"))