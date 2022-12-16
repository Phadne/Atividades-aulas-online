#  Escreva um programa Python para obter o maior número de uma lista.
def max_num_in_list( list ):  
    max = list[ 0 ]  
    for a in list:  
        if a > max:  
            max = a  
    return max  
print(max_num_in_list([7,8,101,34,90])) 