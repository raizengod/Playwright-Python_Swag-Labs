import pytest #Es importante que se importe esta libreria para usar de manera mas profesional las multiples pruebas
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorHome import HomePageLocators

prefijoEvi= "Home_"
rutaEvi= "evidencia/imagen/Home"

def test_contar_productos_en_inventario(set_up_login):
    page = set_up_login

    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)

    print("\n--- Ejecutando test_contar_productos_en_inventario ---")

    # Llamamos a la función global para contar y verificar los productos
    # La función devuelve la cantidad, lo que la hace flexible.
    cantidad_encontrada = FG.Contar_Y_Verificar_contenedores(HS.selectorContenedorProducto(), prefijoEvi, rutaEvi, 1)

    print(f"La prueba finalizó. Se reportaron {cantidad_encontrada} productos en el inventario.")

    # Opcional: Si en algún momento sabes que la cantidad debe ser EXACTAMENTE X,
    # puedes añadir una aserción aquí en el test, pero no es obligatoria
    # si la intención es solo "contar y verificar que haya productos".
    # expect(cantidad_encontrada).to_equal(6) # Por ejemplo, si sabes que siempre deben ser 6.
    

def test_agregar_producto_carrito(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Agregando un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi, 1)
    
def test_verificar_cantidad_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 1)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    
def test_remover_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi)
    #Remover producto del carrito
    FG.Click_Img(HS.selectorRemoverBolso(), prefijoEvi, rutaEvi, 1)
    #Verificamos la no visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi)
    
def test_agregar_multiples_producto_carrito(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Agregando un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi, 0)
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarBrillo(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "2", prefijoEvi, rutaEvi, 1)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarTshirt(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "3", prefijoEvi, rutaEvi, 1)
    
def test_remover_multiples_producto_carrito(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Remover producto del carrito
    FG.Click_Img(HS.selectorRemoverBolso(), prefijoEvi, rutaEvi, 1)
    #Verificamos visibilidad del contador de producto luego de revomer un producto de varios al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "2", prefijoEvi, rutaEvi, 1)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorRemoverBrillo(), prefijoEvi, rutaEvi, 0)
    #Verificamos visibilidad del contador de producto luego de revomer otro producto de varios al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "1", prefijoEvi, rutaEvi, 1)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorRemoverTshirt(), prefijoEvi, rutaEvi, 0)
    #Verificamos la no visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi)
    
def test_multiples_opciones_filtro(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
       
    #Pasando la lista de textos esperados como parámetro.
    lista_texto_esperado = ["Name (A to Z)", 
                            "Name (Z to A)", 
                            "Price (low to high)", 
                            "Price (high to low)"]
    #Prueba que los elementos de la lista contienen múltiples textos
    FG.Verificar_Opciones_ComboBox(HS.selectorFiltro(), lista_texto_esperado, prefijoEvi, rutaEvi, 1)
    
def test_filtro_alfabetico_descendente(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Combo_Value(HS.selectorFiltro(),"za", prefijoEvi, rutaEvi)

    # 2. Definir la lista de nombres de productos esperados en orden descendente
    # ¡Asegurar de que esta lista coincida exactamente con los nombres de la web y el orden Z-A!
    nombres_esperados_za = [
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Onesie",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Backpack"
    ]

    # 4. Llamar a la función global para verificar el orden
    FG.Verificar_Orden_Nombres_Productos(HS.selectorNombres(), nombres_esperados_za, prefijoEvi, rutaEvi)

def test_filtro_alfabetico_ascendente(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Combo_Value(HS.selectorFiltro(),"az", prefijoEvi, rutaEvi)

    # 2. Definir la lista de nombres de productos esperados en orden descendente
    # ¡Asegurar de que esta lista coincida exactamente con los nombres de la web y el orden Z-A!
    nombres_esperados_az = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]

    # 4. Llamar a la función global para verificar el orden
    FG.Verificar_Orden_Nombres_Productos(HS.selectorNombres(), nombres_esperados_az, prefijoEvi, rutaEvi)
    
def test_filtro_precio_menor(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Combo_Value(HS.selectorFiltro(),"lohi", prefijoEvi, rutaEvi)

    #Llamar a la función global para verificar el orden de los precios
    FG.Verificar_Orden_Precios_Productos(HS.selectorPrecios(), prefijoEvi, rutaEvi)
    
def test_filtro_precio_mayor(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Combo_Value(HS.selectorFiltro(),"hilo", prefijoEvi, rutaEvi)

    #Llamar a la función global para verificar el orden de los precios
    FG.Verificar_Orden_Precios_Inverso_Productos(HS.selectorPrecios(), prefijoEvi, rutaEvi)

def test_verificar_descripcion_producto(set_up_login):
    page= set_up_login
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    FG.Combo_Value(HS.selectorFiltro(),"az", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(HS.selectorDetalleBolso(), "carry.allTheThings() with the sleek, streamlined Sly Pack that melds", prefijoEvi, rutaEvi)