# CatracasHenry7X
Código voltado a leitura de dados de catracas Henry7x
The code imports the PySimpleGUI library and the Tkinter library for GUI creation and file dialog. The Tkinter library is used to open a file dialog box to select a file, which is stored in the "file_path" variable. The file must be a .txt or .csv file.

The layout of the GUI is created using PySimpleGUI, with a menu bar at the top, a text field in the middle, and an image at the bottom. The menu bar has two options: "Pesquisar" and "Ajuda". "Pesquisar" has three sub-options: "Consultar_Alunos", "Diretorio", and "Exit". "Ajuda" has one sub-option: "Sobre".

The "selecionar" function is used to select a file when the "Diretorio" option is selected in the menu. It opens a file dialog and returns the selected file path.

The "search_student" function creates another window that takes the input of a student's RA number. If a file is selected, the function opens it and searches for the student's information using the RA number as a reference. If the student is found, the information is written to a temporary file named "resultado.txt". This file is then opened and displayed in a separate window. If the student is not found, a popup message is displayed saying so.

The main loop listens to events from the GUI and calls the appropriate functions based on the selected options in the menu bar. If the "Exit" option is selected, the loop ends and the window closes.
