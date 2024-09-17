def salvar_carro(marca, modelo):
	#salva carro no banco de dados...
	print(f"Carro inserido com sucesso! {marca}/{modelo}")
	
salvar_carro("Fiat", "Palio")
salvar_carro(marca="Fiat", modelo="Palio")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio"})