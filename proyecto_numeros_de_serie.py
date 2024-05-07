import re, os, time, datetime, math
from pathlib import Path

ruta = "C:\\Users\\user\\Desktop\\Insides\\Cursos\\Udemy\\Python TOTAL - Programador Avanzado en 16 días\\Día 9\\Proyecto día 9\\Mi_Gran_Directorio"
inicio = time.time()
# Regular expression
patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de búsuqeda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t-------')
    for archivo in archivos_encontrados:
        print(f'{archivo}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encontrados: {len(nros_encontrados)}')
    print()
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-'*50)

crear_listas()
mostrar_todo()
