from tkinter import *
from APIGoogleSheet import *
from valid_entries import *
from datetime import datetime


FUNCIONARIOS = [
    'NATHAN',
    'RAFAEL',
    'NATANAEL',
    'POLIANA',
    'IZADORA',
    'GUILHERME'
]


def insere_valores(nome, data, marcacao, hora, mensagem):    
    d = data_valida(data.get()[:10])
    h = hora_valida(hora.get()[:5])
    if data and hora:
        valores = [[nome.get(), d, marcacao.get(), h]]
        escritaGoogleSheets(valores)
        mensagem.grid(columnspan=3, sticky=N)
        mensagem.after(1500, mensagem.grid_forget)
        nome.set("")
        marcacao.set("")
        data.delete(0, END)
        hora.delete(0, END)
    else:
        mensagem["text"] = "Falha ao salvar"
        mensagem["fg"] = "#ff8000"
        mensagem.grid(columnspan=3, sticky=N)
        mensagem.after(1500, mensagem.grid_forget)


class MyButton:
    def __init__(self, frame, text, function, row, col):
        Button(
            frame,
            text=text,
            command=function,
            borderwidth=0,
            bg="#f91599",
            fg="#ffffff",
            width=10,            
        ).grid(row=row, column=col, sticky=W, pady=10)


class MyLabel:
    def __init__(self, frame, text, row, col, columnspan=1, sticky="w", size=10, pady=10):
        Label(
            frame,
            text=text,            
            bg="#484848",
            fg="#ffffff",
            font=f"Helvetica {size} bold",        
        ).grid(row=row, column=col, sticky=sticky, pady=pady, columnspan=columnspan)    
    

class App:
    def __init__(self):
        self.master = Tk()        
        self.master.title("Sistema de Ponto")
        self.master.configure(background="#484848")
        self.master.geometry("300x350+300+300")

        MyLabel(frame=self.master, text="API Google Sheets e Tkinter", row=0, col=0, size=16, columnspan=3, sticky="n")
        MyLabel(frame=self.master, text="@noobpythonbr", row=1, col=0, size=13, columnspan=3, sticky="n")        

        MyLabel(frame=self.master, text="Nome", row=2, col=0)
        varNome = StringVar()
        self.nome = OptionMenu(
            self.master, varNome,*FUNCIONARIOS)
        self.nome["borderwidth"] = 0,
        self.nome["width"] = 29
        self.nome["anchor"] = W
        self.nome["pady"] = 0
        self.nome.grid(row=2, column=1, pady=10, columnspan=2, sticky=W)

        MyLabel(frame=self.master, text="Data", row=3, col=0)        
        self.data = Entry(self.master)
        self.data.grid(row=3, column=1, sticky=W)        

        MyButton(frame=self.master, text="Hoje", function=self.data_atual, row=3, col=2)

        MyLabel(frame=self.master, text="Marcação", row=5, col=0)
        marcacao = StringVar()
        MARCACOES = ['ENTRADA', 'INTERVALO', 'RETORNO', 'SAÍDA']
        self.marcacoes = OptionMenu(
            self.master,
            marcacao,
            *MARCACOES)
        self.marcacoes["borderwidth"] = 0,
        self.marcacoes["width"] = 29
        self.marcacoes["anchor"] = W
        self.marcacoes["pady"] = 0
        self.marcacoes.grid(row=5, column=1, pady=10, columnspan=2, sticky=W)

        MyLabel(frame=self.master, text="Hora", row=6, col=0)        
        self.hora = Entry(self.master)
        self.hora.grid(row=6, column=1, sticky=W)        
        
        MyButton(frame=self.master, text="Agora", function=self.hora_atual, row=6, col=2)
        
        sucesso = Label(
            self.master,
            text="Salvo com sucesso!",
            bg="#484848",
            fg="#15ff00",
            font="Helvetica 12 bold",
        )

        Button(
            self.master,
            text="Enviar",
            borderwidth=0,
            bg="#000000",
            fg="#ffffff",
            width=25, 
            command=lambda: insere_valores(varNome, self.data, marcacao, self.hora, sucesso)
        ).grid(row=8, column=0, columnspan=3, pady=20, sticky=N)

    def data_atual(self):
        self.data.delete(0, END)
        self.data.insert(0, datetime.today().strftime('%d/%m/%Y'))        

    def hora_atual(self):
        self.hora.delete(0, END)
        self.hora.insert(0, datetime.today().time().strftime('%H:%M:%S'))

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
        
