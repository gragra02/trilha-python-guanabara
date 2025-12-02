from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção ler arquivo
        lerArquivo(arq)
    elif resposta == 2:
       #opção cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo')
        break
    else:
        print('\033[0;31mERRO: Por favor, digite uma opção válida.\033[m')
    sleep(2)

