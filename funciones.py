a = 'python'
print('afuera en global: ',a,sep=' ')

def funcion():
    a = 33
    print('resultado dentro de una funcion: ',a,sep=' ')

funcion()

def minimo(l):
    l[0] = 1000

    return min(l)
l = [1,2,3,4]
print(l)
print(minimo(l))
print(l)

def log (*args):
    print('LOG: ', args)

log(1+1,2)
