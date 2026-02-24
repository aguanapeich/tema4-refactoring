"""
Programa para la gestión de notas de alumnos.
Este script calcula la media de tres notas, asigna una calificación cualitativa
y muestra un informe detallado por pantalla.

Autor: RICARDO PEREZ GUIRAO 
Fecha: 26 de febrero de 2026
"""

def calc_media(n1, n2, n3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        n1 (float): Primera nota del alumno.
        n2 (float): Segunda nota del alumno.
        n3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (n1 + n2 + n3) / 3

def obtener_calificacion(media):
    """
    Determina la etiqueta de calificación según la nota media.

    Args:
        media (float): Nota media del alumno.

    Returns:
        str: Categoría de la nota (Sobresaliente, Notable, Aprobado o Suspenso).
    """
    # Usamos estructura elif para optimizar la evaluación de rangos
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_expediente(nombre, n1, n2, n3):
    """
    Imprime el informe completo del alumno integrando cálculos y etiquetas.

    Args:
        nombre (str): Nombre completo del alumno.
        n1, n2, n3 (float): Calificaciones numéricas.
    """
    media = calc_media(n1, n2, n3)
    calificacion = obtener_calificacion(media)
    
    print("-" * 25)
    print(f"Alumno: {nombre}")
    print(f"Notas: {n1}, {n2}, {n3}")
    print(f"Media: {media:.2f}") # Formateo a dos decimales para mayor limpieza
    print(f"Resultado: {calificacion}")

def main():
    """Función principal que orquesta la ejecución del programa."""
    alumnos = [
        ("Ana García", 8, 7, 9),
        ("Luis Pérez", 4, 5, 3),
        ("Marta Gómez", 6, 7, 5)
    ]
    
    for nombre, n1, n2, n3 in alumnos:
        mostrar_expediente(nombre, n1, n2, n3)

if __name__ == "__main__":
    main()