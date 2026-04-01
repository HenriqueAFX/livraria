# ================================================================
#   IMPORTAÇÕES
# ================================================================

# Importa comandos do Windows/Linux
import os

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
def Validacao(tipo, valor):
    try:
        if tipo == "int":
            return int(valor)
        if tipo == "float":
            return float(valor)
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

# -------------------------------
# Menu principal
# -------------------------------

# 1. Cadastrar livro
def Cadastrar_livro():
    while True:
        Limpar()
        print(f"""{"-" * 31}
LIVRARIA - CADASTRO DE LIVROS
{"-" * 31}
""")

        codigo = Gera_codigo()
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        editora = input("Editora: ")
        categoria = input("Categoria: ")

        while True:
            entrada = input("Ano: ")
            ano = Validacao("int", entrada)
            if ano != None: break

        while True:
            entrada = input("Valor: ")
            valor = Validacao("float", entrada)
            if valor != None: break

        while True:
            entrada = input("Quantidade: ")
            estoque = Validacao("int", entrada)
            if estoque != None: break

        novo_livro = Livro(codigo=codigo, titulo=titulo, autor=autor, editora=editora, categoria=categoria, ano=ano, valor=valor, estoque=estoque)
        lista_livros.append(novo_livro)
        
        Limpar()
        novo_livro.info()

        op = input("\nDeseja cadastrar mais algum produto?\n[1] Sim\n[2] Não\n\nDigite sua escolha: ")

        if op == "2":
            break

# 2. Listar livros cadastrados
def Livros_cadastrados():
        Limpar()
        print(f"""{"-" * 32}
 LIVRARIA - LIVROS CADASTRADOS
{"-" * 32}
""")
        for livro in lista_livros:
            print("")
            livro.info()
            print(f"{"-" * 70}")

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
                busca = input("\nTitulo: ")
            elif tipo == "autor":
                busca = input("\nAutor: ")
            elif tipo == "editora":   
                busca = input("\nEditora: ")    
            elif tipo == "categoria":
                busca = input("\nCategoria: ")  

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
            busca = Validacao("int", entrada)
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
            busca = Validacao("int", entrada)
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
            busca = Validacao("float", entrada)
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
            busca = Validacao("int", entrada)
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
            busca = Validacao("float", entrada)
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
[0] Encerrar o sistema

Digite sua escolha: """)

# -------------------------------
# 0. Encerrar sistema
# -------------------------------

        if menu == "0":
            Limpar()
            print("Encerrando sistema...\n")
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
        valor_s = f"{self.valor:.2f}".replace(".",",")
        valor_total = self.valor * self.estoque
        valor_total_s = f"{valor_total:.2f}".replace(".",",")
        print(f'''{"Código:".ljust(25)} {self.codigo}
{"Titulo:".ljust(25)} {self.titulo}
{"Autor:".ljust(25)} {self.autor}
{"Editora:".ljust(25)} {self.editora}
{"Categoria:".ljust(25)} {self.categoria}
{"Ano:".ljust(25)} {self.ano}
{"Valor:".ljust(25)} R$ {valor_s}
{"Estoque:".ljust(25)} {self.estoque} unidades
{"Valor total de estoque:".ljust(25)} R$ {valor_total_s}
''')

# ================================================================
#   PRÉ-DEFINIÇÃO DE LISTA
# ================================================================

lista_livros = [
    Livro(1, "Dom Casmurro", "Machado de Assis", "Principis", "Literatura Brasileira", 1899, 29.90, 15),
    Livro(2, "O Hobbit", "J.R.R. Tolkien", "HarperCollins", "Fantasia", 1937, 59.90, 10),
    Livro(3, "1984", "George Orwell", "Companhia das Letras", "Distopia", 1949, 45.00, 20),
    Livro(4, "O Iluminado", "Stephen King", "Suma", "Terror", 1977, 64.90, 8),
    Livro(5, "Sapiens", "Yuval Noah Harari", "L&PM", "História", 2011, 74.90, 12),
    Livro(6, "Duna", "Frank Herbert", "Aleph", "Ficção Científica", 1965, 89.90, 5),
    Livro(7, "A Metamorfose", "Franz Kafka", "Antofágica", "Clássico", 1915, 39.90, 7),
    Livro(8, "Clean Code", "Robert C. Martin", "Alta Books", "Tecnologia", 2008, 95.00, 4),
    Livro(9, "Pai Rico, Pai Pobre", "Robert Kiyosaki", "Alta Books", "Finanças", 1997, 55.00, 25),
    Livro(10, "O Alquimista", "Paulo Coelho", "Paralela", "Autoajuda", 1988, 34.90, 30),
    Livro(11, "Orgulho e Preconceito", "Jane Austen", "Martin Claret", "Romance", 1813, 42.00, 18),
    Livro(12, "O Código Da Vinci", "Dan Brown", "Arqueiro", "Suspense", 2003, 49.90, 14),
    Livro(13, "Mulheres que Correm com os Lobos", "Clarissa Pinkola Estés", "Rocco", "Psicologia", 1992, 79.90, 9),
    Livro(14, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Agir", "Infantil", 1943, 25.00, 50),
    Livro(15, "Cem Anos de Solidão", "Gabriel García Márquez", "Record", "Realismo Mágico", 1967, 69.90, 11),
    Livro(16, "Algoritmos para Viver", "Brian Christian", "Record", "Ciência", 2016, 52.00, 6),
    Livro(17, "Ensaio Sobre a Cegueira", "José Saramago", "Porto Editora", "Ficção", 1995, 58.00, 13),
    Livro(18, "O Cortiço", "Aluísio Azevedo", "Ática", "Naturalismo", 1890, 22.00, 22),
    Livro(19, "Neuromancer", "William Gibson", "Aleph", "Cyberpunk", 1984, 54.00, 7),
    Livro(20, "A República", "Platão", "Edipro", "Filosofia", -375, 48.00, 10),
    Livro(21, "O Processo", "Franz Kafka", "Companhia das Letras", "Clássico", 1925, 44.90, 5),
    Livro(22, "Capitães da Areia", "Jorge Amado", "Companhia das Letras", "Modernismo", 1937, 39.00, 16),
    Livro(23, "O Gene", "Siddhartha Mukherjee", "Companhia das Letras", "Biologia", 2016, 85.00, 4),
    Livro(24, "A Revolução dos Bichos", "George Orwell", "Companhia das Letras", "Sátira Política", 1945, 28.00, 35),
    Livro(25, "Breves Respostas para Grandes Questões", "Stephen Hawking", "Intrínseca", "Divulgação Científica", 2018, 49.00, 20)
]

# ================================================================
#   EXECUÇÃO
# ================================================================

Menu_principal()