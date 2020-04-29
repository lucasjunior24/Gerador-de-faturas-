from tkinter import *
from tkinter import ttk

window = Tk()

window.geometry('820x600')
window.title('Gerar faturamento')

################## VARIAVEIS DE LOGIN #####################

usernameVar = StringVar()
passwordVar = StringVar()

##########3####### VARIAVEIS MAIN WINDOW ##################

options = ["Banana", "Arroz", "Feijão"]
itemVariable = StringVar()
itemVariable.set(options[0])
quantVar = StringVar()


itemRate = 1
rateVar = StringVar()
rateVar.set("%.2f" % itemRate)
costVar = StringVar()

################ VARIAVEIS DE ADD ITENS #####################

addItemNameVar = StringVar()
addItemTaxaVar = StringVar()
addItemTipoVar = StringVar()
addItemArmazVar = StringVar()


billsTV = ttk.Treeview(height=15, column=("Prod nome", "Quantidade", "Valor"))


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

#########################################################################################

    rateLabel = Label(window, text='Taxa:', font='Arial 10')
    rateLabel.grid(row=1, column=2, padx=(10, 0), pady=(10, 0))

    rateValue = Label(window, textvariable=rateVar)
    rateValue.grid(row=1, column=3, padx=(10, 0), pady=(10, 0))

#########################################################################################

    costLabel = Label(window, text='Valor:', font='Arial 10')
    costLabel.grid(row=3, column=2, padx=(5, 0), pady=(10, 0))

    costEntry = Entry(window, textvariable=costVar)
    costEntry.grid(row=3, column=3, padx=(5, 0), pady=(10, 0))


#########################################################################################

    quantLabel = Label(window, text='Quantidade:', font='Arial 10')
    quantLabel.grid(row=2, column=2, padx=(5, 0), pady=(10, 0))

    quantEntry = Entry(window, textvariable=quantVar)
    quantEntry.grid(row=2, column=3, padx=(5, 0), pady=(10, 0))

    billButton = Button(window, text='Gerar Nota:', font='Arial 10')
    billButton.grid(row=2, column=4, padx=(5, 0), pady=(10, 0))

###########################################################################

    billLabel = Label(window, text='Lista de Produtos:', font='Arial 15')
    billLabel.grid(row=4, column=2)

    billsTV.grid(row=5, column=0, columnspan=5, padx=(10, 0))

    scrollBar = Scrollbar(window, orient='vertical', command=billsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading("#0", text="Nome Prod")
    billsTV.heading("#1", text="Taxa")
    billsTV.heading("#2", text="Quantidade")
    billsTV.heading("#3", text="Valor")


def addItem():

    titleLabel = Label(window, text='FATURAMENTO EM PYTHON', width=30,
                       font='Arial 20', fg='red')
    titleLabel.grid(row=0, column=1, columnspan=5, pady=(10, 0))

    itemNomeLabel = Label(window, text='Nome:', font='Arial 10')
    itemNomeLabel.grid(row=1, column=1, pady=(10, 0))

    itemNomeEntry = Entry(window, textvariable=addItemNameVar)
    itemNomeEntry.grid(row=1, column=2, pady=(10, 0))

    itemTaxaLabel = Label(window, text='Taxa Produto:', font='Arial 10')
    itemTaxaLabel.grid(row=1, column=3, pady=(10, 0))

    itemTaxaEntry = Entry(window, textvariable=addItemTaxaVar)
    itemTaxaEntry.grid(row=1, column=4, pady=(10, 0))

    itemTipoLabel = Label(window, text='Tipo Produto:', font='Arial 10')
    itemTipoLabel.grid(row=2, column=1, pady=(10, 0))

    itemTipoEntry = Entry(window, textvariable=addItemTipoVar)
    itemTipoEntry.grid(row=2, column=2, pady=(10, 0))

    armazeLabel = Label(window, text='Armazenamento:', font='Arial 10')
    armazeLabel.grid(row=2, column=3, pady=(10, 0))

    itemArmazEntry = Entry(window, textvariable=addItemArmazVar)
    itemArmazEntry.grid(row=2, column=4, pady=(10, 0))

    addItemButton = Button(window, text='Add Item:', font='Arial 10')
    addItemButton.grid(row=3, column=3, padx=(5, 0), pady=(10, 0))


addItemNameVar = StringVar()
addItemTaxaVar = StringVar()
addItemTipoVar = StringVar()
addItemArmazVar = StringVar()

mainWindow()

window.mainloop()
