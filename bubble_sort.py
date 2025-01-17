#Algoritmo Bubble Sort

from random import randint

lista = []

def fill_list(lista, tamanho):
    #Enche a lista com números aleatórios
    for i in range(0, tamanho):
        lista.append(randint(0, 100))

def bubble_sort(lista):
    #O bubble sort passa o maior elemento para sempre e o menor para trás

    for i in range(len(lista)):
        for j in range(0, len(lista) - 1):
            if(lista[j] > lista[j + 1]):
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])

    return lista

fill_list(lista, 20)
print(lista)
print(bubble_sort(lista))