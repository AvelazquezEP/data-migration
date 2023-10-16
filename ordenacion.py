import numpy as np

def quicksort(a):
    qsort(a,0,len(a)-1)

def particion(a,i,j): # particiona a[i],...,a[j], retorna posición del pivote
    k=np.random.randint(i,j) # genera un número al azar k en rango i..j
    (a[i],a[k])=(a[k],a[i]) # mueve a[k] al extremo izquierdo
    # a[i] es el pivote
    s=i # invariante: a[i+1..s]<=a[i], a[s+1..t]>a[i]
    for t in range(s,j):
        if a[t+1]<=a[i]:
            (a[s+1],a[t+1])=(a[t+1],a[s+1])
            s=s+1
    # mover pivote al centro
    (a[i],a[s])=(a[s],a[i])
    return s

def qsort(a,i,j): # ordena a[i],...,a[j]
    if i<j: # quedan 2 o más elementos por ordenar
        k=particion(a,i,j)
        qsort(a,i,k-1)
        qsort(a,k+1,j)

def check_order(a):
    print("Ordenado" if np.all(a[:-1]<=a[1:]) else "Desordenado")

a = np.random.random(12)
print(a)
check_order(a)
quicksort(a)
print(a)
check_order(a)