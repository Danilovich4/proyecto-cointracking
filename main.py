#es interesante trabajar en proyecto con entornos virtuales -> env 
print("hola, este programa pretende ser una copia de Cointracking")

#Importamos librerias
import requests #para http
import json #tratar mejor con json

#Realizamos la solicitud API
#response: objeto paa almacenar respuesta http
response = requests.get('https://jsonplaceholder.typicode.com/posts')

#Importar la funcion del process.py
from process import leer_datos_json, filtrar_posts_por_titulo, guardar_post_filtrados, contar_posts

#Usamos la funcion para leer datos
posts =leer_datos_json('posts.json')

#Obtener y Filtrar datos posts
titulo_a_buscar = input("Introduce una palabra o frase a buscar (separadas por coma): ").strip() #strip() elimina los espacios en blanco al principio y al final de una cadena existente
titulo_a_buscar = [titulo.strip() for titulo in titulo_a_buscar.split(",")] #split(","): funcion para dividir en subcadenas mediante ,
post_filtrados = filtrar_posts_por_titulo(posts, titulo_a_buscar)

#Imprimir resultados
print(f"Post que contienen '{titulo_a_buscar}' en el titulo:")
for post in post_filtrados:
    print(f"- {post['title']}")

cantidad_posts = contar_posts(post_filtrados)
print(f"Se encontraron {cantidad_posts} posts que coinciden con los criterios.")

#Guardar los posts filtrados
guardar_post_filtrados(post_filtrados, 'post_filtrados.json')

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