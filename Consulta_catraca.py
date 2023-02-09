import PySimpleGUI as sg
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw()
file_path = askopenfilename(filetypes = (("Text files", "*.txt"), ("CSV files", "*.csv")))

sobre ='''
******  Colégio Universitário  ******

        Criado por: Mário André

'''

# Layout
sg.theme('LightGrey6')

WIN_W = 90
WIN_H = 25

# String variables to reduce loop and menu code!
pesquisar = "Consultar_Alunos"
diretorio: str = "Diretorio"
version = "Catracas"
lista: str = "Lista"
# Menu
menu_layout = [
    ["Pesquisar", [pesquisar, diretorio, "---", "Exit"]],
    ["Ajuda", ["Sobre"]]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("", font=("Consolas", 10), size=(WIN_W, 1), key="_INFO_")],
    [sg.Image('./logo1.png', WIN_W, WIN_H, pad=(250,0))]
]

window = sg.Window(version, layout, margins=(50, 50), resizable=True)


def selecionar():
    Tk().withdraw()
    file_path = askopenfilename(filetypes = (("Text files", "*.txt"), ("CSV files", "*.csv")))
    return file_path

def search_student():
    # Define the layout of the GUI
    layout = [
        [sg.Text('Insira o RA do Aluno:')],
        [sg.InputText()],
        [sg.Button('Search'), sg.Button('Cancel')]
    ]

    # Create the window
    janela = sg.Window('Consulta RA', layout)
    # Loop to continuously read the values in the window
    while True:
        event, values = janela.read()
        if event in (None, 'Exit'):
            janela.close()
            break
        elif event == 'Cancel':
            janela.close()
            break
        elif values[0] != None:
            ra = values[0]
            # Check if a file is selected
            # Read the database
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        result = []
        found = False
        for line in lines:
            columns = line.split()
            if len(columns) > 0 and columns[5] == ra:
                result.append(line)
                found = True
        
        if not found:
            sg.popup(f"No student found with RA '{ra}'.")
        else:
            with open("resultado.txt", "w") as f3:
                for line in result:
                    f3.write(line + "\n")
            
            with open("resultado.txt", "r") as f:
                file_exibir = f.read()
                
            layout2 = [
                [sg.Text('Log Aluno')],
                [sg.Multiline(file_exibir,size=(WIN_W, WIN_H))],
                [sg.Button('Cancel')]
            ]
            try:
                janela2 = sg.Window(version, layout2)
                event1 = janela2.read()
                if event1 in (None, 'Exit'):
                    janela2.close()
                    return True
                elif event1 == 'Cancel':
                    janela2.close()
                    return True
            except:
                sg.popup("Error closing window3.")

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Exit':
        break
    if eventos == "Sobre":
        sg.popup(sobre)
    if eventos == pesquisar:
        search_student()
        os.remove("./resultado.txt")
    if eventos == diretorio:
        file_path = selecionar()

window.close()
