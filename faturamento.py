from tkinter import *

window = Tk()

window.geometry('800x600')
window.title('Gerar faturamento')

usernameVar = StringVar()
passwordVar = StringVar()

options = ["Banana", "Arroz", "Feijão"]
itemVariable = StringVar()
itemVariable.set = (options[0])
quantVar = StringVar()


def adminLogin():
    titleLabel = Label(window, text='FATURAMENTO EM PYTHON',
                       font='Arial 20', fg='red')
    titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))

    loginLabel = Label(window, text='Administrador Login:', font='Arial 15')
    loginLabel.grid(row=1, column=2, columnspan=2, padx=20, pady=10)

    usernameLabel = Label(window, text='Usuario:', font='Arial 10')
    usernameLabel.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(window, text='Senha:', font='Arial 10')
    passwordLabel.grid(row=3, column=2, padx=20, pady=5)

    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3, padx=20, pady=5)

    passwordEntry = Entry(window, textvariable=passwordVar,
                          show='*')
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton = Button(window, text='Login:', width=20,
                         height=2, font='Arial 10')
    loginButton.grid(row=4, column=2, columnspan=2)

###################################################################################


def mainWindow():
    titleLabel = Label(window, text='FATURAMENTO EM PYTHON',
                       font='Arial 20', fg='green')
    titleLabel.grid(row=0, column=1, columnspan=3, pady=(10, 0))

    addButton = Button(window, text='Add Itens:', width=15,
                       height=2, font='Arial 10')
    addButton.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))

    sairButton = Button(window, text='Sair:', width=15,
                        height=2, font='Arial 10')
    sairButton.grid(row=1, column=4, pady=(10, 0))

    itemLabel = Label(window, text='Selecionar Item:', font='Arial 10')
    itemLabel.grid(row=2, column=0, padx=(5, 0), pady=(10, 0))

    itemDropDown = OptionMenu(window, itemVariable, *options)
    itemDropDown.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))

    quantLabel = Label(window, text='Quantidade:', font='Arial 10')
    quantLabel.grid(row=2, column=2, padx=(5, 0), pady=(10, 0))

    quantEntry = Entry(window, textvariable=quantVar)
    quantEntry.grid(row=2, column=3, padx=(5, 0), pady=(10, 0))

    billButton = Button(window, text='Gerar Nota:', font='Arial 10')
    billButton.grid(row=2, column=4, padx=(5, 0), pady=(10, 0))

###########################################################################


def addItem():

    titleLabel = Label(window, text='FATURAMENTO EM PYTHON', width=30,
                       font='Arial 20', fg='red')
    titleLabel.grid(row=0, column=1, columnspan=5, pady=(10, 0))

    itemNomeLabel = Label(window, text='Nome:', font='Arial 10')
    itemNomeLabel.grid(row=1, column=1, pady=(10, 0))

    itemTaxaLabel = Label(window, text='Taxa Produto:', font='Arial 10')
    itemTaxaLabel.grid(row=1, column=3, pady=(10, 0))

    itemTipoLabel = Label(window, text='Tipo Produto:', font='Arial 10')
    itemTipoLabel.grid(row=2, column=1, pady=(10, 0))

    armazeLabel = Label(window, text='Armazenamento:', font='Arial 10')
    armazeLabel.grid(row=2, column=3, pady=(10, 0))


mainWindow()

window.mainloop()
