import re
import tkinter as tk
from datosAutomata import Q,S,F,D
from datosMaquina import datos
q0 = 'q0={q0}'
#Automata
def verificacionLlaves(cadena):
    epsilon = False
    tipoDeAutomata = 'AFD'
    contador=0
    conexionesAux = ""
    for i in range (3,len(D)):
        if(D[i] != "(" and D[i] != ")" and  D[i] != "\n"): 
            if(i != len(D)-2):
                conexionesAux = conexionesAux + D[i]     
    conexionesAuxList = conexionesAux.split(',')

    # print(conexionesAuxList)
    for valores in conexionesAuxList:
     
        if(valores.count('{')>=1 or valores.count('}')):
            tipoDeAutomata = 'AFND'
    
 
    if tipoDeAutomata == 'AFND':
   
        resultado = AFND(conexiones3(D),cadena)
       
    elif tipoDeAutomata == 'AFD':
        
        resultado = AFND(conexiones(D),cadena)
    return  resultado   
   
def conexiones(D):
    conexiones_D = [[],[],[]]
    contador = 1
    listAux =[]
    conexionesAux = ""
    for i in range (2,len(D)):
        if(D[i] != "{" and D[i] != "}" and D[i] != "(" and D[i] != ")" and  D[i] != "\n"):   
            conexionesAux = conexionesAux + D[i]

    conexionesAuxList = conexionesAux.split(',')
    for i in conexionesAuxList:
        if(contador == 1):
            conexiones_D[0].append(i)
            contador = 2
        elif(contador == 2):
            conexiones_D[1].append(i)
            contador = 3
        elif(contador == 3):
            listAux.append(i)
            conexiones_D[2].append(listAux)
            listAux = []
            contador = 1
    return conexiones_D

def conexiones3(D):
    conexiones_D = [[],[],[]]
    conexionesAux = ""
    aux2 = ''
    conta = 0
    for i in range (3,len(D)):
        if(D[i] != "(" and D[i] != ")" and  D[i] != "\n"): 
            if(i != len(D)-2):
                conexionesAux = conexionesAux + D[i]

    conexionesAuxList = conexionesAux.split(',')
    listAux = []
    for i in conexionesAuxList:
        if(conta==0):
            conexiones_D[conta].append(i)
            conta = 1
        elif(conta == 1):
            conexiones_D[conta].append(i)
            conta = 2
        elif(conta == 2):      
            conta = 2
            if('{' in i and '}' in i):
                auxEstadoAbiertoCerrado = i.replace('{','').replace('}','')
                listAux.append(auxEstadoAbiertoCerrado)
                conexiones_D[conta].append(listAux)
                aux2 = ''
                listAux = []
                conta = 0          
            elif '{' in i :
                auxEstadoAbierto = i.replace('{','')
                #print('remplaze cerrado }: ',auxEstadocerrado)
                aux2 =  aux2+ auxEstadoAbierto+','          
            elif '}' in i :
                auxEstadoCerrado = i.replace('}',"")
                aux2 = aux2 + auxEstadoCerrado
                listAux.append(aux2)
                conexiones_D[conta].append(listAux)
                listAux = []
                aux2 = ''
                conta = 0
                
            else:
                aux2 = aux2 + i +','
               
    listAuxiliar = []
    for x in range(0,len(conexiones_D[2])):
        #print((conexiones_D[2][x]))
        auxiliar = conexiones_D[2][x][0].split(',')
        listAuxiliar.append(auxiliar)
    conexiones_D[2] = listAuxiliar
    return conexiones_D
            
def estados(Q):
    estadosAux = ""
    for i in range (2,len(Q)):
        if(Q[i] != "{" and Q[i] != "}" and Q[i] != '\n'):
            estadosAux = estadosAux + Q[i]         
    estadosAuxLista = estadosAux.split(',')
    return estadosAuxLista
    
def alfabeto(S):
    alfabetoAux = ""
    for i in range (2,len(S)):
        if(S[i] != "{" and S[i] != "}" and S[i] != "\n"):
            alfabetoAux = alfabetoAux + S[i]         
    alfabetoAuxLista = alfabetoAux.split(',')
    return alfabetoAuxLista

def inicio(q0):
    inicioAux = ""
    for i in range (3,len(q0)):
        if(q0[i] != "{" and q0[i] != "}" and q0[i] != "\n"):
            inicioAux = inicioAux + q0[i]         
    inicioAuxLista = inicioAux.split(',')
    return inicioAuxLista   

def final(F):
    finalAux = ""
    for i in range (2,len(F)):
        if(F[i] != "{" and F[i] != "}" and F[i] != "\n"):
            finalAux = finalAux + F[i]         
    finalAuxLista = finalAux.split(',')

    return finalAuxLista 

def AFND(ListaPadre,cadena):

    auxEstado = [] 
    auxEstado = inicio(q0)
    bandera = True
    band = False
    
    for i in range(0,len(cadena)):
        band = False
        if(cadena[i] in alfabeto(S)): #if si existe el valor dentro del alfabeto
            letra = cadena[i] 
            for a in range(0,len(ListaPadre[1])): #recorre todas las variables que se encuentran en D ejemplo ['a', 'c', 'c', 'b', 'c'] 

                if(ListaPadre[1][a] == letra): #if la variable de la lista es igual a la variable de la entrada a averificar pasa
                    
                    for aux in auxEstado:  
                        if(ListaPadre[0][a] == aux):
                            auxEstado = ListaPadre[2][a]
                            letra = ""   
                               
                            band = True

        else:
            ImpresionFinal = 'Invalida'
            bandera = False 
    if(bandera == True):
        if(band == True):
            for ultimo in auxEstado:
                   
                    if(ultimo in final(F) ):
                        ImpresionFinal= 'Valida'
                        break
                    else:
                        ImpresionFinal = 'Invalida'
                        
        else:
            ImpresionFinal = 'Invalida'
    return ImpresionFinal

def conversionEntrada(ecuacion):
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    bandera = False
    entreAvalidar = False
    aux = []
    entradaFinal = [[],[],[],[]]
    tipoDatos = ['C','H']
    for i in ecuacion:
        if(i == 'C'):
            entradaFinal[0].append(i)
        elif(i in numeros and bandera == False):
            entradaFinal[1].append(i)
            entreAvalidar = True
        elif(i == 'H'):
            entradaFinal[2].append(i)
            bandera = True
        elif(i in numeros and bandera == True):
            entradaFinal[3].append(i)
    datoAux1 = ''
    datoAux2 = ''
    for i in entradaFinal[1]:
        datoAux1 = datoAux1 + i
    for x in entradaFinal[3]:
        datoAux2 = datoAux2 + x

    entradaFinal[1] = []
    entradaFinal[1].append(datoAux1)
    entradaFinal[3] = []
    entradaFinal[3].append(datoAux2)

    if(entreAvalidar == False):
        entradaFinal[1]= []
        entradaFinal[1].append('vacio')
        for i in entradaFinal:
            if(i[0] == 'vacio'):
                entradaFinal.pop(entradaFinal.index(i))
        

    auxEntrada = []
    for i in entradaFinal:
        auxEntrada.append(i[0])
    entradaFinal = []
    entradaFinal = auxEntrada
    
        
    respuesta = verificacionLlaves(entradaFinal)
    return respuesta

def automata(formula):
    respuesta = conversionEntrada(formula)
    if respuesta == 'Valida': 
        # maquina(formula)
        return True
    elif respuesta == 'Invalida':
         return False
         
#expresion regular
def expresionRegular(formula):
    respuesta = 'Invalido'
    p = re.compile('([C]|[C]([1-9]|[0-9]{2,3}))[H]([1-9]{,2}[02468]|[1-9][02468]{,2})')

    valor = p.fullmatch(formula)
    
    if valor is not None:
        # print('BIEN EXPRESION')
        # automata(formula)
        return True
        
    elif valor is None:
        return False
    
#maquina de turing
def llenadoDatos():
    datosNuevos = datos.replace(' ','')
    # print(datosNuevos)
    arrayAux = []
    arrayCompleto = []
    bandera = False 
    valor = ''
    for i in datosNuevos:
        if(i != '-'):
            if(i != '(' ):
                if i != ',' and i != ')' :
                    valor = valor +i
        
                if( i == ',' or i == ')'):
                    
                    arrayAux.append(valor)
                    valor = ''
                
            
        elif(i == '-'):
            arrayCompleto.append(arrayAux)
            arrayAux = []
    

    transicionesIda = []
    transicionesLlegada = []
    bandera = False
    for i in arrayCompleto:
        if(bandera == False):
            transicionesIda.append(i)
            bandera = True 
        elif bandera == True:
            transicionesLlegada.append(i)
            bandera = False
            
    return transicionesIda,transicionesLlegada 

def llenarCinta(entrada):
    cinta = []
    entradaAux = ''
    for i in entrada:
        if(i != 'H' and i != 'C'):
            entradaAux = entradaAux + i
        elif(i == 'H'):
            break
    nuevaEntrada = entradaAux + 'H'
    
   
  
    for i in nuevaEntrada:
        cinta.append(i)
    cinta.append('B')
    cinta.append('B')
    cinta.append('B')
    
    return cinta

def maquina(entrada):
    transicionesIda,transicionesLlegada = llenadoDatos()
    contadorCinta = 0
    respuestaFinal = ''
    res = ''
    cabezal = 'a00'
    cinta = llenarCinta(entrada)
    banderaMaquina =True
    
    while(banderaMaquina == True):
      
        for i in range(len(transicionesIda)):
            if(cabezal == transicionesIda[i][0] and cinta[contadorCinta] == transicionesIda[i][1]):
             
                cabezal = transicionesLlegada[i][0]
             
                cinta[contadorCinta] = transicionesLlegada[i][1]
           
                if transicionesLlegada[i][2] == 'R':
                    
                    contadorCinta +=1
                elif transicionesLlegada[i][2] == 'S':
                    banderaMaquina = False
             
                break
 
          
   
 
   
    for i in cinta:
        if i != '1' and i != '2' and i != '3' and i != '4'and i != '5'and i != '6'and i != '7'and i != '8'and i != '9'and i != '0' and i != 'H' and i != 'B': 
            respuestaFinal = respuestaFinal + i
    res = respuestaFinal + 'no'
    
    return res
      
def resultadoFinal(formula):
    respuestaFinal = 'Formula Invalida'
    expresion = expresionRegular(formula)
    if(expresion == True):
        automataFND = automata(formula)
        if (automataFND == True):
            nombreCadena =  maquina(formula)
            respuestaFinal = nombreCadena
        elif automataFND == False:
            respuestaFinal =  'Formula Invalida'
    elif expresionRegular == False:
        respuestaFinal = 'Formula Invalida'
    return respuestaFinal
   
def ventana():
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 610, height = 400)
    canvas1.config(bg='white')
    canvas1.pack()

    label1 = tk.Label(root, text='Alcanos a nombre de cadena recta')
    label1.config(font=('helvetica', 22),bg='white',fg='#17202A')
    canvas1.create_window(305, 25, window=label1)

    label2 = tk.Label(root, text='Ingrese su formula Molecular')
    label2.config(font=('helvetica', 18),bg='white',fg='#2C3E50')
    canvas1.create_window(300, 100, window=label2)

    entry1 = tk.Entry (root) 
    entry1.config(width=10,font=('helvetica', 15),bg='#D5D8DC')
    canvas1.create_window(300, 140, window=entry1)

    label3 = tk.Label(root, text= 'Nombre de cadena recta: ')
    label3.config(bg='white',font=('helvetica',16),fg='#1C2833')
    canvas1.create_window(300, 230, window=label3)


    def boton():  
        cadena = entry1.get()
        if resultadoFinal(cadena) == 'Formula Invalida':
            label3.config(text='Error: '+resultadoFinal(cadena),fg='red')
        else:
            label3.config(text='Nombre de cadena recta: '+resultadoFinal(cadena),fg='#1C2833')
    
    button1 = tk.Button(text='Validar Formula', command=boton,bg='#2C3E50', fg='#D5D8DC')
    button1.config(width=12,height=1,font=('helvetica',11))
    canvas1.create_window(300, 180, window=button1)

    root.mainloop()    
    
ventana()
