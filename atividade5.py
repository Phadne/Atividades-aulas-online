# Escreva um programa Python para obter o menor número de uma lista.
def min_num_in_list( list ):  
    min = list[ 0 ]  
    for a in list:  
        if a < min:  
            min = a  
    return min  
print(min_num_in_list([7,8,101,34,90]))