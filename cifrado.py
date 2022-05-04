from Diccionarios import Abc,Code

def cipher(oracion,num):
    cifrado=''
    for i in range(len(oracion)):
        code= Code.get(oracion[i])
        if code>=27:
            cifrado= cifrado+oracion[i]
        else:
            code=code+num
            if code>26:
                code= code-26
            else:
                code=code
            cifrado= cifrado+Abc.get(code)
    
    print(cifrado)

ejemplo='el webo mio ta que ladra'
ejemplo2='nu fnkx vrx cj zdn ujmaj'
print(ejemplo)
cipher(ejemplo,9)