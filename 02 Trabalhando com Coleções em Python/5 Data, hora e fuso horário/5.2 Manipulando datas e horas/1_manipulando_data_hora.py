from datetime import datetime, timedelta

data_hora = datetime(2024, 9, 24, 10, 50)
print (data_hora)

# Adicionando uma semana 
data_hora += timedelta(weeks=1)
print(data_hora)