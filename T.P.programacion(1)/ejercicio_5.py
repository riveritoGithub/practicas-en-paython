def detalle_producto():
    print("bienvenido a nuestra tienda web")
    nombre = "Laptop"
    precio = 999.99  
    cantidad_inventario = 50
    disponible = True 
    print(f"Producto: {nombre}")
    print(f"Precio: ${precio}")
    print(f"Cantidad en inventario: {cantidad_inventario}")
    print(f"Disponible: {'Sí' if disponible else 'No'}")
    precio = 899.99  
    cantidad_inventario -= 1  
    disponible = cantidad_inventario > 0 

   
    print("\n--- Detalle actualizado del producto ---")
    print(f"Producto: {nombre}")
    print(f"Precio: ${precio}")
    print(f"Cantidad en inventario: {cantidad_inventario}")
    print(f"Disponible: {'Sí' if disponible else 'No'}")
detalle_producto()
