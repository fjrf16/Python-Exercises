# 1 - crear una funcion que genere una escusa aleatoria con esos datos 
# 2 - creeis otra funcion que cuente el numero de repeticiones de letras en cada array
# 3 - suprimir repeticiones en un array y devolver el array sin la repeticion
# 4 - function que invierta todos los valores de el array

import random, math

# datos iniciales 

surnames = ['10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
escuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined']
dates = ['Jeferson', 'Matilda', 'R@fael', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']


def randomExcuse(arr):

    val=arr[random.randint(0,len(arr)-1)]

    return val

def exercise1(surnames, escuses, dates):
    result=randomExcuse(surnames)+' '+ randomExcuse(escuses)+' '+randomExcuse(dates)
    return result

#print(exercise1(surnames,escuses,dates))

#------------------------------------------------------
def countLetterRep(arr):    
    newArr=[]
    for i in arr:
            newArr.append(i+' '+str(countLetterWord(i)))
    return newArr

def countLetterWord(word):
    obj={}
    wordLC= word.lower()
    for i in wordLC:
        if i in obj:
            obj[i]=obj[i]+1
        else:
            obj[i]=1
    return obj
   
print(countLetterRep(surnames))
#---------------------------------------------------------

def suprress(arr):

    return list(set(arr))

#print(suprress(surnames))

#------------------------------------------------------

def reverseString(chain):
    return chain[::-1]

def reverseArray(arr):
    rewind=arr[::-1]
    newArr=[]
    for i in rewind:
        newArr.append(reverseString(i))        
    return newArr

#print(reverseArray(surnames))