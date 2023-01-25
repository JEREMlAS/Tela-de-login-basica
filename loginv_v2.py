import customtkinter
from tkinter import *

username = 'JEREMlAS'
senha = '1234'

def liberado():
    janela2 = Tk()
    janela2.config(background='black')
    janela2.title('Liberado')
    janela2.geometry('250x170')
    ok = Label(janela2, text='LIBERADO', bg='black' ,foreground='green')
    ok.config(font=('Roboto', 30))
    ok.place(x=35, y=50)
    janela2.mainloop()

def pegar_entrada():
    a = entry_username.get()
    b = entry_senha.get()
    if a == username and b == senha:
        liberado()

# Janela
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
janela = customtkinter.CTk()
janela.iconbitmap('icon.ico')
janela.geometry('700x400')
janela.title('Tela de login')
janela.resizable(False, False)


# Fotinho da Tela
img = PhotoImage(file='casa.png')
label_image = customtkinter.CTkLabel(master=janela, image=img, text='')
label_image.place(x=25, y=120)

# Txto acima da mensagem
label1 = customtkinter.CTkLabel(master=janela, text='Faça login para \nutilizar a ferramenta', text_color='#00B0F0')
label1.configure(font = ('Roboto', 28))
label1.place(x=30, y=15)

# Frame
frame = customtkinter.CTkFrame(master=janela, width= 350, height=396)
frame.pack(side=RIGHT)

# Frame widgets
label2 = customtkinter.CTkLabel(master=frame, text='Faça seu login:', text_color='white')
label2.configure(font = ("Roboto", 30))
label2.place(x=65, y=35)

# Campo username
entry_username = customtkinter.CTkEntry(master=frame, placeholder_text='Nome de usuario', width=300)
entry_username.configure(font = ("Roboto", 14))
entry_username.place(x=25, y=105)

label3 = customtkinter.CTkLabel(master=frame, text='   *O campo "username" é obrigatório', text_color='green')
label3.configure(font = ("Roboto", 10))
label3.place(x=25, y=135)

# Campo senha
entry_senha = customtkinter.CTkEntry(master=frame, placeholder_text='Senha de usuario', width=300, show='*')
entry_senha.configure(font = ("Roboto", 14) )
entry_senha.place(x=25, y=175)

label4 = customtkinter.CTkLabel(master=frame, text='   *O campo "senha" é obrigatório', text_color='green')
label4.configure(font = ("Roboto", 10))
label4.place(x=25, y=205)

# Checkbox(Manter logado)
checkbox = customtkinter.CTkCheckBox(master=frame, text='Lembre-se de mim', checkbox_width=20, checkbox_height=20, border_width=2, hover_color='gray')
checkbox.configure(font = ("Roboto", 12))
checkbox.place(x=25, y=240) 

# Botão
button = customtkinter.CTkButton(master=frame, text='Login', width=300, text_color='lightgray', command=pegar_entrada).place(x=25, y=285)


janela.mainloop()
