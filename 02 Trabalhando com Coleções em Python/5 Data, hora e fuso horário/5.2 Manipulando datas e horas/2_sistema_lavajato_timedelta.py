# SISTEMA PARA LAVA JATO COM ESTIMATIVA PARA O CLIENTE BUSCAR O CARRO

# Importando datetime e timedelta do módulo datetime
from datetime import datetime, timedelta
tipo_carro = "P"

# Tempo levado na lavagem de cada carro de acordo com o tamanho
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

# Guardando data e hora atual em uma variável
data_atual = datetime.now()


# Condicional para adicionar o tempo levado na lavagem com o horário atual dependendo do tamanho do veículo
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")