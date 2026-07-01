import tkinter as tk
import cadastrodepessoas as tela
from tkinter import messagebox as mb

if __name__ == '__main__':
    janela = tk.Tk()
    janela.title("Cadastro de pessoas")
    tela = tela.CadastroPessoas(janela)
    janela.mainloop()