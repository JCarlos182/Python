import os
import tkinter as tk
from tkinter import messagebox

# Função para organizar arquivos
def organizar_arquivos(tipos):
    # Diretório raiz do SO
    base_path = os.path.expanduser('~')

    # Navega no diretório Download
    path = os.path.join(base_path, 'Downloads')
    os.chdir(path)

    # Lista arquivos do diretório atual
    list_files = os.listdir()

    # Criar Pastas
    for tipo in tipos:
        if tipo not in os.listdir():
            os.mkdir(tipo)

    # Organizar Arquivos
    for file in list_files:
        for tipo in tipos:
            if file.endswith('.' + tipo):
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, tipo, file)
                os.replace(old_path, new_path)
                
    messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")

# Função para detectar tipos de arquivos na pasta
def detectar_tipos():
    # Diretório raiz do SO
    base_path = os.path.expanduser('~')

    # Navega no diretório Download
    path = os.path.join(base_path, 'Downloads')
    os.chdir(path)

    # Lista arquivos do diretório atual
    list_files = os.listdir()

    # Detectar tipos de arquivos
    tipos_detectados = set()
    for file in list_files:
        if '.' in file:
            ext = file.split('.')[-1]
            tipos_detectados.add(ext)

    return sorted(tipos_detectados)

# Função chamada ao clicar no botão "Organizar"
def iniciar_organizacao():
    tipos_selecionados = [var.get() for var in vars if var.get()]
    organizar_arquivos(tipos_selecionados)

# Função para marcar ou desmarcar todos os checkbuttons
def alternar_marcar_desmarcar():
    global todos_marcados
    if todos_marcados:
        for var in vars:
            var.set("")
        btn_toggle.config(text="Marcar Todos")
    else:
        primeiro_tipo = tipos_detectados[0]
        for var in vars:
            var.set(primeiro_tipo)
        btn_toggle.config(text="Desmarcar Todos")
    todos_marcados = not todos_marcados

# Interface Gráfica
root = tk.Tk()
root.title("Organizador de Arquivos")

# Tornar a interface responsiva
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(sticky='nsew')

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

label = tk.Label(frame, text="Selecione os tipos de arquivos que deseja organizar:")
label.grid(row=0, column=0, pady=10, padx=10, sticky='w')

# Detectar tipos de arquivos
tipos_detectados = detectar_tipos()
vars = []

# Exibir quantidade de tipos de arquivos detectados
label_qtd = tk.Label(frame, text=f"Tipos de arquivos detectados: {len(tipos_detectados)}")
label_qtd.grid(row=1, column=0, pady=5, padx=10, sticky='w')

# Criar Checkbuttons para cada tipo de arquivo detectado
max_rows = 10
columns = (len(tipos_detectados) + max_rows - 1) // max_rows  # Calcula o número de colunas necessárias

for i, tipo in enumerate(tipos_detectados):
    var = tk.StringVar(value="")
    chk = tk.Checkbutton(frame, text=tipo, variable=var, onvalue=tipo, offvalue="")
    row = i % max_rows + 2  # Ajusta a linha para começar depois das labels
    col = i // max_rows
    chk.grid(row=row, column=col, sticky='w', padx=20, pady=5)
    vars.append(var)

# Variável para controlar o estado de marcar/desmarcar todos
todos_marcados = False

# Botão de marcar/desmarcar todos
btn_toggle = tk.Button(frame, text="Marcar Todos", command=alternar_marcar_desmarcar)
btn_toggle.grid(row=max_rows + 2, column=0, columnspan=columns, pady=10, sticky='ew', padx=10)

button = tk.Button(frame, text="Organizar", command=iniciar_organizacao)
button.grid(row=max_rows + 3, column=0, columnspan=columns, pady=20)

# Ajustar o layout para ser responsivo
for i in range(max_rows + 4):
    frame.rowconfigure(i, weight=1)

for i in range(columns):
    frame.columnconfigure(i, weight=1)

root.mainloop()
