#Escreva uma função Python que pegue duas listas e retorne True se elas tiverem pelo menos um membro comum.
def membro_comum(lista1, lista2):  
     resultado = False  
     for x in lista1:  
         for y in lista2:  
             if x == y:  
                 resultado = True  
                 return resultado  
print(membro_comum([1,2,3,4,5], [5,6,7,8,9]))  
print(membro_comum([1,2,3,4,5], [6,7,8,9])) 