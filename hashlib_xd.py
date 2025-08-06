from tkinter import messagebox, simpledialog
import tkinter as tk
import pandas as pd
import hashlib,os

datoscsv = 'cuentas_hashlib.csv'

def hash_contraseña(password):
    return hashlib.sha256(password.encode()).hexdigest()

def guardar():
    cuenta = input_cuenta.get()
    usuario = input_usuario.get()
    password = input_contra.get()

    if not cuenta:
        messagebox.showwarning('Faltan datos ;-;', 'Debes ingresar cuenta y contraseña')
        return

    pass_hash = hash_contraseña(password)
    datos = {'Cuenta': [cuenta], 'Usuario': [usuario], 'Hash': [pass_hash]}

    if os.path.exists(datoscsv):
        df = pd.read_csv(datoscsv)
        df = pd.concat([df, pd.DataFrame(datos)])
    else:
        df = pd.DataFrame(datos)

    df.to_csv(datoscsv)
    messagebox.showinfo('Guardado', 'Ya se guardó pa :D')

def verificar():
    #??? no jala xd
    cuenta = input_buscar.get()
    password = simpledialog.askstring('Contraseña', 'Pon la contraseña:')

    input_hash = hash_contraseña(password)
    df = pd.read_csv(datoscsv)
    pass_datoscsv = df[df['Hash'].str.lower() == cuenta.lower()]

    if pass_datoscsv.empty:
        messagebox.showinfo(':(', 'No hay nada pa D:')
        return
    hash_guardado = pass_datoscsv.iloc[0]['Hash']

    if input_hash == hash_guardado:
        messagebox.showinfo('Biewn', 'Contraseña esta bien :D')
    else:
        messagebox.showerror('Mal', 'Contraseña está mal D:')


root = tk.Tk()
root.title("Hashlib Gestor")
root.geometry("400x300")

tk.Label(root, text="Cuenta").pack()
input_cuenta = tk.Entry(root)
input_cuenta.pack()

tk.Label(root, text="Usuario:").pack()
input_usuario = tk.Entry(root)
input_usuario.pack()

tk.Label(root, text="Contraseña:").pack()
input_contra = tk.Entry(root)
input_contra.pack()

tk.Button(root, text="Guardar Cuenta", command=guardar).pack(pady=10)

tk.Label(root, text="Buscar cuenta:").pack()
input_buscar = tk.Entry(root)
input_buscar.pack()

tk.Button(root, text="Verificar Contraseña", command=verificar).pack(pady=5)

root.mainloop()
