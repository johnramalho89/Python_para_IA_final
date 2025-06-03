def mesmo_caracter(texto, i, j):
    if i < 0 or j < 0 or i >= len(texto) or j >= len(texto):
        return False
    else:
         if texto[i] != texto[j]:
            return False
         else:
            return True    

print(mesmo_caracter("Marcelinha",1,9))
   

