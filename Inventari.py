# inventario_tienda.

# Diccionario para almacenar el inventario
# Estructura: {nombre_producto: (precio, cantidad)}

inventario = {}

# Función para añadir un producto al inventario
def añadir_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return

    try:
        precio = float(input("Precio del producto: "))
        if precio <= 0:
            print("Error: ingresa un precio válido mayor a cero")

        cantidad = int(input("Cantidad disponible: "))
        if cantidad <= 0:
            print("Error: ingresa una cantidad válida mayor a cero")

        inventario[nombre] = (precio, cantidad)
        print(f"Producto {nombre} con precio {precio} con cantidad {cantidad} ha sido añadido correctamente.\n")

    except ValueError:
        print("Error: ingresa un precio y una cantidad válidos (números positivos).")

# Función para consultar un producto
def consultar_producto():
    nombre = input("Nombre del producto a consultar: ").strip()
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto: {nombre}\nPrecio: ${precio:.2f}\nCantidad: {cantidad}")
    else:
        print("El producto no se encuentra en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio():
    nombre = input("Nombre del producto a actualizar: ").strip()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            if nuevo_precio < 0:
                raise ValueError
            cantidad = inventario[nombre][1]
            inventario[nombre] = (nuevo_precio, cantidad)
            print(f"Precio de '{nombre}' actualizado correctamente.")
        except ValueError:
            print("Error: ingresa un precio válido (número positivo).")
    else:
        print("El producto no está en el inventario.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print("El producto no está en el inventario.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = sum(map(lambda item: item[1][0] * item[1][1], inventario.items()))
    print(f"Valor total del inventario: ${total:.2f}")

# Función para mostrar el menú y gestionar las operaciones
def menu():
    while True:

        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        opcion = input("\nSelecciona una opción: ")


        if opcion == "1":
            while True:
             añadir_producto()
             respuesta = input("Deseas agregar otro producto si / no").lower()

        if respuesta == 'no':
            break;
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, elige entre 1 y 6.")

        respuesta = input("Deseas continuar en el menú si / no").lower()

        if respuesta != 'si':
          print("Salida exitosa")
          break

# Ejecutar el menú
menu()