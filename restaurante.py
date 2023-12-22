
from estruturas.hash_table import *

class Prato:
    def __init__(self, nome, descricao, preco): 
        self.__nome = nome.strip()
        self.__descricao = descricao
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
            self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao_atualizada):
            self.__descricao = descricao_atualizada


    def __str__(self):
        return f'Prato: {self.__nome}. Descrição: {self.__descricao}.'

 
class Restaurante:
    def __init__(self, cardapio):
        self.__cardapio = cardapio  #Atribui o cardapio do restaurante a hash table que é inicializada como cardapio

    def exibir_menu(self):
        for chave, descricao_recuperada in cardapio.items():
            yield f"Prato: {chave}. Descrição: {descricao_recuperada}"
  

         

#Inicializando o cardapio como uma hash table
cardapio = TabelaHash(30)

#Criando todos os pratos do restaurante como objetos da classe Prato
pratos = [
    Prato("Spaghetti Carbonara", "Massa com molho à base de ovos, queijo parmesão e bacon")
    Prato("Pizza Margherita", "Pizza com molho de tomate, queijo mozzarella e manjericão fresco")
    Prato("Risoto De Funghi", "Arroz arbóreo cozido com cogumelos funghi, creme de leite e queijo parmesão")
    Prato("Lasanha A Bolonhesa", "Camadas de massa intercaladas com molho de carne à bolonhesa e queijo")
    Prato("Tiramisu", "Sobremesa italiana à base de café, queijo mascarpone e cacau")
    Prato("Bruschetta", "Fatias de pão italiano grelhado com tomate, azeite de oliva, alho e manjericão")
    Prato("Cannoli", "Massa crocante recheada com creme de ricota e frutas cristalizadas")
    Prato("Ravioli de Ricota e Espinafre", "Massa recheada com ricota e espinafre, servida com molho de tomate fresco")
    Prato("Gelato", "Sorvete italiano em diversos sabores")
    Prato("Negroni", "Coquetel italiano feito com gin, vermute e Campari")
    Prato("Limoncello", "Licor italiano de limão")
]

# Adicionando os pratos ao cardápio
for prato in pratos:
    cardapio.put(prato.nome, prato.descricao)




