# Importar las librerías necesarias de Flask
from flask import Flask, render_template, request, redirect, session, url_for

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = 'clave123'  # Clave secreta para poder usar sesiones

# Lista de productos disponibles en la tienda
# Cada producto tiene un id, nombre, precio e imagen asociada
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20, "imagen": "/static/images/camiseta.jpg"},
    {"id": 2, "nombre": "Gorra", "precio": 15, "imagen": "/static/images/gorra.jpg"},
    {"id": 3, "nombre": "Guantes", "precio": 10, "imagen": "/static/images/guantes.jpg"},
     {"id": 4, "nombre": "Camisa", "precio": 20, "imagen": "/static/images/camisa.jpg"},
    {"id": 5, "nombre": "Sombrero", "precio": 20, "imagen": "/static/images/sombrero.jpg"},
    {"id": 6, "nombre": "Zapato", "precio": 50, "imagen": "/static/images/zapato.jpg"},
     {"id": 7, "nombre": "Reloj", "precio": 15, "imagen": "/static/images/reloj.jpg"},
    {"id": 8, "nombre": "Zapatilla", "precio": 45, "imagen": "/static/images/zapatilla.jpg"},
    {"id": 3, "nombre": "Casaca", "precio": 25, "imagen": "/static/images/casaca.jpg"}
]

# Ruta principal que muestra el catálogo de productos
@app.route('/')
def catalogo():
    # Renderiza la plantilla catalogo.html con la lista de productos
    return render_template('catalogo.html', productos=productos)

# Ruta para agregar un producto al carrito (se ejecuta al hacer POST)
@app.route('/agregar', methods=['POST'])
def agregar():
    # Obtener el id del producto enviado desde el formulario
    producto_id = int(request.form['id'])

    # Buscar el producto en la lista de productos
    producto = next(p for p in productos if p['id'] == producto_id)

    # Si el carrito no existe en la sesión, se crea como lista vacía
    if 'carrito' not in session:
        session['carrito'] = []

    # Agregar el producto al carrito
    session['carrito'].append(producto)

    # Indicar que la sesión fue modificada (necesario en Flask)
    session.modified = True

    # Redirigir al usuario a la vista del carrito
    return redirect(url_for('ver_carrito'))

# Ruta que muestra el contenido del carrito
@app.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', [])
    total = sum(p['precio'] for p in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

# Inicia la aplicación en
# Inicia la aplicación en
if __name__ == '__main__':
    app.run(debug=True)
