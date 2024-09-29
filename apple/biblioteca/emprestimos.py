"""
Módulo: Emprestimos
Data: 08/06/2024
Versão: 4.0
Descrição: Efetua o emprestimo e devolução dos livros
Alunos: Enzo Watanabe de Lima, Rafael Zeni e João Salomão
"""

import pickle as p
import os
import livros as l
import utils as u

emprestimos = []

def verificar_cadastro():
    """
    Verifica se o usuário possui cadastro para empréstimo
    """
    usuarios = u.carregar_cadastro_usu()  
    while True:
        verificação_cadastro = input("Você possui cadastro? (s/n): ").lower()
        if verificação_cadastro == "s":
            informar_matricula = input('Digite o número de sua matrícula: ')
            for usuario in usuarios:
                if usuario["numero_matricula"] == informar_matricula:
                    return usuario  
            print("Usuário não encontrado.")
        elif verificação_cadastro == "n":
            print("Por favor, realize seu cadastro antes de emprestar algum livro")
            break

def verificar_livros_disponiveis():
    """
    Verifica se há livros disponíveis para que o empréstimo possa ser realizado
    """
    l.iniciar_livros() 
    if not l.listao:
        print("Sem livros na lista!")
        return None

    while True:
        l.listar_livros()
        escolher_livro = input('Escolha o número correspondente ao livro que você deseja: ')
        
        try:
            escolha_numero = int(escolher_livro)
            if escolha_numero <= 0 or escolha_numero > len(l.listao):
                print("Número de livro inválido, tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida, digite apenas o número do livro.")
            continue
        
        livro = l.listao[escolha_numero - 1]
        return livro


def realizar_emprestimo():
    """
    Efetua o empréstimo e remove o livro da lista de disponíveis
    """
    usuario = verificar_cadastro()
    if usuario is None:
        print("Não foi possível realizar o empréstimo.")
        return

    livro = verificar_livros_disponiveis()
    if not livro:
        return

    emprestimo = {
        "usuario": usuario["numero_matricula"],
        "livro": livro[0],
        "status": "emprestado"
    }
    
    emprestimos.append(emprestimo)
    with open('emprestimos.pkl', 'wb') as files:
        p.dump(emprestimos, files)
    print(f"Empréstimo realizado com sucesso! Usuário: {usuario['nome_completo']}, Livro: {livro[0]}")

    #Remove o livro emprestado da lista de livros disponíveis
    l.listao.remove(livro)
    with open('livros.pkl', 'wb') as files:
        p.dump(l.listao, files)
    print(f"Livro {livro[0]} removido da lista de livros disponíveis.")


def retornar_emprestimo():
    """
    Retorna o livro emprestado
    """
    usuarios = u.carregar_cadastro_usu()
    l.iniciar_livros()
    global emprestimos
    emprestimos = u.verificar_file_emprestimos()
    
    if not emprestimos:
        print("Não há empréstimos registrados.")
        return

    informar_matricula = input('Digite o número de sua matrícula: ')
    emprestimos_usuario = [e for e in emprestimos if e["usuario"] == informar_matricula]
    
    if not emprestimos_usuario:
        print("Nenhum empréstimo encontrado para este usuário.")
        return

    print("Empréstimos do usuário:")
    for i, emp in enumerate(emprestimos_usuario):
        print(f"{i+1}. {emp['livro']} - Status: {emp['status']}")

    while True:
        try:
            selecao = int(input("Selecione o número do empréstimo a ser retornado: "))
            if 1 <= selecao <= len(emprestimos_usuario):
                emprestimo_selecionado = emprestimos_usuario[selecao - 1]
                emprestimo_selecionado["status"] = "devolvido"
                with open('emprestimos.pkl', 'wb') as files:
                    p.dump(emprestimos, files)
                print("Empréstimo retornado com sucesso!")
                break
            else:
                print("Seleção inválida, tente novamente!")
        except ValueError:
            print("Erro, tente novamente!")




def inicio_emprestimo():
    """
    Faz o menu da funcionalidade emprestimo
    """
    global emprestimos
    emprestimos = u.verificar_file_emprestimos()
    while True:
        print("\nMenu:")
        print("1. Realizar empréstimo\n2. Retornar empréstimo\n3. Sair")
        try:
            selecao = int(input("Insira o seu modo: "))
            if selecao == 1:
                realizar_emprestimo()
            elif selecao == 2:
                retornar_emprestimo()
            elif selecao == 3:
                print("Saindo...")
                break
            else:
                print("Valor inválido, tente novamente!")
        except ValueError:
            print("Erro, tente novamente!")
