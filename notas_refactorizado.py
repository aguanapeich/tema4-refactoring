def calc_media(n1, n2, n3):
    # Calcula y devuelve la media aritmética de tres notas.
    return (n1 + n2 + n3) / 3

def obtener_calificacion(media):
    # Determina la etiqueta de calificación según la nota media.
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_expediente(nombre, n1, n2, n3):
    # Imprime el informe completo del alumno.
    media = calc_media(n1, n2, n3)
    calificacion = obtener_calificacion(media)
    
    print("-" * 22)
    print(f"Alumno: {nombre}")
    print(f"Notas: {n1}, {n2}, {n3}")
    print(f"Media: {media:.2f}")
    print(f"Resultado: {calificacion}")

def main():
    # Datos de los alumnos
    alumnos = [
        ("Ana García", 8, 7, 9),
        ("Luis Pérez", 4, 5, 3),
        ("Marta Gómez", 6, 7, 5)
    ]
    
    for nombre, n1, n2, n3 in alumnos:
        mostrar_expediente(nombre, n1, n2, n3)


    main()