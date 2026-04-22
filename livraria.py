# ================================================================
#   IMPORTAÇÕES
# ================================================================

import os
from datetime import datetime

# ================================================================
#   MÉTODOS/FUNÇÕES
# ================================================================

# Limpa o terminal
def Limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Validacao de dados
def Validacao(tipo, valor, aceita_negativo=1):
    try:
        if tipo == "int":
            num = int(valor)
        elif tipo == "float":
            num = float(valor)
        else:
            return None

        # Tratamento para valores negativos
        if aceita_negativo == 0 and num < 0:
            print(f"Erro: O valor não pode ser negativo ({valor}).")
            return None
            
        return num

    except (ValueError, TypeError):
        print(f"Erro: '{valor}' não é um número válido.")
        return None
    
# Gera um novo código para um novo livro
def Gera_codigo():
    if lista_livros == []:
        codigo = 1
    else:
        ultimo = lista_livros[-1].codigo
        codigo = ultimo + 1
    return codigo

# Corrige visual da quantidade de numeros (1234,56 = 1.234,56)
def Correcao_quantia(valor):
    qtd = len(valor)

    # milhares
    if 7 <= qtd <= 9:
            milhar = valor[:-6] # Antes dos ultimos 6 digitos
            resto = valor[-6:]  # Ultimos 6 digitos (000,00)
            valor = f"{milhar}.{resto}"

    # milhoes
    if 10 <= qtd <= 12:
            milhao = valor[:-10]
            milhar = valor[-10:-6]
            resto = valor[-6:]
            return f"{milhao}.{milhar}.{resto}"
    
    # bilhoes
    if 13 <= qtd <= 15:
        bilhao = valor[:-14]
        milhao = valor[-14:-10]
        milhar = valor[-10:-6]
        resto = valor[-6:]
        return f"{bilhao}.{milhao}.{milhar}.{resto}"

    return valor

# Transfere os dados armazenados no "lista_livros.csv" para uma
# lista interna de mesmo nome, para ser lida pelo sistema
def Carregar_dados():
    arquivo = open("lista_livros.csv", "r")
    arquivo.readline()
    nova_linha = arquivo.readline()

    while nova_linha:
        dados_separados = nova_linha.split(';')
        lista_livros.append(Livro.Construtor_CSV(dados_separados))
        nova_linha = arquivo.readline()

# -------------------------------
# Menu principal
# -------------------------------

# 0. Encerrar sistema
def Encerrar_sistema():
    def Titulo():
        print(f"""{"-" * 36}
 LIVRARIA - ENCERRAMENTO DE SISTEMA
{"-" * 36}
""")

    while True:
        Limpar()
        Titulo()
        op = input("""Qualquer alteração não salva será perdida ao encerrar a sessão atual.
               
Deseja salvar as alterações feitas na sessão atual?
[1] Sim
[2] Não
               
Digite sua escolha: """)
    
        if op == "1":
            Limpar()
            Titulo()
            print("Salvando registros...")

            cabecalho = "codigo,titulo,autor,editora,categoria,ano,valor,estoque"

            with open('lista_livros.csv', 'w') as arquivo:
                arquivo.write(f"{cabecalho}\n")

                for livro in lista_livros:
                    arquivo.write(f"{livro.codigo};{livro.titulo};{livro.autor};{livro.editora};{livro.categoria};{livro.ano};{livro.valor};{livro.estoque}\n".upper())

            print("\nRegistros salvos com sucesso!")
            break

        if op == "2":
            Limpar()
            Titulo()
            print("Nenhuma alteração foi salva ou perdida.")
            break

# 1. Cadastrar livro
def Cadastrar_livro():
        Limpar()
        print(f"""{"-" * 31}
LIVRARIA - CADASTRO DE LIVROS
{"-" * 31}
""")

        novo_livro = Livro.Construtor_manual()
        lista_livros.append(novo_livro)
        
        Limpar()
        novo_livro.info()
        input("""Livro cadastrado com sucesso!
                 
Pressione 'Enter' para voltar ao menu principal.""")

# 2. Listar livros cadastrados
def Livros_cadastrados():
    Limpar()
    print(f"""{"-" * 32}
LIVRARIA - LIVROS CADASTRADOS
{"-" * 32}
""")
    i = 0.0

    for livro in lista_livros:
        print("")
        livro.info()
        print(f"{"-" * 70}")
        valor_total = livro.valor * livro.estoque
        i += valor_total

    valor_total_str = f"{i:.2f}".replace(".",",")
    valor_total_str = Correcao_quantia(valor_total_str)
    print(f'\nValor total do estoque da livraria: R$ {valor_total_str}')

    input("\nPressione 'Enter' para voltar ao menu principal.")

# 3. Buscar livros cadastrados
def Buscar_livros():

    # -------------------------------
    # Funções auxiliares
    # -------------------------------
    
    def Titulo():
        print(f"""{"-" * 29}
 LIVRARIA - BUSCA DE LIVROS
{"-" * 29}""")
    def Limpar_e_titulo():
        Limpar()
        Titulo()
    def Linha():
        print("-" * 62)
    def Volta_menu():
        input("\nPressione 'Enter' para voltar ao menu de busca.")
    def Nenhum_registro(i):
        if i<1: print("\nNenhum registro encontrado.")
    def Busca_texto(tipo):
            Limpar_e_titulo()    
            
            if tipo == "titulo":
                busca = input("\nTitulo: ").upper()
            elif tipo == "autor":
                busca = input("\nAutor: ").upper()
            elif tipo == "editora":   
                busca = input("\nEditora: ").upper()   
            elif tipo == "categoria":
                busca = input("\nCategoria: ").upper()

            Limpar_e_titulo()
            i = 0 

            for livro in lista_livros:
                encontrou = False
                if tipo == "titulo" and livro.titulo == busca: encontrou = True
                if tipo == "autor" and livro.autor == busca: encontrou = True
                if tipo == "editora" and livro.editora == busca: encontrou = True
                if tipo == "categoria" and livro.categoria == busca: encontrou = True

                if encontrou == True:
                    print("")
                    livro.info()
                    Linha()
                    i += 1

            Nenhum_registro(i)
            Volta_menu()
        
    # -------------------------------
    # Funções de busca
    # -------------------------------
    def Busca_codigo():
        while True:
            Limpar_e_titulo()
            entrada = input("\nCódigo: ")
            busca = Validacao("int", entrada, 0)
            if busca != None: break

        Limpar_e_titulo()
        i = 0 

        for livro in lista_livros:
            if livro.codigo == busca:
                print("")
                livro.info()
                Linha()
                i+=1

        Nenhum_registro(i)
        Volta_menu()

    def Busca_titulo():
        Busca_texto("titulo")

    def Busca_autor():
        Busca_texto("autor")
        
    def Busca_editora():
        Busca_texto("editora")

    def Busca_categoria():
        Busca_texto("categoria")

    def Busca_ano():
        while True:
            Limpar_e_titulo()
            entrada = input("\nAno: ")
            busca = Validacao("int", entrada, 1)
            if busca != None: break
        
        while True:
            op = input(f"""
[1] Livros do ano {busca}
[2] Livros do ano {busca} e anterior
[3] Livros do ano {busca} e posterior

Digite sua escolha: """)

            Limpar_e_titulo()
            i = 0

            if op == "1":
                for livro in lista_livros:
                    if livro.ano == busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break
        
            elif op == "2":
                for livro in lista_livros:
                    if livro.ano <= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

            elif op == "3":
                for livro in lista_livros:
                    if livro.ano >= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

        Nenhum_registro(i)
        Volta_menu()

    def Busca_preco():
        while True:
            Limpar_e_titulo()
            entrada = input("\nPreço: R$ ")
            busca = Validacao("float", entrada, 0)
            if busca != None: break
            
        busca_s = f"{busca:.2f}".replace(".",",")

        while True:
            op = input(f"""
[1] Livros de R$ {busca_s}
[2] Livros de R$ {busca_s} e menor
[3] Livros de R$ {busca_s} e maior

Digite sua escolha: """)

            Limpar_e_titulo()
            i = 0

            if op == "1":
                for livro in lista_livros:
                    if livro.valor == busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break
        
            elif op == "2":
                for livro in lista_livros:
                    if livro.valor <= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

            elif op == "3":
                for livro in lista_livros:
                    if livro.valor >= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

        Nenhum_registro(i)
        Volta_menu()

    def Busca_quantidade():
        while True:
            Limpar_e_titulo()
            entrada = input("\nQuantidade: ")
            busca = Validacao("int", entrada, 0)
            if busca != None: break
        
        while True:
            op = input(f"""
[1] Livros de quantidade {busca}
[2] Livros de quantidade {busca} e menor
[3] Livros de quantidade {busca} e maior

Digite sua escolha: """)

            Limpar_e_titulo()
            i = 0

            if op == "1":
                for livro in lista_livros:
                    if livro.estoque == busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break
        
            elif op == "2":
                for livro in lista_livros:
                    if livro.estoque <= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

            elif op == "3":
                for livro in lista_livros:
                    if livro.estoque >= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

        Nenhum_registro(i)
        Volta_menu()

    def Busca_valor_total():
        while True:
            Limpar_e_titulo()
            entrada = input("\nValor total em estoque: R$ ")
            busca = Validacao("float", entrada, 0)
            if busca != None: break
            
        busca_s = f"{busca:.2f}".replace(".",",")

        while True:
            op = input(f"""
[1] Livros com valor total de R$ {busca_s}
[2] Livros com valor total de R$ {busca_s} e menor
[3] Livros com valor total de R$ {busca_s} e maior

Digite sua escolha: """)

            Limpar_e_titulo()
            i = 0

            if op == "1":
                for livro in lista_livros:
                    if (livro.estoque * livro.valor) == busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break
        
            elif op == "2":
                for livro in lista_livros:
                    if (livro.estoque * livro.valor) <= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

            elif op == "3":
                for livro in lista_livros:
                    if (livro.estoque * livro.valor) >= busca:
                        print("")
                        livro.info()
                        Linha()
                        i+=1
                break

        Nenhum_registro(i)
        Volta_menu()
    
    def Busca_menu():

        while True:
            Limpar()
            busca = input(f"""{"-" * 29}
 LIVRARIA - BUSCA DE LIVROS
{"-" * 29}
                    
[1] Buscar livros por código
[2] Buscar livros por titulo
[3] Buscar livros por autor
[4] Buscar livros por editora
[5] Buscar livros por categoria
[6] Buscar livros por ano
[7] Buscar livros por preço
[8] Buscar livros por quantidade em estoque
[9] Buscar livros por valor total em estoque
[0] Voltar ao menu principal

Digite sua escolha: """)

            if busca == "1":
                Busca_codigo()
            if busca == "2":
                Busca_titulo()
            if busca == "3":
                Busca_autor()
            if busca == "4":
                Busca_editora()
            if busca == "5":
                Busca_categoria()
            if busca == "6":
                Busca_ano()
            if busca == "7":
                Busca_preco()
            if busca == "8":
                Busca_quantidade()
            if busca == "9":
                Busca_valor_total()
            if busca == "0":
                break

    # -------------------------------
    # Menu de busca
    # -------------------------------
    Busca_menu()

# 4. Salvar atualizações de cadastro
def Salvar_atualizacoes():
        def Titulo():
            print(f"""{"-" * 32}
 LIVRARIA - SALVAR ATUALIZAÇÕES
{"-" * 32}
""")
        
        while True:
            Limpar()
            Titulo()
            op = input("""Qualquer alteração não salva será perdida ao encerrar a sessão atual.
               
Deseja salvar as alterações feitas na sessão atual?
[1] Sim
[2] Não
               
Digite sua escolha: """)
    
            if op == "1":
                Limpar()
                Titulo()
                print("Salvando registros...")

                cabecalho = "CODIGO;TITULO;AUTOR;EDITORA;CATEGORIA;ANO;VALOR;ESTOQUE"

                with open('lista_livros.csv', 'w') as arquivo:
                    arquivo.write(f"{cabecalho}\n")

                    for livro in lista_livros:
                        arquivo.write(f"{livro.codigo};{livro.titulo};{livro.autor};{livro.editora};{livro.categoria};{livro.ano};{livro.valor};{livro.estoque}\n".upper())

                print("\nRegistros salvos com sucesso!")
                break

            if op == "2":
                Limpar()
                Titulo()
                print("Nenhuma alteração foi salva ou perdida.")
                break

        input("\nPressione 'Enter' para voltar ao menu principal.")

# Menu principal
def Menu_principal():
    while True:
        Limpar()

        menu = input(f"""{"-" * 38}
 LIVRARIA - GERENCIAMENTO DE ESTOQUE
{"-" * 38}
                    
[1] Cadastrar livro
[2] Listar livros cadastrados
[3] Buscar livros cadastrados
[4] Salvar atualizações de cadastro
[0] Encerrar o sistema

Digite sua escolha: """)
        
# [4] Editar livro cadastrado (EM DESENVOLVIMENTO)
# [5] Excluir livro cadastrado (EM DESENVOLVIMENTO)

        # -------------------------------
        # 0. Encerrar sistema
        # -------------------------------
        if menu == "0":
            Limpar()
            Encerrar_sistema()
            print("\nEncerrando sistema...\n")
            break

        # -------------------------------
        # 1. Cadastrar livro
        # -------------------------------
        if menu == "1":
            Cadastrar_livro()

        # -------------------------------
        # 2. Listar livros cadastrados
        # -------------------------------
        if menu == "2":
            Livros_cadastrados()

        # -------------------------------
        # 3. Buscar livros cadastrados
        # -------------------------------
        if menu == "3":
            Buscar_livros()

        # -------------------------------
        # 4. Editar livro cadastrado
        # -------------------------------
        #if menu == "4":
            ...

        # -------------------------------
        # 5. Excluir livro cadastrado
        # -------------------------------
        #if menu == "5":
            ...

        # -------------------------------
        # 6. Salvar atualizações de cadastro
        # -------------------------------
        #if menu == "6":
        if menu == "4":
            Salvar_atualizacoes()

# ================================================================
#   CLASSE
# ================================================================

class Livro:
    def __init__(self, codigo, titulo, autor, editora, categoria, ano, valor, estoque):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    # -------------------------------
    #   MÉTODOS/FUNÇÕES DE CLASSE
    # -------------------------------

    def info(self):
        valor_str = f"{self.valor:.2f}".replace(".",",")
        valor_total = self.valor * self.estoque
        valor_total_str = f"{valor_total:.2f}".replace(".",",")

        valor_str = Correcao_quantia(valor_str)
        valor_total_str = Correcao_quantia(valor_total_str)

        print(f'''{"Código:".ljust(25)} {self.codigo}
{"Titulo:".ljust(25)} {self.titulo}
{"Autor:".ljust(25)} {self.autor}
{"Editora:".ljust(25)} {self.editora}
{"Categoria:".ljust(25)} {self.categoria}
{"Ano:".ljust(25)} {self.ano}
{"Valor:".ljust(25)} R$ {valor_str}
{"Estoque:".ljust(25)} {self.estoque} unidades
{"Valor total de estoque:".ljust(25)} R$ {valor_total_str}
''')

    @classmethod
    def Construtor_manual(cls):
        codigo = Gera_codigo()
        
        while True:
            titulo = input("Titulo: ")
            if titulo == "": print("Erro: O campo titulo não pode estar vazio.")
            if titulo != "": break

        while True:
            autor = input("Autor: ")
            if autor == "": print("Erro: O campo autor não pode estar vazio.")
            if autor != "": break

        while True:
            editora = input("Editora: ")
            if editora == "": print("Erro: O campo editora não pode estar vazio.")
            if editora != "": break

        while True:
            categoria = input("Categoria: ")
            if categoria == "": print("Erro: O campo categoria não pode estar vazio.")
            if categoria != "": break

        while True:
            entrada = input("Ano: ")
            ano = Validacao("int", entrada, 1)
            
            if ano != None:
                ano_atual = datetime.now().year
                
                if ano > ano_atual:
                    confirmou = False
                    while True:
                        op = input(f"\n{ano} é maior que o ano atual, tem certeza que deseja continuar?\n[1] Sim\n[2] Não\n\nDigite sua escolha: ")
                        
                        if op == "1":
                            confirmou = True
                            break
                        elif op == "2":
                            confirmou = False
                            break
                        else:
                            print("Escolha inválida.")

                    if confirmou: 
                        break
                else:
                    break

            

        while True:
            entrada = input("Valor: ")
            valor = Validacao("float", entrada, 0)
            
            if valor != None:
                if valor == 0:
                    confirmou = False
                    while True:
                        op = input(f"\nO valor digitado foi R$ 0,00, tem certeza que deseja continuar??\n[1] Sim\n[2] Não\n\nDigite sua escolha: ")
                        
                        if op == "1":
                            confirmou = True
                            break
                        elif op == "2":
                            confirmou = False
                            break
                        else:
                            print("Escolha inválida.")
                    
                    if confirmou:
                        break
                else:
                    break

        while True:
            entrada = input("Quantidade: ")
            estoque = Validacao("int", entrada, 0)
            if estoque != None: break

        novo_livro = Livro(codigo=codigo, titulo=titulo, autor=autor, editora=editora, categoria=categoria, ano=ano, valor=valor, estoque=estoque)
        return novo_livro

    @classmethod
    def Construtor_CSV(cls, dados_livro):
        codigo = int(dados_livro[0])
        titulo = dados_livro[1]
        autor = dados_livro[2]
        editora = dados_livro[3]
        categoria = dados_livro[4]
        ano = int(dados_livro[5])
        valor = float(dados_livro[6])
        estoque = int(dados_livro[7].replace("\n", ""))
        return cls(codigo, titulo, autor, editora, categoria, ano, valor, estoque)
    
# ================================================================
#   PRÉ-DEFINIÇÃO DE LISTAS
# ================================================================

lista_livros = []
Carregar_dados()

# ================================================================
#   EXECUÇÃO
# ================================================================

Menu_principal()