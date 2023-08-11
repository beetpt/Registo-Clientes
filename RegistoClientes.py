import customtkinter as ctk
from customtkinter import*
from tkinter import messagebox
from tkinter import simpledialog
import os
import csv



def abrir_janela():
    global janela_dados
    global entry_nome, entry_morada, entry_codigo_postal, entry_localidade, entry_contribuinte, entry_contacto, entry_email
    
    janela_dados = ctk.CTkToplevel()
    janela_dados.title("Registo Clientes")
    janela_dados.geometry("450x310")  # Define o tamanho da janela principal
    janela_dados.focus_force()
    janela_dados.attributes("-topmost", True)
    


    label_nome = ctk.CTkLabel(janela_dados, text="Nome do cliente:")
    label_nome.grid(row=0, column=0, sticky=ctk.E, padx=(5, 0))
    entry_nome = ctk.CTkEntry(janela_dados, width=300, height=30)
    entry_nome.grid(row=0, column=1, sticky=ctk.W)

    label_morada = ctk.CTkLabel(janela_dados, text="Morada do cliente:")
    label_morada.grid(row=1, column=0, sticky=ctk.E, padx=(5, 0))
    entry_morada = ctk.CTkEntry(janela_dados, width=300, height=30)
    entry_morada.grid(row=1, column=1, sticky=ctk.W)

    label_codigo_postal = ctk.CTkLabel(janela_dados, text="Código postal:")
    label_codigo_postal.grid(row=2, column=0, sticky=ctk.E, padx=(5, 0))
    entry_codigo_postal = ctk.CTkEntry(janela_dados, width=75,height = 30)
    entry_codigo_postal.grid(row = 2,column = 1 ,sticky = ctk.W)

    label_localidade = ctk.CTkLabel(janela_dados,text="Localidade do cliente:")
    label_localidade.grid(row = 3,column = 0 ,sticky = ctk.E,padx=(5 ,0))
    entry_localidade = ctk.CTkEntry(janela_dados,width = 200,height = 30)
    entry_localidade.grid(row = 3,column = 1 ,sticky = ctk.W)

    label_contribuinte = ctk.CTkLabel(janela_dados,text="Nº Contribuinte:")
    label_contribuinte.grid(row=4, column=0, sticky=ctk.E, padx=(5, 0))
    entry_contribuinte = ctk.CTkEntry(janela_dados, width=75,height = 30)
    entry_contribuinte.grid(row = 4,column = 1 ,sticky = ctk.W)

    label_contacto = ctk.CTkLabel(janela_dados,text="Contacto:")
    label_contacto.grid(row = 5,column = 0 ,sticky = ctk.E,padx=(5 ,0))
    entry_contacto = ctk.CTkEntry(janela_dados,width = 75,height = 30)
    entry_contacto.grid(row = 5,column = 1 ,sticky = ctk.W)

    label_email = ctk.CTkLabel(janela_dados,text="E-mail:")
    label_email.grid(row = 6,column = 0 ,sticky = ctk.E,padx=(5 ,0))
    entry_email = ctk.CTkEntry(janela_dados,width = 200,height = 30)
    entry_email.grid(row = 6,column = 1 ,sticky = ctk.W)

    label_empty = ctk.CTkLabel(janela_dados,text="")
    label_empty.grid(row = 7,column = 0 ,sticky = ctk.E,padx=(5 ,0))

    button_salvar = ctk.CTkButton(janela_dados,text="Salvar",command=salvar_cliente)
    button_salvar.grid(row = 8,column = 1,pady=2)

    button_sair = ctk.CTkButton(janela_dados,text="Sair",command=janela_dados.destroy)
    button_sair.grid(row = 9,column = 1,pady=2)

def salvar_cliente():
    print("salvar_cliente function called")

    global janela_dados

    nome = entry_nome.get()
    morada = entry_morada.get()
    codigo_postal = entry_codigo_postal.get()
    localidade = entry_localidade.get()
    contribuinte = entry_contribuinte.get()
    contacto = entry_contacto.get()
    email = entry_email.get()

    with open('clientes.csv', 'a', newline='', encoding="utf-8-sig") as file:
        writer      = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Nº Cliente', 'Nome', 'Morada', 'Código Postal', 'Localidade', 'Nº Contribuinte', 'Contacto', 'E-mail'])
            num_cliente     = 1
        else:
            with open('clientes.csv', 'r') as f:
                reader = csv.reader(f)
                last_row = list(reader)[-1]
                num_cliente = int(last_row[0]) + 1
        writer.writerow([num_cliente, nome, morada, codigo_postal, localidade, contribuinte, contacto, email])
        #Dá informação dos dados serem salvos
        messagebox.showinfo("Sucesso", "Cliente registado!")

        janela_dados.destroy()

# Define input field variables in the global scope
entry_nome = None
entry_morada = None
entry_codigo_postal = None
entry_localidade = None
entry_contribuinte = None
entry_contacto = None
entry_email = None

####Menu Principal###

janela_principal = ctk.CTk()
janela_principal.title("Menu Clientes")
janela_principal.geometry("400x350")
janela_principal.iconbitmap("icons8-scroll-emoji-96.ico")

#Definir Butões
def button_nome():
    CTkLabel.configure(text="Procura por nome")
def button_contribunte():
    CTkLabel.configure(text="Procura por Contrubuinte")
def button_telemovel():
    CTkLabel.configure(text="Procura por Telemovel")
def button_inserircliente():
    CTkLabel.configure (text="Inserir Novo Cliente")
def button_sair():
   CTkLabel.configure(text="Sair")


###Funções Busca Cliente###
def procurar_cliente():
    # Get the name to search for from the user
    procurar_cliente_nome = simpledialog.askstring("Procurar Cliente", "Insira o nome do cliente:")
    
    # Read the data from the CSV file
    with open('clientes.csv', 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    
    # Search for the client data
    for row in data:
        if row[1] == procurar_cliente_nome:
            # Client found, display data in new window
            janela_dados = ctk.CTkToplevel()
            janela_dados.title(f"Dados do Cliente: {procurar_cliente_nome}")
            janela_dados.geometry("450x310")
            
            for i, field in enumerate(header):
                label = ctk.CTkLabel(janela_dados, text=f"{field}:")
                label.grid(row=i, column=0, sticky=ctk.W, padx=(5, 0))
                value = ctk.CTkLabel(janela_dados, text=row[i])
                value.grid(row=i, column=1, sticky=ctk.W)
                    
            return
                
    
    # Client not found, display error message
    messagebox.showerror("Erro", f"Cliente '{procurar_cliente_nome}' não encontrado.")

###Nova Entrada de Busca Contribuinte###
def procurar_cliente_contribuinte():
    # Get the name to search for from the user
    procurar_cliente_contribuinte = simpledialog.askstring("Procurar Cliente", "Insira o Nº Contribuinte:")
    
    # Read the data from the CSV file
    with open('clientes.csv', 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    
    # Search for the client data
    for row in data:
        if row[5] == procurar_cliente_contribuinte:
            # Client found, display data in new window
            janela_dados = ctk.CTkToplevel()
            janela_dados.title(f"Dados do Cliente: {procurar_cliente_contribuinte}")
            janela_dados.geometry("450x310")
            
            for i, field in enumerate(header):
                label = ctk.CTkLabel(janela_dados, text=f"{field}:")
                label.grid(row=i, column=0, sticky=ctk.W, padx=(5, 0))
                value = ctk.CTkLabel(janela_dados, text=row[i])
                value.grid(row=i, column=1, sticky=ctk.W)
                    
            return
                
    
    # Client not found, display error message
    messagebox.showerror("Erro", f"Cliente '{procurar_cliente_contribuinte}' não encontrado.")


###Nova Entrada de Busca Contacto###
def procurar_cliente_contacto():
    # Get the name to search for from the user
    procurar_cliente_contacto = simpledialog.askstring("Procurar Cliente", "Insira o Nº Contacto:")
    
    # Read the data from the CSV file
    with open('clientes.csv', 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    
    # Search for the client data
    for row in data:
        if row[6] == procurar_cliente_contacto:
            # Client found, display data in new window
            janela_dados = ctk.CTkToplevel()
            janela_dados.title(f"Dados do Cliente: {procurar_cliente_contacto}")
            janela_dados.geometry("450x310")
            
            for i, field in enumerate(header):
                label = ctk.CTkLabel(janela_dados, text=f"{field}:")
                label.grid(row=i, column=0, sticky=ctk.W, padx=(5, 0))
                value = ctk.CTkLabel(janela_dados, text=row[i])
                value.grid(row=i, column=1, sticky=ctk.W)
                    
            return
                
    
    # Client not found, display error message
    messagebox.showerror("Erro", f"Cliente '{procurar_cliente_contacto}' não encontrado.")


#Define o texto representado na Labele e botões
CTkLabel = ctk.CTkLabel(janela_principal, text="Procurar Clientes por:")
CTkLabel.pack(pady=5)

procurar_nome = CTkButton(janela_principal, text="Nome", command=procurar_cliente)
procurar_nome.pack(pady=5)

procurar_contribuinte = CTkButton(janela_principal, text="Contribuinte", command=procurar_cliente_contribuinte)
procurar_contribuinte.pack(pady=5)

procurar_telemovel = CTkButton(janela_principal, text="Telemovel", command=procurar_cliente_contacto)
procurar_telemovel.pack(pady=5)

CTkLabel = ctk.CTkLabel(janela_principal, text="Inserir Clientes")
CTkLabel.pack(pady=5)

press_button = CTkButton(janela_principal, text="Inserir Novo Cliente", command=abrir_janela)
press_button.pack(pady=5)

press_button = CTkButton(janela_principal, text="Sair", command=janela_principal.destroy)
press_button.pack(pady=20, side="top")

author_label = ctk.CTkLabel(janela_principal, text="Autor: Carlos Mação\n Version: 1.0.1")
author_label.pack(pady=10, side="bottom")

janela_principal.mainloop()
