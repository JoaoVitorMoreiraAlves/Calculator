#Importanto as bibliotecas necessárias
from tkinter import *
from tkinter import ttk


#Cores
preto = "#3b3b3b"
branca = "#feffff"
azul = "#38576b"
cinza = "#ECEFF1"
laranja = "#FFAB40"
azul_claro = "#e8fff2"


#Criação da Janela
janela = Tk()
janela.title("Calculadora") #Titulo do app

janela.geometry("277x285") # 277 de largura e 285 de altura

janela.config(bg=cinza)



#Dividindo a Janela em duas partes(Frames)
#Primeiro Frame
frame_tela = Frame(janela, width=277, height=63, bg=azul_claro)

frame_tela.grid(row=0, column=0)

#Segundo Frame
frame_baixo = Frame(janela, width=277, height=222, bg=branca)

frame_baixo.grid(row=1, column=0)




#Variável valor texto
valor_texto = StringVar()

#Variável todos valores
todos_valores = ''
#Funções
def entrar_valores(event):

    global todos_valores #Tornando a variável todos valores global para podermos (?)

    todos_valores = todos_valores + str(event) #Concatenando os valore para mostrar na tela
 
    
    #Passando o valor para a tela
    valor_texto.set(todos_valores)

#Função para calcular
def calcula():
    try:
        global todos_valores
        if '*-+' in todos_valores:
            limpando_tela()
            valor_texto.set('Equação Inválida!')
        elif '*+-' in todos_valores:
            limpando_tela()
            valor_texto.set('Equação Inválida!')
        elif '/-+' in todos_valores:
            limpando_tela()
            valor_texto.set('Equação Inválida!')
        elif '/+-' in todos_valores:
            limpando_tela()
            valor_texto.set('Equação Inválida!')
        else:
            resultado = eval(todos_valores)
            valor_texto.set(resultado) 
            todos_valores = str(resultado)       
    except SyntaxError:
        limpando_tela()
        valor_texto.set('Equação Inválida!')
    except ZeroDivisionError:
        limpando_tela()
        valor_texto.set('Impos. dividir por 0!')



#Função para limpar a tela
def limpando_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#Criando label


app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=7, relief=FLAT, 
                  anchor="e", justify=RIGHT, font="Arial 18 bold", bg=azul_claro)
app_label.place(x=0, y=0)



#Criando botões para o segundo frame
#Botões C, % e /
botao1 = Button(frame_baixo, command=limpando_tela,text="C", width=18, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Botão Clear
botao1.place(x=0, y=0)

botao2 = Button(frame_baixo, command=lambda: entrar_valores("%") ,text="%", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Botão de Divisão para pegar o RESTO
botao2.place(x=140, y=0)

botao3 = Button(frame_baixo, command=lambda: entrar_valores("/") ,text="/", width=8, height=2, 
                    font="Arial 9 bold", bg=laranja, relief=RAISED, overrelief=RIDGE) #Divisão normal
botao3.place(x=210, y=0)


#Botões 7,8,9 e *
botao4 = Button(frame_baixo, command=lambda: entrar_valores("7") ,text="7", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 7
botao4.place(x=0,y=45)

botao5 = Button(frame_baixo, command=lambda: entrar_valores("8") ,text="8", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 8
botao5.place(x=69,y=45)


botao6 = Button(frame_baixo, command=lambda: entrar_valores("9") ,text="9", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 9
botao6.place(x=140,y=45)

botao7 = Button(frame_baixo, command=lambda: entrar_valores("*") ,text="*", width=8, height=2, 
                    font="Arial 9 bold", bg=laranja, relief=RAISED, overrelief=RIDGE) #Simbolo de Multiplicação
botao7.place(x=210, y=45)


#Botões 4,5,6 e -
botao8 = Button(frame_baixo, command=lambda: entrar_valores("4") ,text="4", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 4
botao8.place(x=0,y=90)

botao9 = Button(frame_baixo, command=lambda: entrar_valores("5") ,text="5", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 5
botao9.place(x=69,y=90)


botao10 = Button(frame_baixo, command=lambda: entrar_valores("6") ,text="6", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 6
botao10.place(x=140,y=90)

botao11 = Button(frame_baixo, command=lambda: entrar_valores("-") ,text="-", width=8, height=2, 
                    font="Arial 9 bold", bg=laranja, relief=RAISED, overrelief=RIDGE) #Simbolo de subtração
botao11.place(x=210, y=90)


#Botões 1,2,3 e +
botao12 = Button(frame_baixo, command=lambda: entrar_valores("1") ,text="1", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 1
botao12.place(x=0,y=135)

botao13 = Button(frame_baixo, command=lambda: entrar_valores("2") ,text="2", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 2
botao13.place(x=69,y=135)


botao14 = Button(frame_baixo, command=lambda: entrar_valores("3") ,text="3", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 3
botao14.place(x=140,y=135)

botao15 = Button(frame_baixo, command=lambda: entrar_valores("+") ,text="+", width=8, height=2, 
                    font="Arial 9 bold", bg=laranja, relief=RAISED, overrelief=RIDGE) #Simbolo de adição
botao15.place(x=210, y=135)


#Botões 0,',' e =
botao16 = Button(frame_baixo, command=lambda: entrar_valores("0") ,text="0", width=18, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Número 0
botao16.place(x=0, y=180)

botao17 = Button(frame_baixo, command=lambda: entrar_valores(".") ,text=".", width=8, height=2, 
                    font="Arial 9 bold", bg=cinza, relief=RAISED, overrelief=RIDGE) #Ponto
botao17.place(x=140,y=180)

botao18 = Button(frame_baixo, command=calcula,text="=", width=8, height=2, 
                    font="Arial 9 bold", bg=laranja, relief=RAISED, overrelief=RIDGE) #Simbolo de igual
botao18.place(x=210, y=180)




janela.mainloop() #Abrindo o App e deixando ele em loop até a pessoa fechar