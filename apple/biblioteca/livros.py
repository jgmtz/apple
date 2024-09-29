"""
Módulo: Livros
Data: 08/06/2024
Versão: 4.0
Descrição: Efetua o cadastro, busca, lista e remoção dos livros
Alunos: Enzo Watanabe de Lima, Rafael Zeni e João Salomão
"""

import pickle as p
import os

# Lista com todos os livros e seus dados guardados e organizados
listao = []

def iniciar_livros():
    """
    Cria se necessário o arquivo livros.pkl e se ele estiver vazio, evita erro
    """
    global listao
    if os.path.isfile('livros.pkl') and os.path.getsize('livros.pkl') > 0:
        try:
            with open('livros.pkl', 'rb') as f:
                listao = p.load(f)
        except (EOFError, p.UnpicklingError) as e:
            print("Erro ao carregar os dados do arquivo:", e)
            listao = []
    else:
        listao = []


def menu_livros():
    """
    Faz o menu da funcionalidade livros
    """

    iniciar_livros()
    while True:
        try:
            print("\nMenu de Gerenciamento de Livros")
            print("1. Cadastrar Livros\n2. Listar Livros\n3. Remover Livros\n4. Sair")
            selecao = input("Selecione o que deseja realizar: ")
            if selecao == "1":
                cadastro_livros()
            elif selecao == "2":
                listar_livros()
            elif selecao == "3":
                remover_livros()
            elif selecao == "4":
                print("Saindo...")
                break
            else:
                print("Valor inválido, selecione novamente!")
        except ValueError:
            print("Erro, tente novamente!")

def cadastro_livros():
    """
    Realiza o cadastro dos livros, pedindo o nome, autor e gênero, e armazena em uma lista chamada listao
    """
    while True:
        try:
            livro = []
            # Adiciona os livros na lista
            while True:
                novos_livros = input("\nInsira o nome do livro para cadastro: ")
                if novos_livros == "":
                    print("Deve ser inserido um nome para o livro!")
                    continue
                else:
                    break
            livro.append(f"{novos_livros}")
            # Adiciona os autores na lista
            while True:
                autores_livros = input("Insira o autor(a) deste livro: ")
                if autores_livros == "":
                    print("Deve ser inserido um nome para o(a) autor(a) do livro!")
                    continue
                else:
                    break
            livro.append(f"Autor: {autores_livros}")
            # Adiciona os gêneros na lista
            while True:
                genero_livros = input("Insira o gênero deste livro: ")
                if genero_livros == "":
                    print("Deve ser inserido um gênero para o livro!")
                    continue
                else:
                    break
            livro.append(f"Gênero: {genero_livros}")

            print("Cadastro Concluído!")
            listao.append(livro)

            termino = input("Deseja continuar cadastrando livros? (s/n): ")
            while True:
                if termino.lower() == "n" or termino.lower() == "s":
                    break
                else:
                    print("Resposta inválida, selecione uma opção entre (s/n): ")
                    termino = input("Deseja continuar cadastrando livros? (s/n): ")
            if termino.lower() == "n":
                break
        except ValueError:
            print("Inválido")
    with open('livros.pkl', 'wb') as f:
        p.dump(listao, f)

def listar_livros():
    """
    Faz a listagem com o nome de todos os livros que foram cadastrados
    """
    if not listao:
        print("Sem livros na lista!")
    else:
        print("Lista de Livros Disponíveis:")
        for i, livro in enumerate(listao):
            print(f"{i+1}. Livro: {livro[0]}")

def remover_livros():
    """
    Remove algum livro que o usuário selecionar
    """
    if not listao:
        print("Sem livros para remover!")
        return
    
    listar_livros()
    
    try:
        remover = int(input("\nSelecione o número do livro que deseja remover (0 para sair): "))
        if remover == 0:
            return
        
        if 0 < remover <= len(listao):
            #Função para remover o livro da lista
            livro_removido = listao.pop(remover - 1)
            print(f"Livro '{livro_removido[0]}' removido com sucesso!")
            

        else:
            print("Número de livro inválido!")
    except ValueError:
        print("Erro: insira um número válido correspondente a algum livro!")
    with open('livros.pkl', 'wb') as f:
        p.dump(listao, f)
