# CLASE CLIENTE
class Cliente():
    def __init__(self, dni, nombre, apellido, sexo, edad, pais):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.pais = pais
        self.monto_total = 0
        
    def comprar_productos_dulces(self, producto_dulce, cantidad_solicitada):
        if producto_dulce:
            stock_disp = producto_dulce.stock - cantidad_solicitada
            if producto_dulce.stock >= stock_disp:
                carro = producto_dulce.generar_producto(self.dni, cantidad_solicitada)
                if carro:
                    self.monto_total += carro.valor * cantidad_solicitada
                    print(f"""Se agregan {cantidad_solicitada} unidad(es) de {producto_dulce.nombre} marca {producto_dulce.marca} al carro de la persona {self.nombre} {self.apellido} - id: {self.dni}
\tNombre Producto: {producto_dulce.nombre}
\tStock Disponible: {producto_dulce.stock-cantidad_solicitada}
\tStock Solicitado: {cantidad_solicitada}
\tStock Real: {stock_disp}
\t\tValor Unitario: {producto_dulce.valor}
\t\tSubtotal (Stock Solicitado * Valor Unitario): {round(producto_dulce.valor*cantidad_solicitada,2)}\n""")
                else:
                    print("*************************** ERROR STOCK ********************************")
                    print(f"La Cantidad supera al Stock del producto {producto_dulce.nombre}\nStock: {producto_dulce.stock}\nSolicita: {cantidad_solicitada}\nStock Real: {stock_disp}")
                    print("*************************** ERROR STOCK ********************************")
            else:
                print(f"No existe suficinte Stock del producto {producto_dulce.nombre}\nStock: {producto_dulce.stock}\nSolicita: {cantidad_solicitada}\nStock Real: {stock_disp}\n")
        else:
            print("No hay Producto")

    def valida_stock(self, producto_dulce):
        if producto_dulce:
            return print(f'El producto {producto_dulce.nombre} de la marca {producto_dulce.marca} tiene stock total de {producto_dulce.stock - producto_dulce.producto_stock} unidad(es)')
            
# CLASE PRODUCTO
class Producto():
    def __init__(self, id_prod, nombre, marca, valor):
        self.id_prod = id_prod
        self.nombre = nombre
        self.marca = marca
        self.valor = valor

    def __str__(self):
        return f"El producto es {self.nombre} y su valor es {self.valor}."

# Herencia
# hereda los atributos de la clase Producto
class Producto_dulce(Producto): 
    def __init__(self, id_prod, nombre, marca, valor, tipo_dulce, stock):
        super().__init__(id_prod, nombre, marca, valor)
        self.tipo_dulce = tipo_dulce
        self.stock = stock
        self.producto_stock = 0
        
    def generar_producto(self, dni, cantidad):
        if self.producto_stock + cantidad > self.stock:
            return None
        else:
            agrega_carro = Carro(self.nombre, self.marca, self.valor, dni, cantidad)
            self.producto_stock += cantidad
            return agrega_carro

class Carro(Producto_dulce):
    def __init__(self, nombre, marca, valor, dni, cantidad):
        super().__init__(1, nombre, marca, valor, dni, 1)  
        self.dni = dni
        self.sesion_id = 1
        self.cantidad = cantidad