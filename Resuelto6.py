class Producto:
    def __init__(self, nombre, marca, año, precio):
        self.nombre = nombre
        self.marca = marca
        self.año = año
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Marca: {producto.marca}, Año: {producto.año}, Precio: {producto.precio}")

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos para el año {año}:")
            for producto in productos_filtrados:
                print(f"Nombre: {producto.nombre}, Marca: {producto.marca}, Precio: {producto.precio}")
        else:
            print(f"No hay productos para el año {año}")

# Crear algunos productos
producto1 = Producto("Filtro de aire", "Bosch", 2020, 25.99)
producto2 = Producto("Batería", "ACDelco", 2019, 119.99)
producto3 = Producto("Pastillas de freno", "Motorcraft", 2021, 49.99)

# Crear un catálogo y agregar los productos
catalogo = Catalogo()
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos en el catálogo
print("Todos los productos:")
catalogo.mostrar_productos()

# Filtrar productos por año
catalogo.filtrar_por_año(2020)

    
