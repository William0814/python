def selection_sort(arr, n):
    for i in range(n):
        ## para almacenar el indice del elemento mínimo
        min_element_index = i
        for j in range(i + 1, n):
            ##comprobando y reemplezando el índice minimo del elemento
            if arr[j]< arr[min_element_index]:
                min_element_index = j
                ## intercambiando el elemento actual con elemento minimo
        arr[i], arr[min_element_index]= arr[min_element_index], arr[i]
if __name__=='__main__':
    ## inicializacion del array
    arr = [3,4,7,8,1,9,5,2,6]
    selection_sort(arr, 9)

## imprimir el array
print(str(arr))
# --------------------------------------------

def bubble_sort(arr, n):
    for i in range(n):
        ## Iterando de 0 a n-i-1 ya que i elementos ya estan ordenados.
        for j in range(n - i -1):
            # comprobando el siguiente elemento.
            if arr[j]> arr[j+1]:
                # Intercambiando los elementos adyacentes.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
if __name__== '__main__':
    # iniciamos el array
    arr =[3,4,7,8,1,9,5,2,6]
    bubble_sort(arr , 9)
    print(str(arr))
