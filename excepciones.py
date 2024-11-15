'''def indexador(object, index):
    return object[index]


print(indexador('python',2))
raise IndexError ('exepcion lanzada manualmente...')#captura el error de index
    #print("El parametro esta fuera de rango...")'''

'''#except: ""   captura todos los errores no es recomendable......
except TypeError: #captura el error de type
    print("El parametro tiene que ser numero.....")

print("Hemos salido del try-cash")'''


'''a = 10
b =0

assert(a > b), 'A tiene que ser mayor que b'
print('aqui no ha saltado el assert')'''

'''class mierror(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
raise(mierror('mensaje de error'))'''

def divide (x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('no se puede dividir por cero')
    else:
        print('el resultado es: ')
    finally:
        print('ejecutamos el finally')
divide, (4,12)
divide(4,0)
