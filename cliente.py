import socket
import os
import sys

MAX_MESSAGE_SIZE = 1024
SERVIDOR_HOST = 'localhost'
SERVIDOR_PORTA = 8888

if len(sys.argv) == 2:
    SERVIDOR_HOST = sys.argv[1]
elif len(sys.argv) == 3:
    SERVIDOR_HOST = sys.argv[1]
    SERVIDOR_PORTA = int(sys.argv[2])

CODIGOS_SERVIDOR = {
    '200': 'Cliente registrado com sucesso!', # resposta padrão
    '201': 'Cliente já registrado!', # verificação
    '202': 'Operação realizada com sucesso!', # aceito
    '203': 'Item indisponível.', # não autorizado
    '204': 'Cliente desconectado!', # nenhum conteudo
    '205': 'Faça uma nova solicitação.', # resetar conteudo ###
    '206': 'Ainda há itens disponíveis.', # conteudo parcial 
    '207': 'Cardápio entregue!', # cardápio entregue com sucesso
    '208': 'O pedido contém os seguintes itens.', # indica que o estado de um recurso já foi relatado em uma resposta anterior.
    '400': 'Item inválido.', # erro do cliente 
    '401': 'Produto não encontrado no nosso menu!', # não encontrado
    '402': 'Ainda não é possível entregar o pedido.', # pagamento necessário
    '409': 'Item já está cadastrado.', # o item ja esta cadastrado no cardapio
}



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # função para limpar tela do console

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVIDOR_HOST, SERVIDOR_PORTA))

    mensagem_servidor = client_socket.recv(MAX_MESSAGE_SIZE).decode()
    print(mensagem_servidor)

    def enviar_mensagem(mensagem):
        client_socket.send(mensagem.encode())
        return client_socket.recv(MAX_MESSAGE_SIZE).decode()

    resposta = enviar_mensagem(f"REGISTRAR {input_celular()}")
    print(CODIGOS_SERVIDOR[resposta])
   
    while True:
        choice = mostrar_menu()

        if choice == '1':
            limpar_tela()
            codigo, resposta = enviar_mensagem("OPCOES").split("-", 1)
            print(resposta)
            print(CODIGOS_SERVIDOR[codigo])

        elif choice == '2':
            limpar_tela()
            codigo = enviar_mensagem(f"PEDIR {input_pedido()}")
            print(CODIGOS_SERVIDOR[codigo])
           

        elif choice == '3':
            limpar_tela()
            codigo = enviar_mensagem(f"CADASTRAR / {input_cadastro()}")
            print(CODIGOS_SERVIDOR[codigo])

        elif choice == '4':
            resposta = enviar_mensagem("SAIR")
            if resposta == "204":
                break

        else:
            limpar_tela()
            print("Opção inválida! Tente novamente.")

    client_socket.close()

def input_pedido():
    while True:
        pedido = input("Digite o nome do prato desejado: ").title()
        if pedido.isalpha():
            limpar_tela()
            return pedido
        else:
            print("Entrada inválida. Digite apenas letras.")


def input_cadastro():
    while True:
        pedido = input("Digite o prato que deseja cadastrar (separe o nome e a descrição do prato com /): ").title()
        if '/' in pedido:
            limpar_tela()
            return pedido
        else:
            print("Entrada inválida. Não esqueça de separar o nome e a descrição com /.")


def input_celular():
    celular = input("Digite seu celular: ")
    while not valida_celular(celular):
        limpar_tela()
        print("celular inválido! Tente novamente.")
        celular = input("Digite seu celular: ")
    return celular

def valida_celular(_celular):
    if len(_celular) == 9 and _celular.isdigit():
        return True
    else:
        return False

def cardapio_esgotado(resposta):
    if resposta == "205":
        print("Cardápio esgotado, o pedido não pode ser entregue")
        return True
    else:
        return False

def mostrar_menu():
    print('''
    1 - Ver cardápio
    2 - Realizar pedido
    3 - Cadastrar item no cardápio
    4 - Sair
    ''')
    choice = input("Digite a opção desejada: ")
    return choice

if __name__ == '__main__':
    main()