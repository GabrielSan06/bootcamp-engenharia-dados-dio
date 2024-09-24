# pip install pytz

import datetime
import pytz

# Criando datetime com timezone
data_hora = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data_hora)