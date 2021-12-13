from tkinter import *
from tkinter import messagebox

import telaAvaliacao as ta
import InserirAvaliacao as inserAv


class PreencherAvaliacao:
    def __init__(self, janela, produto):
        self.janelaAtual = janela
        self.produto = produto

        self.janelaAtual.title("Avaliar Produto")
        self.janelaAtual.geometry("400x300+760+390")
        self.janelaAtual.resizable(False, False)

        self.lbComentario = Label(janela, text = "Comentário: ")
        self.lbIdUser = Label(janela, text = "ID usuário: ")

        self.txtComentario = Entry(janela)
        self.txtIdUser = Entry(janela)
        
        self.btnAvaliar = Button(janela, text = "Avaliar", command = self.avaliarProduto)
        self.btnCancelar = Button(janela, text = "Cancelar", command = self.limparCampos)

        self.lbComentario.place(x = 100, y = 50)
        self.txtComentario.place(x = 200 , y = 50)
        self.lbIdUser.place(x = 100, y = 100)
        self.txtIdUser.place(x = 200 , y = 100)
    
        self.btnAvaliar.place(x = 100, y = 150)
        self.btnCancelar.place(x = 200, y = 150)

        self.janelaAtual.mainloop()


    def limparCampos(self):
        self.txtComentario.delete(0, END)
        self.txtIdUser.delete(0, END)

        self.janelaAtual.destroy()
        ta.MenuAvaliacao(Tk(), self.produto)


    def avaliarProduto(self):
        comentario = self.txtComentario.get()
        idUser = self.txtIdUser.get()

        if comentario == "" or idUser == "":
            messagebox.showinfo("Avaliação de produto", "Preencha todos os campos")
        
        else:
            inserAv.inserir_avaliacao(comentario, int(idUser), int(self.produto))
            messagebox.showinfo("Avaliação de produto", "Produto avaliado com sucesso")
            self.limparCampos()


if __name__ == "__main__":
    janela = Tk()
    minhaJanela = PreencherAvaliacao(janela, 3)
