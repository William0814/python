a = 'python'
print('afuera en global: ',a,sep=' ')

def funcion():
    a = 33
    print('resultado dentro de una funcion: ',a,sep=' ')

funcion()