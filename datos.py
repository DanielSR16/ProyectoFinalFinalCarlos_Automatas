primerEstado = 2
primerEstadoTotal = ''
segundoEstado = 102
tercerEstado = 202
estadoFinal = 302
primerNumero = 2
segundoNumero = 6
transiciones = ''
estadosFinales = ''


for i in range(1,100):
    data = '('+'q'+str(primerEstado)+','+str(primerNumero)+',{q'+str(segundoEstado)+'}),('+'q'+str(segundoEstado)+',H,{q'+str(tercerEstado)+'}),(q'+str(tercerEstado)+','+str(segundoNumero)+',{q'+str(estadoFinal)+'}),'
    primerEstadoTotal = primerEstadoTotal + 'q'+str(primerEstado)+','
    transiciones = transiciones + data  
    estadosFinales = estadosFinales+ 'q'+str(estadoFinal)+','
    primerEstado += 1
    segundoEstado += 1
    tercerEstado += 1
    estadoFinal += 1
    primerNumero += 1
    segundoNumero += 2
contadorNumeros = 1  
numerosTotal = ''


for x in range(0,202):
    numerosTotal = numerosTotal+',' + str(contadorNumeros)
    contadorNumeros += 1 
contadorTotalEstados = 1
totalEstados = ''
for j in range(400):
    totalEstados = totalEstados + 'q'+str(contadorTotalEstados)+','
    contadorTotalEstados += 1
    
    # print(data)
D = 'D={(q0,C,'+'{q1,'+primerEstadoTotal[:-1]+'}),(q1,H,{q201}),(q201,4,{q301}),'+transiciones[:-1]+'}'
F = 'F={q301,'+estadosFinales[:-1]+'}'
S = 'S={C,H'+numerosTotal+'}'
Q = 'Q={'+totalEstados[:-1]+'}'


print(D)
print('-------------------------------------')
print(F)