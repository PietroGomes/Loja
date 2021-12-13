from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import InserirProduto as ip
import telaMenu as tm


class NovoProduto:
    def __init__(self, janela):
        self.janelaAtual = janela
        self.janelaAtual.title("Novo Produto")
        self.janelaAtual.geometry("400x300+760+390")
        self.janelaAtual.resizable(False, False)
        
        self.lbNome = Label(janela, text = "Nome: ")
        self.lbDescricao = Label(janela, text = "Descrição: ")
        self.lbPreco = Label(janela, text = "Preço: ")
        self.lbUrlFoto = Label(janela, text = "URL Foto: ")

        self.txtNome = Entry(janela)
        self.txtDescricao = Entry(janela)
        self.txtPreco = Entry(janela)
        self.txtUrlFoto = Entry(janela)
        
        self.btnCadastrar = Button(janela, text = "Cadastrar", command = self.cadastrarProduto)
        self.btnCancelar = Button(janela, text = "Cancelar", command = self.limparCampos)

        self.lbNome.place(x = 100, y = 50)
        self.txtNome.place(x = 200 , y = 50)
        self.lbDescricao.place(x = 100, y = 100)
        self.txtDescricao.place(x = 200 , y = 100)
        self.lbPreco.place(x = 100, y = 150)
        self.txtPreco.place(x = 200 , y = 150)
        self.lbUrlFoto.place(x = 100, y = 200)
        self.txtUrlFoto.place(x = 200 , y = 200)
    
        self.btnCadastrar.place(x = 100, y = 250)
        self.btnCancelar.place(x = 200, y = 250)
        self.janelaAtual.mainloop()


    def cadastrarProduto(self):
        nome = self.txtNome.get()
        descricao = self.txtDescricao.get()
        preco = self.txtPreco.get()
        urlFoto = self.txtUrlFoto.get()

        if nome == "" or descricao == "" or preco == "" or urlFoto == "":
            messagebox.showinfo("Cadastro de produto", "Preencha todos os campos")
        else:
            ip.inserir_produto(nome, descricao, float(preco), urlFoto)
            messagebox.showinfo("Cadastro de produto", "Produto cadastrado com sucesso")
            self.limparCampos()
            

    def limparCampos(self):
        self.txtNome.delete(0, END)
        self.txtDescricao.delete(0, END)
        self.txtPreco.delete(0, END)
        self.txtUrlFoto.delete(0, END)
        
        self.janelaAtual.destroy()
        tm.Menu(Tk())


if __name__ == "__main__":
    janela = Tk()
    minhaJanela = NovoProduto(janela)
