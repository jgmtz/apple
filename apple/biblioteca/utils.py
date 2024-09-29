"""
Módulo: Utils
Data: 08/06/2024
Versão: 4.0
Descrição: Funções usadas no Sistema
Alunos: Enzo Watanabe de Lima, Rafael Zeni e João Salomão
"""
import pickle as p
import sys as s
import os
#INÍCIO
def inicio():
    """
    Faz o menu que da acesso a todos os outros menus
    """
    while True:
        try:
            print("*" * 14)
            print("1. Livros\n2. Usuários\n3. Empréstimos\n4. Sair")
            escolha = input("Selecione o modo que deseja operar: ")
            if escolha == "1":
                import livros as l
                l.menu_livros()
            elif escolha == "2":
                import cadastro_usuarios as usu
                usu.iniciar_usuario(usuarios=verificar_file_usuarios())
            elif escolha == "3":
                import emprestimos as emp
                emp.inicio_emprestimo()
            elif escolha == "4":
                print("Finalizando Código...")
                s.exit()
            else:
                print("Valor inválido")
                continue
            print("*" * 30)
        except ValueError:
            print("")



#CADASTRO USUÁRIO
def verificar_file_usuarios():
    """
    Cria, se necessário, o arquivo cadastro_usu.pkl e se ele estiver vazio, evita erro
    """
    if os.path.isfile('cadastro_usu.pkl') and os.path.getsize('cadastro_usu.pkl') > 0:
        try:
            with open('cadastro_usu.pkl', 'rb') as file:
                return p.load(file)
        except (EOFError, p.UnpicklingError) as e:
            print("Erro ao carregar os dados do arquivo:", e)
            return []
    else:
        return []

#pergunta do menu principal
def pergunta_opcao():
    """
    Printa as opções para a funcionalidade usuários
    """
    print("Gerenciamento de Cadastro de Usuários")
    print("1. Cadastrar Usuário\n2. Listar Usuários\n3. Remover Usuário\n4. Editar Usuário\n5. Sair")
    opcao = input("Selecione o que deseja realizar: ")
    return opcao

#salvar itens atualizados do usuario
def atualizar_cadastro_usu(usuarios):
    """
    Salva os itens referentes ao usuário
    """
    with open('cadastro_usu.pkl', 'wb') as file:
        p.dump(usuarios, file)
#carregar itens atualizados do usuario
def carregar_cadastro_usu():
    """
    Carrega os itens referentes ao usuário
    """
    with open('cadastro_usu.pkl', 'rb') as file:
        usuarios = p.load(file)
    return usuarios

#coletando os dados do usuário
def solicitar_nome_completo() -> str:
    """
    Solicita o nome completo do usuário
    """
    while True:
        nome_completo = input("Insira o nome completo do usuário: ")
        if nome_completo == "":
            print("Deve ser informado um nome!")
            continue
        else:
            return nome_completo

def solicitar_telefone() -> str:
    """
    Solicita o telefone do usuário
    """
    while True:
        telefone = input("Insira o telefone do usuário (11 dígitos): ")
        if not telefone.isnumeric():
            print("O número deve conter apenas números!")
            continue
        elif len(telefone) != 11:
            print("O telefone deve ter 11 dígitos, exemplo: 41992345678")
            continue
        else:
            return telefone

def solicitar_endereco() -> str:
    """
    Solicita o endereço do usuário
    """
    while True:
        endereco = input("Insira o endereço do usuário (Rua, Número, Bairro): ")
        if endereco == "":
            print("Deve ser informado um endereço!")
            continue
        else:
            return endereco

def solicitar_numero_matricula() -> str:
    """
    Solicita um numero de matricula para o usuário
    """
    while True:
        numero_matricula = input("Insira um número para matrícula do usuário (8 dígitos): ")
        if not numero_matricula.isnumeric():
            print("A matrícula deve conter apenas números!")
            continue
        elif len(numero_matricula) != 8:
            print("A matrícula deve ter 8 números")
            continue
        else:
            return numero_matricula
   
#editando usuário
def encontrar_usuario_por_matricula(usuarios: list, numero_matricula: str) -> dict:
    """
    Encontra o usuário pela matrícula para que possa ser editado
    """
    for usuario in usuarios:
        if usuario["numero_matricula"] == numero_matricula:
            return usuario
    return None

def editar_nome_completo(usuario: dict) -> str:
    """
    Edita o nome do usuário
    """
    nome_completo = input(f"Nome completo [{usuario['nome_completo']}]: ")
    if nome_completo:
        usuario["nome_completo"] = nome_completo
    return usuario

def editar_telefone(usuario: dict) -> str:
    """
    Edita o telefone do usuário
    """
    while True:
        telefone = input(f"Telefone [{usuario['telefone']}]: ")
        if telefone:
            if not telefone.isnumeric():
                print("O número deve conter apenas números!")
                continue
            elif len(telefone) != 11:
                print("O telefone deve ter 11 dígitos, exemplo: 41992345678")
                continue
            else:
                usuario["telefone"] = telefone
                break
        break
    return usuario

def editar_endereco(usuario: dict) -> str:
    """
    Edita o endereço do usuário
    """
    endereco = input(f"Endereço [{usuario['endereco']}]: ")
    if endereco:
        usuario["endereco"] = endereco
    return usuario

#remover usuário
def prints_dados_usuario(usuario: dict):
    """
    Printa os dados do usuário
    """
    print(f"\nNome Completo: {usuario['nome_completo']}")
    print(f"Telefone: {usuario['telefone']}")
    print(f"Endereço: {usuario['endereco']}")
    print(f"Número de Matrícula: {usuario['numero_matricula']}\n")

def conferir_listar_usuarios(usuarios: list):
    """
    Confere se o usuário está na lista de usuários
    """
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return
    else:
        print("\nLista de usuários cadastrados:")
        for usuario in usuarios:
            prints_dados_usuario(usuario)








#CADASTRO LIVROS
def verificar_file_livros():
    """
    Cria se necessário o arquivo livros.pkl e se ele estiver vazio, evita erro
    """
    if os.path.isfile('livros.pkl') and os.path.getsize('livros.pkl') > 0:
        try:
            with open('livros.pkl', 'rb') as f:
                return p.load(f)
        except (EOFError, p.UnpicklingError) as e:
            print("Erro ao carregar os dados do arquivo:", e)
            return []
    else:
        return []

#menu livros
def pergunta_selecao():
    """
    Cria o menu usuarios
    """
    print("*" * 20)
    print("Gerenciamento de Cadastro de Usuários")
    print("1. Cadastrar Livro\n2. Listar Livros\n3. Buscar Livro\n4. Remover Livros\n5. Sair")
    selecao = input("Selecione o que deseja realizar: ")
    return selecao

#salvar itens atualizados do livros
def atualizar_livros(listao):
    """
    Salva os itens referentes aos livros
    """
    with open('livros.pkl', 'wb') as f:
        p.dump(listao, f)
#carregar itens atualizados do livros
def carregar_livros():
    """
    Carrega os itens referentes aos livros
    """
    with open('livros.pkl', 'rb') as f:
        listao = p.load(f)
    return listao



#EMPRÉSTIMOS
def verificar_file_emprestimos():
    """
    Cria se necessário o arquivo emprestimos.pkl e se ele estiver vazio, evita erro
    """
    if os.path.isfile('emprestimos.pkl') and os.path.getsize('emprestimos.pkl') > 0:
        try:
            with open('emprestimos.pkl', 'rb') as files:
                return p.load(files)
        except (EOFError, p.UnpicklingError) as e:
            print("Erro ao carregar os dados do arquivo:", e)
            return []
    else:
        return []
    

#salvar itens atualizados do emprestimo
def atualizar_emprestimos(emprestimos):
    """
    Salva os itens referentes aos livros
    """
    with open('emprestimos.pkl', 'wb') as files:
        p.dump(emprestimos, files)
#carregar itens atualizados do emprestimo
def carregar_emprestimos():
    """
    Carrega os itens referentes aos livros
    """
    with open('emprestimos.pkl', 'rb') as files:
        emprestimos = p.load(files)
    return emprestimos


def pergunta_opcao_emp():
    """
    Cria o menu de empréstimos
    """
    print("Gerenciamento de Empréstimos")
    print("1. Realizar Empréstimo\n2. Realizar Devolução\n3. Sair")
    opcao_emp = input("Selecione o que deseja realizar: ")
    return opcao_emp


