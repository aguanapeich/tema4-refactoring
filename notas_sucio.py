a=10
b= 3
c=7

def f(a, b, c): 
    r = (a + b + c) / 3 
    return r 

def check(x): 
    if x >= 5: 
        print("aprobado") 
        return True 
    else: 
        print("suspendido") 
        return False 

def f2(a, b, c): 
    r = (a + b + c) / 3 
    if r >= 5: 
        print("aprobado") 
        return True 
    else: 
        print("suspendido") 
        return False 

def mostrar(nombre, a, b, c): 
    print("Alumno: " + nombre) 
    print("Nota 1: " + str(a)) 
    print("Nota 2: " + str(b)) 
    print("Nota 3: " + str(c)) 
    media = (a + b + c) / 3 
    print("Media: " + str(media)) 
    if media >= 9: 
        print("Sobresaliente") 
    if media >= 7 and media < 9: 
        print("Notable") 
    if media >= 5 and media < 7: 
        print("Aprobado") 
    if media < 5: 
        print("Suspenso") 
print("----------------------") 


def main(): 
    mostrar("Ana García", 8, 7, 9) 
    mostrar("Luis Pérez", 4, 5, 3) 
    mostrar("Marta Gómez", 6, 7, 5) 
main() 
