A = [2, 3, 6, 7, 9]
B = [1, 2, 6, 10, 11]
C = [0, 1, 2, 11, 14, 15]
D = [6, 7, 9, 10, 12, 13] 


# ini 
# end

def calcular_mediana(A, B):
  mid1 = int(len(A) / 2)
  mid2 = int(len(B) / 2)

  if A[mid1] == B[mid2]:
    return A[mid1]

  if len(A) == 1: # caso base 1
    return (A[0] + B[0]) / 2

  elif len(A) == 2: # caso base 2
    R = [min(A[0], B[0]), max(A[ 0], B[0]), min(A[1], B[1]), max(A[1], B[1])]
    return (R[1] + R[2]) / 2
  
  elif A[mid1] < B[mid2]:
    return calcular_mediana(A[mid1 + 1:], B[:mid2])
  
  else:
    return calcular_mediana(A[:mid1], B[mid2:])    


print(calcular_mediana(C,D))
