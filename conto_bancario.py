class ContoBancario:

	def __init__(self, numero_conto, utente): 
		self.numero_conto = numero_conto 
		self.utente = utente 
		self.saldo = 0
		self.operazioni = []

	def __eq__(self,other): 
		if not isinstance(self,other): 
			return False

		return self.numero_conto == other.numero_conto

    def __repr__(self): 
    	return f"ContoBancario(numero_conto={self.numero_conto},utente={self.utente},saldo={self.saldo})"


    def versamento(self, importo): 
    	pass

    def prelievo(self, importo):
    	pass 

    def visalizzaSaldo(self):
    	pass

    def visualizzaStorico(self): 
    	pass