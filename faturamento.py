from tkinter import *

window = Tk()

window.geometry('600x600')
window.title('Gerar faturamento')

usernameVar = StringVar()
passwordVar = StringVar()


def adminLogin():
    titleLabel = Label(window, text='FATURAMENTO EM PYTHON')
    titleLabel.grid(row=0, column=0, columnspan=2, padx=(40, 0), pady=(10, 0))

    loginLabel = Label(window, text='Administrador Login:')
    loginLabel.grid(row=1, column=2, columnspan=2, padx=20, pady=10)

    usernameLabel = Label(window, text='Usuario:')
    usernameLabel.grid(row=2, column=2)

    passwordLabel = Label(window, text='Senha:')
    passwordLabel.grid(row=3, column=2)

    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3)

    passwordEntry = Entry(window, textvariable=passwordVar)
    passwordEntry.grid(row=3, column=3)


adminLogin()

window.mainloop()
