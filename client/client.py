import requests
import json
import time

# Define la URL base de la API
API_URL = "http://web:5000"

# Define las rutas de los endpoints de la API
ENDPOINTS = {
    "books": "/books",
}


# Función para hacer una petición GET a la API
def get_books():
    response = requests.get(f"{API_URL}{ENDPOINTS['books']}")
    if response.status_code == 200:
        try:
            books = response.json()
            print("Lista de libros:")
            for book in books['books']:
                print(f"ID: {book['id']}, Título: {book['title']}, Descripción: {book['description']}, Autor: {book['author']}")
        except json.decoder.JSONDecodeError:
            print("Error: La respuesta de la API no es un JSON válido")
    else:
        print(f"Error: No se pudo obtener la lista de libros (Código de estado: {response.status_code})")

# Función para hacer una petición POST a la API
def create_book(book):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{API_URL}{ENDPOINTS['books']}", data=json.dumps(book), headers=headers)
    
    if response.status_code == 201:
        try:
            created_book = response.json().get('book')
            if created_book and 'id' in created_book:
                print(f"Libro creado exitosamente:")
                print(f"ID: {created_book['id']}, Título: {created_book['title']}, Descripción: {created_book['description']}, Autor: {created_book['author']}")
            else:
                print("Error: La respuesta de la API no contiene un libro válido")
        except json.decoder.JSONDecodeError:
            print("Error: La respuesta de la API no es un JSON válido")
    else:
        print(f"Error: No se pudo crear el libro (Código de estado: {response.status_code})")

# Función para hacer una petición PUT a la API
def update_book(book_id, updated_book):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{API_URL}{ENDPOINTS['books']}/{book_id}", data=json.dumps(updated_book), headers=headers)
    if response.status_code == 200:
        updated_book = response.json()['book']
        print("Libro actualizado exitosamente:")
        print(f"ID: {updated_book['id']}, Título: {updated_book['title']}, Descripción: {updated_book['description']}, Autor: {updated_book['author']}")
    else:
        print(f"Error al actualizar el libro (Código de estado: {response.status_code})")

# Función para hacer una petición DELETE a la API
def delete_book(book_id):
    response = requests.delete(f"{API_URL}{ENDPOINTS['books']}/{book_id}")
    if response.status_code == 200:
        print("Libro eliminado exitosamente.")
    else:
        print(f"Error al eliminar el libro (Código de estado: {response.status_code})")

# Ejemplos de uso
new_book = {
    "title": "Nuevo libro",
    "description": "Una descripción",
    "author": "Un autor",
}

print("Obteniendo lista de libros...")
get_books()

print("\nCreando un nuevo libro...")
create_book(new_book)

print("\nObteniendo lista de libros actualizada...")
get_books()

print("\nActualizando el libro con ID 1...")
update_book(2, {"title": "Libro actualizado"})

print("\nObteniendo lista de libros actualizada...")
get_books()

print("\nEliminando el libro con ID 1...")
delete_book(1)

print("\nObteniendo lista de libros actualizada...")
get_books()