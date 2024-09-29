"""
Módulo: Utils
Data: 08/06/2024
Versão: 4.0
Descrição: Funções usadas em todo o sistema
Alunos: Enzo Watanabe de Lima, Rafael Zeni e João Salomão
"""

import os
import pickle as p
import utils as u

def iniciar_usuario(usuarios):
    """
    Faz o menu da funcionalidade usuários
    """
    usuarios = u.verificar_file_usuarios()
    while True:
        try:
            opcao = u.pergunta_opcao()
            if opcao == "1":
                adicionar_usuarios(usuarios)
                u.atualizar_cadastro_usu(usuarios)
            elif opcao == "2":
                listar_usuarios(usuarios)
                u.atualizar_cadastro_usu(usuarios)
            elif opcao == "3":
                remover_usuario(usuarios)
                usuarios = u.carregar_cadastro_usu()
                u.atualizar_cadastro_usu(usuarios)               
            elif opcao == "4":
                editar_usuarios(usuarios)
                u.atualizar_cadastro_usu(usuarios)
            elif opcao == "5":
                print("Saindo...")
                import main as m
                m.u.inicio()
            else:
                print("Valor inválido, selecione novamente!")
                continue
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")


def coletar_dados_usuario() -> dict:
    """
    Coleta os dados do usuário, recebendo seu nome, telefone, endereço e numero de matrícula
    """
    while True:
        try:
            #solicita o nome do usuario para cadastro
            nome_completo = u.solicitar_nome_completo()
            #solicita o telefone do usuario
            telefone = u.solicitar_telefone()
            #solicita o endereço do usuario
            endereco = u.solicitar_endereco()
            #solicita o número da matricula do usuario
            numero_matricula = u.solicitar_numero_matricula()
            usuario = {"nome_completo": nome_completo,
                       "telefone": telefone,
                       "endereco": endereco,
                       "numero_matricula": numero_matricula}
            return usuario
        except ValueError as e:
            print(e)
        print("Por Favor, corrija o erro e tente novamente!")
        continue

usuarios = []


#adicionar usuário
def adicionar_usuarios(usuarios):
    """
    Pega as informações do usuário coletadas anteriormente, e coloca dentro de uma lista
    """
    usuario = coletar_dados_usuario()
    if usuario is None:
        return False
    for u in usuarios:
        if u["numero_matricula"] == usuario["numero_matricula"]:
            print("Usuário já cadastrado!")
            return False
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!") 
    return True


#editar usuário
def editar_usuarios(usuarios: list):
    """
    Possibilita o usuário editar alguma informação de seu cadastro, menos a matrícula
    """
    numero_matricula = input("Insira o número de matrícula para editar os dados: ")
    usuario = u.encontrar_usuario_por_matricula(usuarios, numero_matricula)
    if usuario:
        print("Usuário encontrado!")
        print("Insira os novos dados (pressione Enter para manter o dado atual): ")
        usuario = u.editar_nome_completo(usuario)
        usuario = u.editar_telefone(usuario)
        usuario = u.editar_endereco(usuario)
        print("Usuário editado com sucesso!")
        return True
    else:
        print("Usuário não encontrado!")
        return False


#remover usuário
def remover_usuario(usuario: list):
    """
    Possibilita a remoção de um usuário
    """
    usuarios = u.verificar_file_usuarios()
    numero_matricula = input("Insira o número de matrícula que deseja remover: ")
    for usuario in usuarios:
        if usuario["numero_matricula"] == numero_matricula:
            usuarios.remove(usuario)
            u.atualizar_cadastro_usu(usuarios)
            print("Usuário removido!")
            return True    
    print("Usuário não encontrado!")
    return False


#listar usuários cadastrados
def listar_usuarios(usuarios: list):
    """
    Lista todos os usuários
    """
    u.conferir_listar_usuarios(usuarios)


usuarios = []

iniciar_usuario(usuarios)