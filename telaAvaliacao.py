from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import telaMenu as tm
import SelectAvaliacao as sa
import telaPreencherAvaliacao as tpa
import DeletarAvaliacao as da

class MenuAvaliacao:
    def __init__(self, janela, produto):
        self.janelaAtual = janela
        self.produto = produto

        self.janelaAtual.title("Avaliar Produto")
        self.janelaAtual.geometry("800x600+560+240")
        self.janelaAtual.resizable(False, False)

        self.tv = ttk.Treeview(
            janela,
            columns = ['id', 'comentario', 'data', 'idUsuario', 'idProduto'],
            show = "headings"
        )

        self.tv.column("id", minwidth = 0, width = 50)
        self.tv.column("comentario", minwidth = 0, width = 250)
        self.tv.column("data", minwidth = 0, width = 100)
        self.tv.column("idUsuario", minwidth = 0, width = 50)
        self.tv.column("idProduto", minwidth = 0, width = 50)

        self.tv.heading("id", text = "ID")
        self.tv.heading("comentario", text = "Comentário")
        self.tv.heading("data", text = "Data")
        self.tv.heading("idUsuario", text = "ID Usuário")
        self.tv.heading("idProduto", text = "ID Produto")
        self.tv.place(relx = 0.1, relwidth = 0.8)

        self.atualizarTabela(self.produto)

        self.btnAvaliar = Button(self.janelaAtual, text = "Avaliar", command = self.preencherAvaliacao)
        self.btnAvaliar.place(x = 100, rely = 0.45, width = 200)

        self.btnDeletar = Button(self.janelaAtual, text = "Deletar", command = self.deletarAvaliacao)
        self.btnDeletar.place(x = 300, rely = 0.45, width = 200)

        self.btnCancelar = Button(self.janelaAtual, text = "Cancelar", command = self.limparCampos)
        self.btnCancelar.place(x = 500, rely = 0.45, width = 200)

        self.janelaAtual.mainloop()


    def atualizarTabela(self, idProduto):
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        listaAvaliacoes = sa.get_todas_avaliacoes(idProduto)

        for i in listaAvaliacoes:
            self.tv.insert("", "end", values = (i.idAvaliacao, i.comentario, i.data, i.idUsuario, i.idProduto))


    def limparCampos(self):
        self.janelaAtual.destroy()
        tm.Menu(Tk())


    def deletarAvaliacao(self):
        try:
            itemSelecionado = self.tv.selection()[0]
            msgBox = messagebox.askquestion("Deletar Avaliação", "Deseja excluir avaliação?", icon = "warning")
            
            if msgBox == "yes":
                valores = self.tv.item(itemSelecionado, "values")
                idProduto = valores[0]

                da.delete_avaliacao_id(idProduto)
                self.tv.delete(itemSelecionado)
                messagebox.showinfo("Exclusão de Avaliação", "Avaliação excluída com sucesso")
            else:
                return

        except:
            messagebox.showinfo("Deletar Avaliação", "Selecione uma avaliação")


    def preencherAvaliacao(self):
        self.janelaAtual.destroy()
        tpa.PreencherAvaliacao(Tk(), self.produto)


if __name__ == "__main__":
    janela = Tk()
    minhaJanela = MenuAvaliacao(janela, 3)