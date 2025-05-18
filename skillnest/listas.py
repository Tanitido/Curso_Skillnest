# Carga de Datos - creacion del diccionario
ventas = [
    {"fecha": "2025-01-05", "producto": "a", "cantidad": 4, "precio": 850.0},
    {"fecha": "2025-01-05", "producto": "b", "cantidad": 12, "precio": 30.5},
    {"fecha": "2025-01-06", "producto": "a", "cantidad": 2, "precio": 820.0},
    {"fecha": "2025-01-06", "producto": "c", "cantidad": 6, "precio": 60.0},
    {"fecha": "2025-01-07", "producto": "b", "cantidad": 9, "precio": 28.75}
]

# calculo de ingresos
ingresos_totales = 0
for v in ventas:
    ingresos_totales += v["cantidad"] * v["precio"]
# print("ingresos totales:" + " " + str(ingresos_totales)) - test

# Análisis del Producto Más Vendido
ventas_por_producto = {}
for v in ventas:
    p = v["producto"]
    if p in ventas_por_producto:
        ventas_por_producto[p] += v["cantidad"]
    else:
        ventas_por_producto[p] = v["cantidad"]
mayor = None
cantidad_mayor = 0
for producto in ventas_por_producto:
    cantidad = ventas_por_producto[producto]
    if cantidad > cantidad_mayor:
        cantidad_mayor = cantidad
        mayor = producto
p_mas_vendido = mayor
c_mas_vendida = cantidad_mayor
# print("{} con {} unidades".format(p_mas_vendido, c_mas_vendida)) test

# Promedio de Precio por Producto
precios_por_producto = {}
for v in ventas:
    p = v["producto"]
    if p not in precios_por_producto:
        precios_por_producto[p] = [0.0, 0]
    precios_por_producto[p][0] += v["precio"] * v["cantidad"]
    precios_por_producto[p][1] += v["cantidad"]

precio_promedio_por_producto = {}
for p in precios_por_producto:
    datos = precios_por_producto[p]
    suma = datos[0]
    total = datos[1]
    precio_promedio_por_producto[p] = suma / total
# for p in precio_promedio_por_producto: print(p + ": " + str(precio_promedio_por_producto[p])) -test

    # Ventas por Día
ingresos_por_dia = {}
for v in ventas:
    f = v["fecha"]
    ingreso = v["cantidad"] * v["precio"]
    if f in ingresos_por_dia:
        ingresos_por_dia[f] += ingreso
    else:
        ingresos_por_dia[f] = ingreso
# for fecha in ingresos_por_dia: print(fecha + ": " + str(ingresos_por_dia[fecha])) -test

# Resumen de Ventas
resumen_ventas = {}
for p in ventas_por_producto:
    resumen_ventas[p] = {
        "cantidad_total": ventas_por_producto[p],
        "ingresos_totales": precios_por_producto[p][0],
        "precio_promedio": precio_promedio_por_producto[p]
    }
"""    
for producto in resumen_ventas:
    resumen = resumen_ventas[producto]
    print("Producto: " + str(producto))
    print("  Cantidad total: " + str(resumen["cantidad_total"]))
    print("  Ingresos totales: " + str(resumen["ingresos_totales"]))
    print("  Precio promedio: " + str(resumen["precio_promedio"]))
    print()  # línea en blanco para separar productos 
test
"""

# Impresión de Resultados
print("Lista de Ventas:")
for v in ventas:
    print(v)

print("Ingresos Totales:")
print(str(ingresos_totales))

print("Producto más vendido:")
print("{} con {} unidades".format(p_mas_vendido, c_mas_vendida))

print("Precio promedio por producto:")
for p, prom in precio_promedio_por_producto.items():
    print("{}: {}".format(p, prom))

print("Ingresos por día:")
for f, ingreso in ingresos_por_dia.items():
    print("{}: {}".format(f, ingreso))

print("Resumen de ventas:")
for p, resumen in resumen_ventas.items():
    print("{}: {}".format(p, resumen))
