def FreqNum(Array, ini, fim, comp):

  NumArray = Array[ini]
 
  metade = (ini + fim) // 2 #definindo metade o array
  
  if NumArray < Array[metade]:  #valor a ser encontrado para comparação está a esquerda da metade
    return FreqNum(Array, ini, metade, comp)

  if Array[metade] == NumArray: #verifica se o valor encontrado na metade é igual ao primeiro do array
    if metade == len(Array) - 1:
      print(str(NumArray), "ocorre", str((metade + 1) - comp), "vezes")

    elif Array[metade] < Array[metade + 1]: #o próximo valor sendo diferente, significa que a frequencia foi encontrada
      print(str(NumArray), "ocorre", str((metade + 1) - comp), "vezes")
      if NumArray != Array[len(Array) - 1]:
        return FreqNum(Array, metade + 1, len(Array) - 1, metade + 1) 

    elif Array[metade] == Array[metade + 1]:  #ainda existe mais recorrência do número
      return FreqNum(Array, metade + 1, fim, comp)

Array = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8,8,8, 9,9,9]
FreqNum(Array, 0, len(Array), 0)


