from datetime import datetime
import hashlib

class Bloco:

    def __init__(self, indice, hash_anterior, dados):
        self.indice = indice
        self.timestamp = datetime.utcnow().timestamp()
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.valor_pow = 0
        self.hash = self.calcular_hash()
    
    def print_bloco(self):
	    print("Índice:", self.indice)
	    print("Timestamp:", self.timestamp)
	    print("Dados:", self.dados)
	    print("Hash anterior:", self.hash_anterior)
	    print("Hash:", self.hash)
	    print("Valor pow:", self.valor_pow)

    def calcular_hash(self):
        hash_calculado = []
        while(hash_calculado[:4] != "aaaa"):
            dados_hash = (str(self.indice) + str(self.timestamp) + str(self.dados) + str(self.hash_anterior) + str(self.valor_pow))
            hash_calculado = hashlib.sha256(dados_hash.encode("UTF-8")).hexdigest()
            self.valor_pow += 1
        return hash_calculado


