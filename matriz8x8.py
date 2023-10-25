#usando listas como hacer una matriz 8x8 en python basico
# crear programa en python;que de manera aleatoria llene esta matiz.
#visualizar canal rojo 
# canal g y b de verde y azul
#inplementar filtro que pase la imagen a color a escalas de grises
import tkinter as tk
import random

# Función para crear una matriz aleatoria 8x8 de colores RGB
def generar_matriz_aleatoria():
    matriz = []
    for _ in range(8):
        fila = []
        for _ in range(8):
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            fila.append(color)
        matriz.append(fila)
    return matriz

# Función para actualizar la imagen en el lienzo
def actualizar_imagen():
    for i in range(8):
        for j in range(8):
            color = matriz[i][j]
            canvas.create_rectangle(j * CELDA, i * CELDA, (j + 1) * CELDA, (i + 1) * CELDA, fill='#%02x%02x%02x' % tuple(color))
    ventana.update()

# Funciones para aplicar filtros de colores
def aplicar_filtro_rojo():
    for i in range(8):
        for j in range(8):
            matriz[i][j] = [matriz[i][j][0], 0, 0]
    actualizar_imagen()

def aplicar_filtro_verde():
    for i in range(8):
        for j in range(8):
            matriz[i][j] = [0, matriz[i][j][1], 0]
    actualizar_imagen()

def aplicar_filtro_azul():
    for i in range(8):
        for j in range(8):
            matriz[i][j] = [0, 0, matriz[i][j][2]]
    actualizar_imagen()

def aplicar_filtro_gris():
    for i in range(8):
        for j in range(8):
            promedio = sum(matriz[i][j]) // 3
            matriz[i][j] = [promedio, promedio, promedio]
    actualizar_imagen()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Imagen")

# Crear un lienzo en la ventana para mostrar la imagen
CELDA = 50
canvas = tk.Canvas(ventana, width=8*CELDA, height=8*CELDA)
canvas.pack()

# Generar una matriz aleatoria de colores RGB
matriz = generar_matriz_aleatoria()

# Actualizar la imagen en el lienzo
actualizar_imagen()

# Crear botones para los filtros
btn_rojo = tk.Button(ventana, text="Filtro Rojo", command=aplicar_filtro_rojo)
btn_verde = tk.Button(ventana, text="Filtro Verde", command=aplicar_filtro_verde)
btn_azul = tk.Button(ventana, text="Filtro Azul", command=aplicar_filtro_azul)
btn_gris = tk.Button(ventana, text="Filtro Escala de Grises", command=aplicar_filtro_gris)

btn_rojo.pack()
btn_verde.pack()
btn_azul.pack()
btn_gris.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()



