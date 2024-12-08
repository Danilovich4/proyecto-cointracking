# Es interesante trabajar en proyecto con entornos virtuales -> env
print("Hola, este programa pretende ser una copia de Cointracking")

# Importamos librerías
import requests  # Para HTTP
import json  # Para trabajar mejor con JSON

# Importar las funciones del archivo process.py
from process import (
    leer_datos_json,
    filtrar_posts_por_titulo,
    guardar_post_filtrados,
    contar_posts,
    filtrar_post_por_id,
    filtrar_post_por_usuario,
    contar_palabras_en_titulos,
    validar_input,
)

# Usamos la función para leer datos
posts = leer_datos_json('posts.json')

# Obtener y Filtrar datos posts
while True:
    print("\nOpciones disponibles:")
    print("1. Buscar por título")
    print("2. Buscar por ID")
    print("3. Buscar por usuario")
    print("4. Contar palabras en títulos")
    print("5. Salir")

    opcion = validar_input("Elige una opción (1-5): ", tipo="numero")
    
    if opcion == 1:
        titulos_a_buscar = validar_input(
            "Introduce una palabra o frase a buscar (separadas por comas): ", tipo="texto"
        ).split(",")
        titulos_a_buscar = [titulo.strip() for titulo in titulos_a_buscar]
        post_filtrados = filtrar_posts_por_titulo(posts, titulos_a_buscar)
    
    elif opcion == 2:
        ids_a_buscar = validar_input(
            "Introduce los IDs que quieres buscar (separados por comas): ", tipo="lista"
        )
        post_filtrados = filtrar_post_por_id(posts, ids_a_buscar)
    
    elif opcion == 3:
        usuario_id = validar_input("Introduce el ID de usuario: ", tipo="numero")
        post_filtrados = filtrar_post_por_usuario(posts, usuario_id)
    
    elif opcion == 4:
        palabra = validar_input("Introduce la palabra que deseas contar en los títulos: ", tipo="texto")
        cantidad = contar_palabras_en_titulos(posts, palabra)
        print(f"La palabra '{palabra}' aparece {cantidad} veces en los títulos.")
        post_filtrados = []  # No hay posts que filtrar
    
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida.")
        continue

    # Imprimir resultados
    print(f"\nPosts filtrados encontrados: {len(post_filtrados)}")
    for post in post_filtrados:
        print(f"- {post['title']}")

    # Contar y guardar posts filtrados
    cantidad_posts = contar_posts(post_filtrados)
    print(f"Se encontraron {cantidad_posts} posts que coinciden con los criterios.")
    guardar_post_filtrados(post_filtrados, 'posts_filtrados.json')

""""
if response.status_code == 200: #como la respuesta es exitosa de 200, guarda la info en archivo json
    print("solicitud exitosa")
    posts = response.json() #Convertimos datos JSON en objeto Python JSON->Python
    print(posts[:2]) #mostrar los dos primeros posts
    #Guardar datos en archivo JSON
    with open('posts.json','w') as file: #w permite crear o sobrescribir archivo
        json.dump(posts, file, indent=4) #Guardar datos con una identificacion(sepaparacion de lineas) Python->JSON
    print("Los datos han sido guardados en 'post.json'")
else:
    print("Error en solicitud:", response.status_code)
"""