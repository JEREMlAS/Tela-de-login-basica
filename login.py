from tkinter import *

def liberado():
    janela2 = Tk()
    janela2.title('Liberado')
    janela2.geometry('200x200')
    ok = Label(janela2, text='LIBERADO')
    ok.place(x=50, y=50)

def pegar_entrada():
    a = entrada1.get()
    b = entrada2.get()
    if a == 'Pedro' and b == '1234':
        acesso['text'] = 'Permitido'
        acesso['foreground'] = 'darkgreen'
        liberado()
    else:
        acesso['text'] = 'senha e/ou \nlogin incorretos'
        acesso['foreground'] = 'red'

#Janela
janela = Tk()
janela.title("Teste da Bagaça")
janela.geometry('240x300')
janela.config(background='white')
#Texto
texto = Label(janela, text='Tela de login', bg='white')
texto.grid(column=1, row=0, padx=0, pady=10)
#Texto2
login = Label(janela, text='Login: ', bg='white')
login.grid(column=0, row=1, padx=10)
senha = Label(janela, text='Senha: ', bg='white')
senha.grid(column=0, row=2, padx=10)
#Entradas
entrada1 = Entry(janela, bg='lightgray', foreground='black')
entrada1.grid(column=1, row=1)
entrada2 = Entry(janela, bg='lightgray', foreground='black')
entrada2.grid(column=1, row=2)
#Botão
botao = Button(janela, text='Enviar', foreground='white', bg='darkblue', command=pegar_entrada)
botao.grid(column=1, row=3, padx=10, pady=10)
#aceitar ou não
acesso = Label(janela, text="", bg='white', foreground="darkblue")
acesso.grid(column=1, row=5)


janela.mainloop()
