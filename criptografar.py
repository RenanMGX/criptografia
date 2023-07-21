import tkinter as tk
from tkinter import filedialog
from sys import exit
from time import sleep
import pickle

comando_cripto = ["-c", "/c" , "criptografar", "cripto", "encode" , "-e", "/e"]
comando_descript = ["-d", "/d", "descriptografar", "descript", "decode"]
comando_sair = ["sair", "exit", "\s", "-s", "bye"]

def tratar(bruto):
    tratado = ""
    for x in bruto:
        tratado += f"[{x}] "
    return tratado

def procurar_arquivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def tratar_type():
    caminho_arquivo = procurar_arquivo()
    if caminho_arquivo == None:
        return False
    caminho = caminho_arquivo
    nome = caminho_arquivo.split("/")[-1].split(".")[-2]
    tipo = caminho_arquivo.split("/")[-1].split(".")[-1]
    return {"caminho" : caminho, "nome_pi" : f"{nome}.pickle", "nome_py" : f"descript_{nome}.py", "tipo" : tipo}

def encoder():
    print("escolha o arquivo para criptografar")
    caminho_arquivo = tratar_type()
    if caminho_arquivo["tipo"] != "py":
        msg_error("apenas arquivos .py")
        return False
    with open(caminho_arquivo["caminho"], "r") as arqui:
        arquivo = arqui.read().split("\n")
    with open(caminho_arquivo["nome_pi"], "wb") as arqui:
        pickle.dump(arquivo, arqui)
    return True

def decoder():
    print("escolha o arquivo para descriptografar")
    caminho_arquivo = tratar_type()
    if caminho_arquivo["tipo"] != "pickle":
        msg_error("apenas arquivos .pickle")
        return False
    with open(caminho_arquivo["caminho"], "rb") as arqui:
        arquivo = ""
        for x in pickle.load(arqui):
            arquivo += f"{x}\n"
    with open(caminho_arquivo["nome_py"], "w") as arqui:
        arqui.write(arquivo)


def msg_error(msg):
    print(f"Error: {msg}")

def iniciar():
    while True:
        comando = input("comando: ")
        print("")
        comando = comando.lower()
        if comando in comando_sair:
            print("ate logo")
            sleep(1)
            exit()
        elif comando in comando_cripto:
            if encoder():
                sleep(1)
                print("criptografia realizada com exito!")
            else:
                sleep(1)
        elif comando in comando_descript:
            if decoder():
                sleep(1)
                sleep("descriptografia realizada com exito!")
            else:
                sleep(1)
        else:
            print(f"criptografar: {tratar(comando_cripto)}\n")
            print(f"descriptografar: {tratar(comando_descript)}\n")
            print(f"sair: {tratar(comando_sair)}\n")
        

if __name__ == "__main__":
    print("arquivo para criptografar e descriptografar")
    iniciar()
