import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

# Datos de entrenamiento
# [peso en gramos, textura (0=lisa, 1=rugosa), color(rojo = 1 verde = 2 anaranajado = 3)]
caracteristicas = [
    [150, 0,1], # manzana
    [170, 0,1], # manzana
    [140, 0,1], # manzana
    [130, 1,3], # naranja
    [150, 1,3], # naranja
    [160, 1,3], # naranja
    [80, 0,2],  # limón
    [90, 0,2],  # limón
    [70, 0,2],  # limón
    [15, 1,1],  # fresa
    [18, 1,1],  # fresa
    [20, 1,1],  # fresa
]

# Etiquetas: 0=manzana, 1=naranja, 2=limón 3-Fresa
etiquetas = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]

# Nombres de las frutas (para visualización)
nombres_frutas = ["Manzana", "Naranja", "Limón", "Fresa"]

# Crear y entrenar el clasificador
clasificador = tree.DecisionTreeClassifier()
clasificador = clasificador.fit(caracteristicas, etiquetas)

# Función para predecir
def predecir_fruta(peso, textura, colores):
    resultado = clasificador.predict([[peso, textura, colores]])
    return nombres_frutas[resultado[0]]

# Ejemplos de predicción
print("Predicción para fruta de 160g y textura lisa (0):",
      predecir_fruta(160, 0,3))
print("Predicción para fruta de 140g y textura rugosa (1):",
      predecir_fruta(140, 1,3))

print(predecir_fruta(15,1,1))

# Actividad para estudiantes:
# 1. Añadir más datos de entrenamiento
# 2. Añadir una nueva característica (por ejemplo, color)
# 3. Añadir una nueva fruta para clasificar