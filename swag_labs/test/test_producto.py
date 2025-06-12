import pytest #Es importante que se importe esta libreria para usar de manera mas profesional las multiples pruebas
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorHome import HomePageLocators
from selectores.selectorProducto import DetallePageLocators
from selectores.selectorMenu import MenuPageLocators

prefijoEvi= "Producto_"
rutaEvi= "evidencia/imagen/Producto"

def test_ingresar_por_nombre_producto(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Click(HS.selectorNombreBolso(), "Sauce Labs Backpack")
    #cuando Playwright intenta hacer coincidir .*/inventory-item.html?id=4, el ? está 
    #actuando como un cuantificador para el carácter l justo antes de él, y no como el carácter ? literal que forma parte de la URL.
    #Se necesita "escapar" el carácter ? en la expresión regular para que sea interpretado como un carácter literal y no como un cuantificador. 
    #Se puede hacer esto colocando una barra invertida (\\) antes del ?.
    FG.Validar_URL(r".*/inventory-item.html\?id=4", 0)
    FG.Validar_Label(DS.selectorNombreDetalle(), "Sauce Labs Backpack", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(DS.selectorDescProducto(), "carry.allTheThings() with the sleek, streamlined", prefijoEvi, rutaEvi)
    FG.Precio_Individual_Elemento(DS.selectorPrecProd(), "$29.99", DS.obtenerValor(), prefijoEvi, rutaEvi)
    
def test_regresar_a_home(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    
    FG.Click_Img(DS.selectorBack(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL(".*/inventory.html", 1)
    
def test_ingresar_por_imagen_producto(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Click_Img(HS.selectorImg(), prefijoEvi, rutaEvi)
    #cuando Playwright intenta hacer coincidir .*/inventory-item.html?id=4, el ? está 
    #actuando como un cuantificador para el carácter l justo antes de él, y no como el carácter ? literal que forma parte de la URL.
    #Se necesita "escapar" el carácter ? en la expresión regular para que sea interpretado como un carácter literal y no como un cuantificador. 
    #Se puede hacer esto colocando una barra invertida (\\) antes del ?.
    #Aunque \\? es la forma correcta de escapar el ? en una expresión regular, Python sigue emitiendo una advertencia porque la cadena no está 
    #marcada como una "raw string" (cadena cruda). Sin la r al principio, Python intenta procesar \? como una secuencia de escape normal de Python, lo 
    # cual es ineficaz y genera la advertencia.
    # Se debe usar una raw string agregando el prefijo r justo antes de la comilla de apertura de la cadena. Esto le dice a Python que ignore 
    # el procesamiento de secuencias de escape dentro de esa cadena, permitiendo que la expresión regular reciba \\? literalmente.
    FG.Validar_URL(r".*/inventory-item.html\?id=4", 0)
    FG.Validar_Label(DS.selectorNombreDetalle(), "Sauce Labs Backpack", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(DS.selectorDescProducto(), "carry.allTheThings() with the sleek, streamlined", prefijoEvi, rutaEvi)
    FG.Precio_Individual_Elemento(DS.selectorPrecProd(), "$29.99", DS.obtenerValor(), prefijoEvi, rutaEvi)
    
def test_agregar_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Click_Img(DS.selectorAgregar(), prefijoEvi, rutaEvi, 1)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    
def test_remover_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Click_Img(DS.selectorRemover(), prefijoEvi, rutaEvi, 1)
    #Verificamos que no se visualiza el contador del carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    
def test_remover_prod_cart_menu(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #Agregando un producto al carrito
    FG.Click_Img(DS.selectorAgregar(), prefijoEvi, rutaEvi, 0)
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    
    #Abrir menú
    FG.Click_Img(MS.selectorMenu(), prefijoEvi, rutaEvi, 0)
    #Presionar opción remover todos los productos
    FG.Click_Img(MS.selectorRestaurarContador(), prefijoEvi, rutaEvi)
    #cerramos menú
    FG.Click_Img(MS.selectorCerrar(), prefijoEvi, rutaEvi)
    
    #Verificamos que no se visualiza el contador del carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificados que el texto del botón remover cambio a agregar
    FG.Elemento_No_Visible(DS.selectorRemover(), prefijoEvi, rutaEvi, 0)
    FG.Elemento_Visible(DS.selectorAgregar(), prefijoEvi, rutaEvi, 0)
    
def test_agregar_prod_desc_ver_home(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #Refresh de la web
    page.reload()
    
    #Agregando un producto al carrito desde el detalle
    FG.Click_Img(DS.selectorAgregar(), prefijoEvi, rutaEvi, 0)
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    
    #Regresamos al home
    FG.Click_Img(DS.selectorBack(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL(".*/inventory.html", 1)
    
    #Verificamos que el botón revomer del producto se visualice desde el home
    FG.Elemento_Visible(HS.selectorRemoverBolso(), prefijoEvi, rutaEvi, 1)
    
def test_remover_prod_cart_home(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'DetalleSelector'
    DS= DetallePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Removemos producto desde la pantalla home
    FG.Click_Img(HS.selectorRemoverBolso(), prefijoEvi, rutaEvi, 1)
    
    #Verificamos que no se visualiza el contador del carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    
    #Ingresar al detalle del producto nuevamente
    FG.Click_Img(HS.selectorNombreBolso(), prefijoEvi, rutaEvi, 1)
    
    #Verificados que el texto del botón remover cambio a agregar
    FG.Elemento_No_Visible(DS.selectorRemover(), prefijoEvi, rutaEvi, 0)
    FG.Elemento_Visible(DS.selectorAgregar(), prefijoEvi, rutaEvi, 0)
    
    #Verificamos que no se visualiza el contador del carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    
def test_regresar_home_menu(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Abrir menú desde detalle de producto
    FG.Click_Img(MS.selectorMenu(), prefijoEvi, rutaEvi)
    #Seleccionar opción Todos los items
    FG.Click_Img(MS.selectorItems(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL(".*/inventory.html", 1)
    
    print("\n--- Ejecutando test_contar_productos_en_inventario ---")

    # Llamamos a la función global para contar y verificar los productos
    # La función devuelve la cantidad, lo que la hace flexible.
    cantidad_encontrada = FG.Contar_Y_Verificar_contenedores(HS.selectorContenedorProducto(), prefijoEvi, rutaEvi, 1)

    print(f"La prueba finalizó. Se reportaron {cantidad_encontrada} productos en el inventario.")
    
    #Definir la lista de nombres de productos esperados en orden descendente
    #¡Asegurar de que esta lista coincida exactamente con los nombres de la web y el orden Z-A!
    nombres_esperados = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]

    #Llamar a la función global verificar nombres productos
    FG.Verificar_Orden_Nombres_Productos(HS.selectorNombres(), nombres_esperados, prefijoEvi, rutaEvi)