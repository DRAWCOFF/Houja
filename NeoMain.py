import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib

CAMINHO_USUARIOS = "usuarios.json"
CAMINHO_CONTEUDO = "conteudo.json"
CAMINHO_QUESTOES = "questoes.json"
page : int = 0

Aluno = None #recebe na função login, os dados do usuário
SIZEWINDOW = "1000x800"
def gerar_hash(senha: str) -> str:
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def carregar_conteudo():
    if os.path.exists(CAMINHO_CONTEUDO):
        with open(CAMINHO_CONTEUDO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return {"Content": []}

def salvar_content(data):
    with open(CAMINHO_CONTEUDO, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)

std_source = carregar_conteudo()
List_cont_stg_hklv1 = std_source["Content"][0]["Stage 1"][0]["HKlv1"]

#
topic_value = 0
topic = List_cont_stg_hklv1[topic_value] #assunto hira

mainTc = topic["Assunto"]

wht =  topic["what"] #oque é hira ou kata

exp =  topic["Explicacao"] # explicação hira ou kata

fnc =  topic["funcao"] # função hira ou kata

expl_1 = topic["Exemplo1"] # explicação hira ou kata
expl_2 = topic["Exemplo2"]
expl_3 = topic["Exemplo3"]
expl_4 = topic["Exemplo4"]



# Carrega os usuários do arquivo JSON
def carregar_usuarios():
    if os.path.exists(CAMINHO_USUARIOS):
        with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return {"usuarios": []}

# Salva os usuários no arquivo JSON
def salvar_usuarios(data):
    with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)

# Dados carregados
dados = carregar_usuarios()

b1 = None
b2 = None
b3 = None

mkpage = Aluno["markpage"]

def clear_elements(pai):
        for widget in pai.winfo_children():
            widget.destroy()

def tab_learn():
    global b1
    global b2
    global b3
    global page
    global topic_value
    page = 1
    TbLearn = tk.Toplevel(janela)
    TbLearn.title("Houja - Aprender")
    TbLearn.geometry(SIZEWINDOW)

    """def verificar_markpage():
        for pg in mkpage:
            if pg == mkpage:
                page = pg
                return page
            
    def pass_page():
        page += 1
        mkpage += 1
        return page, mkpage

    def update_page():
        clear_elements(TbLearn)
        b1 = mainTc"""


    Bt_next = tk.Button(TbLearn, text="continuar")
    Bt_next.pack(pady = 5)


def Prime_screen(quem):
    Prime = tk.Toplevel(janela)
    Prime.title("Houja - Resumo do Aprendizado")
    Prime.geometry(SIZEWINDOW)
    h1 = tk.Label(Prime, text=f"Seja bem vindo ao HouJa:", font=32)
    h1.pack()
   

    
    Bt_learn_stg1 = tk.Button(Prime, text=f"Vamos começar a aprender Japonês", command=tab_learn)
    Bt_learn_stg1.pack(pady=5)

# Função de login
def fazer_login():
    global topic_value
    nome = entrada_usuario.get()
    senha = entrada_senha.get()
    senha_hash = gerar_hash(senha)#paramos aqui
    global Aluno
    
    for usuario in dados["usuarios"]:
        if usuario["User"] == nome and usuario["senha"] == senha_hash:
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo(a), {nome}!")
            
            Aluno = usuario #assim que logar irá puxar todas ás variaveis desse usuario do Banco de Dados
            topic_value = Aluno["ListOfConceptsSaw"]
            Prime_screen(usuario)
            entrada_senha.destroy()
            entrada_usuario.destroy()
            
            BtLogar.destroy()
            BtCadas.destroy()
            Tsen.destroy()
            Tusu.destroy()
            logado = tk.Label(janela, text="Você logou").pack(pady=5)
            return

    messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")



# Função de cadastro
def abrir_cadastro():
    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("300x200")

    tk.Label(janela_cadastro, text="Novo Usuário:").pack(pady=5)
    entrada_novo_usuario = tk.Entry(janela_cadastro)
    entrada_novo_usuario.pack()

    tk.Label(janela_cadastro, text="Nova Senha:").pack(pady=5)
    entrada_nova_senha = tk.Entry(janela_cadastro, show="*")
    entrada_nova_senha.pack()

    def cadastrar():
        novo_usuario = entrada_novo_usuario.get()
        nova_senha = entrada_nova_senha.get()

        # Verifica se o usuário já existe
        for usuario in dados["usuarios"]:
            if usuario["User"] == novo_usuario:
                messagebox.showerror("Erro", "Usuário já existe.")
                return

        if novo_usuario.strip() == "" or nova_senha.strip() == "":
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return


        #Sempre que alterar ás váriveis do usuarios.json, lembre-se de add aqui também, se não buga
        nova_senha_hash = gerar_hash(nova_senha)
        novo_registro = {"User": novo_usuario, "senha": nova_senha_hash, "HK_lv": 1, "Kj_level": 1, "ListOfLearned_HK": [], "ListOfLearned_Kj": [],"ListOfConceptsSaw": 0,"ListOfQuestions_mistakes": [],"ListOfQuestions_correct": [],"STAGE": 1}

        dados["usuarios"].append(novo_registro)
        salvar_usuarios(dados)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()

    tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar).pack(pady=15)


def bloquear_teclas(event):
    if event.keysym in ["Return", "space"]:
        return "break"  # Impede que a tecla tenha efeito

# Interface principal
janela = tk.Tk()
janela.title("Houja - Login")
janela.geometry("300x200")

Tusu = tk.Label(janela, text="Usuário:")
Tusu.pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()


Tsen = tk.Label(janela, text="Senha:")
Tsen.pack(pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

#tk.Button(janela, text="Entrar", command=fazer_login,).pack(pady=5)
BtLogar = tk.Button(janela, text="Entrar", command=fazer_login)
BtLogar.pack(pady=5)
BtCadas = tk.Button(janela, text="Cadastrar", command=abrir_cadastro)
BtCadas.pack(pady=5)
janela.mainloop()
