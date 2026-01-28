class Utente: 

	def __init__(self, nome): 
		self.nome = nome

	def __repr__(self): 
		return f"Utente(nome={self.nome})"

	# Due oggetti sono uguali se hanno lo stesso nome. 
	# Approccio molto didatitco
	def __eq__(self, other):
		if not isinstance(self,other): 
			return False

		# Torna implicitamente True se uguaglianza
		# va a buon fine
		return self.nome == other.nome
