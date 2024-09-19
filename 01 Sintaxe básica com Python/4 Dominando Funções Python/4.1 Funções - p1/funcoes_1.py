def exibir_mensagem():
	print("Olá mundo!")

# Parâmetro obrigatório
def exibir_mensagem_2(nome):
	print(f"Seja bem vindo {nome}!") 

# Parâmetro opcional
def exibir_mensagem_3(nome="Anônimo"):
	print(f"Seja bem vindo {nome}!") 
	

# Chamando a função 1
# exibir_mensagem()

# Chamando a função com parâmetro obrigatório
# exibir_mensagem_2(nome="Gabriel")

# Chamando a função com parâmetro opcional
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Chappie")



# Retornando o a soma dos números da lista
def calcular_total(numeros):
	return sum(numeros)
	
# Retornando mais de um valor de uma só vez
def retorna_antecessor_e_sucessor(numero):
	antecessor = numero - 1
	sucessor = numero + 1
	
	return antecessor, sucessor

# Chamando as funções
calcular_total([10, 20, 34]) 
retorna_antecessor_e_sucessor(10) 