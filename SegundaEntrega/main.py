from clases.clases import Cliente, Producto_dulce

# Generar Cliente
cliente1 = Cliente('33.445.227','Cristian','Varela','Masculino','32','Argentina')
cliente2 = Cliente('55.332.212','Mauricio','Cuello','Masculino','32','Argentina')
cliente3 = Cliente('14.690.122','Rodrigo','Diaz','Masculino','40','Chile')

# Generar Productos
producto_dulce1 = Producto_dulce(1,'Chupetin','Arcor',8.59,'Masticable',15)
producto_dulce2 = Producto_dulce(2,'Caramelo','Arcor',3.59,'Masticable',10)
producto_dulce3 = Producto_dulce(3,'Chocolate','Ferrero',5.59,'Amargo',7)
producto_dulce4 = Producto_dulce(4,'Alfajor','Ferrero',4.99,'Dulce',3)

#############################################################################################################

# Comprar Productos - Cliente 1
print(f"\t====== DETALLE CLIENTE {cliente1.nombre} {cliente1.apellido} / DNI: {cliente1.dni} ======\n")
cliente1.comprar_productos_dulces(producto_dulce1, 7)
cliente1.comprar_productos_dulces(producto_dulce1, 2)
cliente1.comprar_productos_dulces(producto_dulce2, 2)
cliente1.comprar_productos_dulces(producto_dulce3, 1)

# Valida Stock - Cliente 1
cliente1.valida_stock(producto_dulce1)
cliente1.valida_stock(producto_dulce2)
cliente1.valida_stock(producto_dulce3)

# Total - Cliente 1
print(f"El monto total de la compra para el DNI {cliente1.dni} de {cliente1.nombre} {cliente1.apellido} es {round(cliente1.monto_total,2)}\n")
#############################################################################################################


#############################################################################################################
# Comprar Productos - Cliente 2
print(f"\t====== DETALLE CLIENTE {cliente2.nombre} {cliente2.apellido} / DNI: {cliente2.dni} ======\n")
cliente2.comprar_productos_dulces(producto_dulce1, 1)
cliente2.comprar_productos_dulces(producto_dulce2, 2)
cliente2.comprar_productos_dulces(producto_dulce3, 1)

# Valida Stock - Cliente 2
cliente2.valida_stock(producto_dulce1)
cliente2.valida_stock(producto_dulce2)
cliente2.valida_stock(producto_dulce3)

# Total - Cliente 2
print(f"El monto total de la compra para el DNI {cliente2.dni} de {cliente2.nombre} {cliente2.apellido} es {round(cliente2.monto_total,2)}\n")
#############################################################################################################


#############################################################################################################
# Comprar Productos - Cliente 3
print(f"\t====== DETALLE CLIENTE {cliente3.nombre} {cliente3.apellido} / DNI: {cliente3.dni} ======\n")
cliente3.comprar_productos_dulces(producto_dulce2, 4)
cliente3.comprar_productos_dulces(producto_dulce3, 2)
cliente3.comprar_productos_dulces(producto_dulce4, 80) # no existe la cantidad

# Valida Stock - Cliente 1
cliente3.valida_stock(producto_dulce2)
cliente3.valida_stock(producto_dulce3)
cliente3.valida_stock(producto_dulce4)

# Total - Cliente 1
print(f"El monto total de la compra para el DNI {cliente3.dni} de {cliente3.nombre} {cliente3.apellido} es {round(cliente3.monto_total,2)}\n")
#############################################################################################################