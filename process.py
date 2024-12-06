print("Archivo donde procesaremos datos JSON")

import json

#Funcion Leer archivo JSON
def leer_datos_json(nombre_archivo): #nombre_archivo hace que al llamar la funcion nosotros ya indiquemos cual es el nombre
    with open(nombre_archivo, 'r') as file: #r para leer archivo
        datos = json.load(file) #Cargar datos archivos JSON en variable Python
    return datos


#Funcion para filtrar por titulo
def filtrar_posts_por_titulo(posts, titulo):
    return [
        post 
        for post in posts 
        if any(titulo.lower() in post['title'].lower() for titulo in titulo) #any se usaría si quisiéramos verificar si cualquiera de los valores de un campo (por ejemplo, el título o el cuerpo del post)
            ] #post es lo que devuelve, la resta es una iteracion con condicional

def filtrar_post_por_id (posts, ids_buscar):
    return [post for post in posts if post['id'] in ids_buscar]

def filtrar_post_por_usuario(posts, usuario_id): #Filtra los posts por userId.
    return [post for post in posts if post['userId'] == usuario_id]

def contar_palabras_en_titulos (posts, palabra): #Cuenta cuántas veces aparece una palabra en los títulos de los posts.
    try:
        return sum(post['title'].lower().count(palabra) for post in posts)
    except Exception as e: #Agreguemos una depuración para entender mejor el problema:
        print(f"Error procesando un post: {e}")
        return 0

""" 
#Funcion filtrar contenido
def filtrar_posts_por_contenido(posts, contenido):
    return [post for post in posts if contenido.lower() in post['body'].lower()]
"""
    
#Funcion para guardar lo filtrado
def guardar_post_filtrados(posts_filtrados, nombre_archivo):
    with open(nombre_archivo, 'w') as file:
        json.dump(posts_filtrados, file, indent=4)
    print(f"Los posts filtrados se han guardado en '{nombre_archivo}'")

#Funcion para contar coincidencias
def contar_posts(posts_filtrados):
    return len(posts_filtrados)

#Imprimir contenido
"""Comentario largo
print("Contenido del archivo JSON:")
for post in posts: #esto define que post es 1 elemento del conjunto posts
    print(f"ID: {post['id']}, Titulo: {post['title']}") #f para colocar variables directamente
    print(f"Cuerpo: {post['body']}\n")
"""