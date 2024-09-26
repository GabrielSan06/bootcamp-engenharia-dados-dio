# pip install pytz

from datetime import datetime
import pytz

# Criando datetime com timezone
data_hora = datetime.now(pytz.timezone("Europe/Oslo"))
data_hora_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
data_hora_3 = datetime.now()


print(data_hora)
print(data_hora_2)
print(data_hora_3)