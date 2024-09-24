from datetime import datetime as dt

date_string = "24/07/2024 11:38"

# Convertendo string para datetime
data_hora = dt.strptime(date_string, "%d/%m/%Y %H:%M")
print(data_hora)