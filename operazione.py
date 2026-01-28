from datetime import datetime

class Operazione: 

	def __init__(self, tipo, importo): 
		self.tipo = tipo 
		self.importo = importo 
		self.data = datetime.now()

	def __eq__(self,other): 
		if not isinstance(self,other): 
			return False

		# Due operazioni sono la stessa operazione se tutte le variabili di istanza coincidono (didattico)
		return self.tipo == other.tipo and 
			   self.importo == other.importo and 
			   self.data == other.data

    def __repr__(self): 
    	return f"Operazione(tipo={self.tipo},importo={self.importo},data={self.data})"