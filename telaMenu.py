from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

import SelectProduto as sp
import ConnectionBD as con
import DeletarProduto as dp
import telaCadastro as tc
import telaAvaliacao as ta


class Menu:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Relojoaria Seu Joaquim")
        self.janela.geometry("800x600+560+240")
        self.janela.resizable(False, False)

        self.tv = ttk.Treeview(
            janela,
            columns = ['id', 'nome', 'descricao', 'preco', 'foto'],
            show = "headings")

        self.tv.column('id', minwidth=0, width=50)
        self.tv.column('nome', minwidth=0, width=100)
        self.tv.column('descricao', minwidth=0, width=250)
        self.tv.column('preco', minwidth=0, width=50)
        self.tv.column('foto', minwidth=0, width=150)

        self.tv.heading('id', text="ID")
        self.tv.heading('nome', text="Nome")
        self.tv.heading('descricao', text="Descrição")
        self.tv.heading('preco', text="Preço")
        self.tv.heading('foto', text="Foto")
        self.tv.pack()

        self.atualizarTabela()

        self.btnNovoProduto = Button(self.janela, text = "Novo produto", command = self.cadastrarProduto)
        self.btnNovoProduto.place(x = 100, rely = 0.45, width = 200)

        self.btnAvaliacao = Button(self.janela, text = "Avaliação", command = self.avaliarProduto)
        self.btnAvaliacao.place(x = 300, rely = 0.45, width = 200)

        self.btnDeletar = Button(self.janela, text = "Deletar", command = self.deletarProduto)
        self.btnDeletar.place(x = 500, rely = 0.45, width = 200)

        self.janela.mainloop()


    def selecionar(self):
        try:
            itemSelecionado = self.tv.selection()[0]
            valores = self.tv.item(itemSelecionado, "values")
            messagebox.showinfo("Item selecionado", f"O item selecionado foi: {valores[0]}")
        except:
            messagebox.showinfo("Aviso", "Nenhum item foi selecionado")


    def deletarProduto(self):
        try:
            itemSelecionado = self.tv.selection()[0]
            msgBox = messagebox.askquestion("Deletar Produto", "Deseja excluir o produto?", icon = "warning")

            if msgBox == "yes":
                valores = self.tv.item(itemSelecionado, "values")
                idProduto = valores[0]

                dp.delete_produto_id(idProduto)
                self.tv.delete(itemSelecionado)
                messagebox.showinfo("Exclusão de Produto", "Produto excluído com sucesso")
            else:
                return
            
        except:
            messagebox.showinfo("Deletar Produto", "Selecione um produto")


    def atualizarTabela(self):
        for i in self.tv.get_children():
            self.tv.delete(i)

        listaProdutos = sp.get_todos_produtos()

        for i in listaProdutos:
            self.tv.insert("", "end", values = (i.id, i.nome, i.descricao, i.preco, i.foto))


    def cadastrarProduto(self):
        self.janela.destroy()
        tc.NovoProduto(Tk())


    def avaliarProduto(self):
        try:
            itemSelecionado = self.tv.selection()[0]
            valores = self.tv.item(itemSelecionado, "values")
            idProduto = valores[0]

            self.janela.destroy()
            ta.MenuAvaliacao(Tk(), int(idProduto))
        
        except:
            messagebox.showinfo("Avaliar Produto", "Selecione um produto")


if __name__ == "__main__":
    janela = Tk()
    minhaJanela = Menu(janela)
