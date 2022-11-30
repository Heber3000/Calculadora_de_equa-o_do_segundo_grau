import math
import tkinter as tk
from PIL import Image,ImageTk


janela = tk.Tk()
janela.geometry("680x780")
janela.title("Calculador de Equação do Segundo Grau")


a = tk.Label(text="Informe o a:")
a.grid(column=0,row=1)
b = tk.Label(text="Informe o b:")
b.grid(column=0,row=2)
c = tk.Label(text="Informe o c:")
c.grid(column=0,row=3)

aEntrada = tk.Entry()
aEntrada.grid(column=1,row=1)
bEntrada = tk.Entry()
bEntrada.grid(column=1,row=1)
cEntrada = tk.Entry()
cEntrada.grid(column=1,row=1)



def getEntrada():
    dados = EquacaoSegundoGrau(aEntrada.get(),bEntrada.get(),cEntrada.get())

    textArea = tk.Text(master=janela,height=10,width=25)
    textArea.grid(column=1,row=6)
    resposta = f'{dados.verificar_equacao()}\n{dados.delta()}'
    textArea.insert(tk.END,resposta)

    botao = tk.Button(janela,text='Calcular Eq do segundo grau',command=getEntrada,bg='red')
    botao.grid(column=1,row=6)




class EquacaoSegundoGrau:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def verificar_equacao(self):
        if self.a == 0:
            return f'Não é equacao do segundo grau'
        else:
            return f'É equação do segundo grau'

    def delta(self):
        self.delta = math.pow(self.b,2) - 4*self.a*self.c
        if self.delta < 0:
            return f'Não há raízes'
        elif self.delta == 0:
            return f'Há apenas uma raiz {(-self.b+math.sqrt(self.delta))/2*self.a}'
        else:
            return f'Há duas raízes {(-self.b+math.sqrt(self.delta))/2*self.a} e {(-self.b-math.sqrt(self.delta))/2*self.a}'




