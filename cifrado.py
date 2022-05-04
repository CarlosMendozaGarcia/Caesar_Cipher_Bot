import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from Diccionarios import Abc,Code

stop_words=set(stopwords.words("english"))
def cipher(oracion,num):
    text= sent_tokenize(oracion)
    cifrado=''
    for string in text:
        aux=''
        for i in range(len(string)):
            mayus=string[i].isupper()
            code= Code.get(string[i].lower(),'symbol')
            if code=='symbol':
                aux= aux+string[i]
            else:
                code=code+num
                if code>26:
                    code= code-26
                else:
                    code=code
                if mayus==True:
                    aux= aux+Abc.get(code).upper()
                else:
                    aux= aux+Abc.get(code)
        cifrado= cifrado+aux        
    return cifrado

def decipher(oracion):
    text= sent_tokenize(oracion)
    filtered=[]
    for j in range(1,26):
        decifrado= cipher(oracion,j)
        words= word_tokenize(decifrado) 
        copia= nltk.pos_tag(words)
        decipher=False
        for tokens in copia:
            name= tokens[0].lower()
            tag= tokens[1].lower()
            if tag =='nn' or tag == 'nnp' :
                decipher=False
                decifrado=''
                break
            else:
                decipher=True
                break
        if decipher==True:
            print(decifrado)
            break




ejemplo='Never gonna give you up. Never gonna let you down.'
print(ejemplo)
print(cipher(ejemplo,9))
ejemplo2='Wnena pxwwj pren hxd dy. Wnena pxwwj unc hxd mxfw.'
decipher(ejemplo2)

