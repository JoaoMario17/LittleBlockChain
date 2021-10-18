from Bloco import Bloco

class BlockChain:

    blocos = []

    def __init__(self):
        self.criar_bloco_genesis()

    def criar_bloco_genesis(self):
	    genesis = Bloco(0, 0, "Gênesis")
	    self.blocos.append(genesis)

    def print_blocos(self):
        for bloco in self.blocos:
            bloco.print_bloco()
            print()

    def add_bloco(self, bloco):
	    if(self.bloco_valido(bloco)):
		    self.blocos.append(bloco)

    def bloco_valido(self, bloco):
	    for bl in self.blocos: 
		    if bl.indice == bloco.indice:
			    return False
	    if bloco.hash[:4] != "aaaa":
		    return False
	    return True

    def get_ultimo_hash(self):
	    return self.blocos[-1].hash

    def get_ultimo_indice(self):
	    return self.blocos[-1].indice


my_blockchain = BlockChain()

bloco1 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Roger", "apelido": "Mr.R"});
my_blockchain.add_bloco(bloco1)
bloco2 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Lúcia", "apelido": "LadyLucy"});
my_blockchain.add_bloco(bloco2)
bloco3 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Carlos", "apelido": "ElCarlito"});
my_blockchain.add_bloco(bloco3)
bloco4 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Roger", "apelido": "Moscou"});
my_blockchain.add_bloco(bloco4)

my_blockchain.print_blocos()