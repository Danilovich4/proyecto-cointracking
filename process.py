print("Archivo donde procesaremos datos JSON")

import json

def leer_datos_json(filename):
    """Leer un archivo JSON y devolver los datos."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encontró.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filename}' no contiene un JSON válido.")
        return []

def filtrar_posts_por_titulo(posts, palabras):
    """Filtrar posts que contienen ciertas palabras en sus títulos."""
    return [
        post for post in posts
        if any(palabra.lower() in post['title'].lower() for palabra in palabras)
    ]

def filtrar_post_por_id(posts, ids):
    """Filtrar posts por una lista de IDs."""
    return [post for post in posts if post['id'] in ids]

def filtrar_post_por_usuario(posts, usuario_id):
    """Filtrar posts por ID de usuario."""
    return [post for post in posts if post['userId'] == usuario_id]

def contar_posts(posts):
    """Contar el número de posts en una lista."""
    return len(posts)

def guardar_post_filtrados(posts, filename):
    """Guardar una lista de posts filtrados en un archivo JSON."""
    try:
        with open(filename, 'w') as file:
            json.dump(posts, file, indent=4)
        print(f"Los posts filtrados se han guardado en '{filename}'.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def contar_palabras_en_titulos(posts, palabra):
    """Contar cuántas veces aparece una palabra en los títulos de los posts."""
    return sum(post['title'].lower().count(palabra.lower()) for post in posts)

def validar_input(mensaje, tipo):
    """
    Solicita al usuario una entrada y la valida según el tipo especificado.
    Tipos válidos: 'numero', 'texto', 'lista'.
    """
    while True:
        entrada = input(mensaje).strip()
        
        if tipo == "numero":
            if entrada.isdigit():  # Verifica si la entrada contiene solo dígitos
                return int(entrada)
            print("Error: Por favor, introduce un número válido.")
        
        elif tipo == "texto":
            if entrada:  # Asegura que no esté vacío
                return entrada
            print("Error: La entrada no puede estar vacía.")
        
        elif tipo == "lista":
            try:
                return [int(item.strip()) for item in entrada.split(",") if item.strip()]
            except ValueError:
                print("Error: Introduce una lista válida de números separados por comas.")
        
        else:
            print("Error: Tipo de validación desconocido.")
            break
