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
bEntrada.grid(column=1,row=2)
cEntrada = tk.Entry()
cEntrada.grid(column=1,row=3)



def getEntrada():
    dados = EquacaoSegundoGrau(float(aEntrada.get()),float(bEntrada.get()),float(cEntrada.get()))

    textArea = tk.Text(master=janela,height=10,width=25)
    textArea.grid(column=1,row=6)
    resposta = dados.delta()
    textArea.insert(tk.END,resposta)

botao = tk.Button(janela,text='Calcular Eq do segundo grau',command=getEntrada,bg='red')
botao.grid(column=1,row=6)




class EquacaoSegundoGrau:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def delta(self):
        self.delta = (math.pow(self.b,2) - 4*self.a*self.c)
        if self.delta < 0:
            return f'Não há raízes'
        elif self.delta == 0:
            return f'Só há uma raiz {"%.2f" % float((self.b+math.sqrt(self.delta))/self.a*2)}'
        else:
            return f'Há duas raizes {"%.2f" % float((-self.b+math.sqrt(self.delta))/self.a*2)},{"%.2f" % float((-self.b+math.sqrt(self.delta))/self.a*2)}'








foto = Image.open("Captura de tela em 2022-11-30 09-54-56.png")
foto.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(foto)
foto_label = tk.Label(image=photo)
foto_label.grid(column=1,row=0)

janela.mainloop()


