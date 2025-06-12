import pytest #Es importante que se importe esta libreria para usar de manera mas profesional las multiples pruebas
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorHome import HomePageLocators
from selectores.selectorCarrito import CarritoPageLocators

prefijoEvi= "Carrito_"
rutaEvi= "evidencia/imagen/Carrito"

def test_ingresar_carrito_sin_prod(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    
    #Ingresar al carrito
    FG.Click_Img(HS.selectorCarritoCompra(), prefijoEvi, rutaEvi)
    #Se verifica que se está en la ruta correcta
    FG.Validar_URL(".*/cart.html")
    #Se valida elementos en la pantalla de carrito sin productos listados
    FG.Validar_Label(CS.selectorTituloCarrito(), "Your Cart", prefijoEvi, rutaEvi)
    FG.Validar_Label(CS.selectorColumCantidad(), "QTY", prefijoEvi, rutaEvi)
    FG.Validar_Label(CS.selectorColumDescripcion(), "Description", prefijoEvi, rutaEvi)
    FG.Contar_Y_Verificar_no_contenedores(CS.selectorContenedor(), prefijoEvi, rutaEvi)
    FG.Elemento_No_Visible(CS.selectorRemoverProd(), prefijoEvi, rutaEvi)
    FG.Elemento_Visible(CS.selectorComprar(), prefijoEvi, rutaEvi, 1)

def test_ir_a_home(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Ir a la pantalla de compra de productos
    FG.Click_Img(CS.selectorComprar(), prefijoEvi, rutaEvi)
    #Se valida ruta actual de URL
    FG.Validar_URL(".*/inventory.html")
    #Se valida visibilidad de contenedores de productos
    FG.Contar_Y_Verificar_contenedores(HS.selectorContenedorProducto(), prefijoEvi, rutaEvi, 1)
    
def test_ver_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Agregar un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi)
    #Ingresar al carrito
    FG.Click_Img(HS.selectorCarritoCompra(), prefijoEvi, rutaEvi)
    #Se valida visibilidad de contenedores de productos
    FG.Contar_Y_Verificar_contenedores(CS.selectorContenedor(), prefijoEvi, rutaEvi)
    #Verificando nombre de producto
    FG.Validar_Label(CS.selectorNombreProd(), "Sauce Labs Backpack", prefijoEvi, rutaEvi)
    #Verificando cuantidificador de unidades por producto
    FG.Validar_Label(CS.selectorContIndividualProd(), "1", prefijoEvi, rutaEvi)
    #Verificando descripción de de producto
    FG.Verificar_Texto_Contenido(CS.selectorDescProd(), "carry.allTheThings() with the sleek, streamlined", prefijoEvi, rutaEvi)
    #Verificar precio de producto
    FG.Precio_Individual_Elemento(CS.selectorPrecProd(), "$29.99", CS.obtenerValor(), prefijoEvi, rutaEvi, 1)
    
def test_remover_un_prod_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Hacer click en el botón remover
    FG.Click_Img(CS.selectorRemoverProd(), prefijoEvi, rutaEvi, 1)
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi)
        
    
def test_ver_varios_producto_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Ir a la pantalla de compra de productos
    FG.Click_Img(CS.selectorComprar(), prefijoEvi, rutaEvi)
    #Agregar un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi)
    FG.Click_Img(HS.selectorAgregarBrillo(), prefijoEvi, rutaEvi)
    FG.Click_Img(HS.selectorAgregarTshirt(), prefijoEvi, rutaEvi)
    
    #Ingresar al carrito
    FG.Click_Img(HS.selectorCarritoCompra(), prefijoEvi, rutaEvi)
    #Verificar contador de productos en el carrito
    FG.Validar_Label(HS.selectorContador(), "3", prefijoEvi, rutaEvi)
    #Se valida visibilidad de contenedores de productos
    FG.Contar_Y_Verificar_contenedores(CS.selectorContenedor(), prefijoEvi, rutaEvi)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_nombre_esperado = ["Sauce Labs Backpack", 
                            "Sauce Labs Bike Light", 
                            "Sauce Labs Bolt T-Shirt"]
    #Verificando nombre de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorContenedor(), lista_nombre_esperado, prefijoEvi, rutaEvi, 1)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_unidad_esperada = ["1", 
                            "1", 
                            "1"]
    #Verificando cuantidificador de unidades por producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorContIndividualProd(), lista_unidad_esperada, prefijoEvi, rutaEvi)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_desc_esperada = [f"carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.", 
                           f"A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.", 
                           f"Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt."]
    #Verificando descripción de de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorDescProd(), lista_desc_esperada, prefijoEvi, rutaEvi)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_precio_esperada = ["$29.99", 
                           "$9.99",
                           "$15.99"]
    #Verificar precio de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorPrecProd(), lista_precio_esperada, prefijoEvi, rutaEvi, 1)
    
def test_remover_prod_carrito(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Hacer click en el botón remover
    FG.Click_Img(CS.selectorRemoverProd(), prefijoEvi, rutaEvi, 1)
    FG.Validar_Label(HS.selectorContador(), "2", prefijoEvi, rutaEvi)
    
def test_cancelar_flujo_compra_cliente(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Iniciamos flujo checkout
    FG.Click_Img(CS.selectorInicarCheckout(), prefijoEvi, rutaEvi, 1)
    
    #Verificar visualización de campos de la pantalla información del cliente
    FG.Validar_Label(CS.selectorInfoPersonal(), "Checkout: Your Information", prefijoEvi, rutaEvi)
    FG.Validar_URL(".*/checkout-step-one.html",0)
    FG.Elemento_Visible(CS.selectorTxtNombre(), prefijoEvi, rutaEvi)
    FG.Elemento_Visible(CS.selectorTxtApellido(), prefijoEvi, rutaEvi)
    FG.Elemento_Visible(CS.selectorTxtCodigoPostal(), prefijoEvi, rutaEvi)
    
    #Cancelamos checkout
    FG.Click_Img(CS.selectorCancelarCompra(), prefijoEvi, rutaEvi, 1)
    
def test_mensajes_error_nombre_datos_cliente(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)    
    
    #Se valida regresar a la pantalla de mi carrito
    FG.Validar_Label(CS.selectorTituloCarrito(), "Your Cart", prefijoEvi, rutaEvi)
    
    #Iniciamos nuevamente flujo checkout
    FG.Click_Img(CS.selectorInicarCheckout(), prefijoEvi, rutaEvi, 1)
    
    #Click continuar sin completar datos de campos de la pantalla información del cliente
    FG.Click_Img(CS.selectorContinuar(), prefijoEvi, rutaEvi, 1)
    
    #Verificar primer mensaje de error
    FG.Men_Confir(CS.selectorError(), "Error: First Name is required", prefijoEvi, rutaEvi)
    
    #Cerrar label mensaje de error
    FG.Click_Img(CS.selectorCerrar(), prefijoEvi, rutaEvi)
    
def test_mensajes_error_apellido_datos_cliente(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)    
    
    #Completar datos de campos nombre de la pantalla información del cliente
    FG.cTextoImg(CS.selectorTxtNombre(), "Paper", prefijoEvi, rutaEvi)
    FG.Click_Img(CS.selectorContinuar(), prefijoEvi, rutaEvi, 1)
    
    #Verificar primer mensaje de error
    FG.Men_Confir(CS.selectorError(), "Error: Last Name is required", prefijoEvi, rutaEvi)
    
    #Cerrar label mensaje de error
    FG.Click_Img(CS.selectorCerrar(), prefijoEvi, rutaEvi, 1)
    
def test_mensajes_error_zip_datos_cliente(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)    
    
    #Completar datos de campos nombre y apellido de la pantalla información del cliente
    FG.cTextoImg(CS.selectorTxtApellido(), "Rock", prefijoEvi, rutaEvi)
    FG.Click_Img(CS.selectorContinuar(), prefijoEvi, rutaEvi, 1)
    
    #Verificar primer mensaje de error
    FG.Men_Confir(CS.selectorError(), "Error: Postal Code is required", prefijoEvi, rutaEvi)
    
    #Cerrar label mensaje de error
    FG.Click_Img(CS.selectorCerrar(), prefijoEvi, rutaEvi, 1)
    
def test_completar_datos_cliente_compra_preview(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)    
    
    #Completar datos de campos de la pantalla información del cliente
    FG.cTextoImg(CS.selectorTxtCodigoPostal(), "333-568", prefijoEvi, rutaEvi)
    
    #Continua siguiente pantalla
    FG.Click_Img(CS.selectorContinuar(), prefijoEvi, rutaEvi, 1)

def test_cancelar_flujo_compra_preview(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
        
    #Verificar visualización de la pantalla preview de la compra
    FG.Validar_Label(CS.selectorPreview(), "Checkout: Overview", prefijoEvi, rutaEvi)
    FG.Validar_URL(".*checkout-step-two.html",0)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_nombre_esperado = ["Sauce Labs Bike Light",
                             "Sauce Labs Bolt T-Shirt"]
    #Verificando nombre de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorProdPreview(), lista_nombre_esperado, prefijoEvi, rutaEvi, 1)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_unidad_esperada = ["1", 
                            "1"]
    #Verificando cuantidificador de unidades por producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorCuantPreview(), lista_unidad_esperada, prefijoEvi, rutaEvi)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_desc_esperada = [f"A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.", 
                           f"Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt."]
    #Verificando descripción de de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorDescPreview(), lista_desc_esperada, prefijoEvi, rutaEvi)
    
    #Pasando la lista de textos esperados como parámetro.
    lista_precio_esperada = ["$9.99",
                             "$15.99"]
    #Verificar precio de producto
    FG.Verificar_Lista_Texto_Contenido(CS.selectorPrecPreview(), lista_precio_esperada, prefijoEvi, rutaEvi, 1)
    
    #Cancelamos checkout
    FG.Scroll(0, 500)
    FG.Click_Img(CS.selectorCancelarCompra(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL(".*/inventory.html",0)
    FG.Validar_Label(HS.selectorContador(), "2", prefijoEvi, rutaEvi)

def test_finalizar_compra_exitosa(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)    
    
    #Ingresar al carrito
    FG.Click_Img(HS.selectorCarritoCompra(), prefijoEvi, rutaEvi, 1)
    #Iniciar flujo checkout
    FG.Click_Img(CS.selectorInicarCheckout(), prefijoEvi, rutaEvi, 1)
    #Completar datos clientes
    FG.cTextoImg(CS.selectorTxtNombre(), "Paper", prefijoEvi, rutaEvi)
    FG.cTextoImg(CS.selectorTxtApellido(), "Rock", prefijoEvi, rutaEvi)
    FG.cTextoImg(CS.selectorTxtCodigoPostal(), "333-568", prefijoEvi, rutaEvi)
    FG.Click_Img(CS.selectorContinuar(), prefijoEvi, rutaEvi, 1)
    #Verificar visualización del sumario en preview y continuar
    FG.Scroll(0, 500)
    FG.Elemento_Visible(CS.selectorSumario(), prefijoEvi, rutaEvi)
    FG.Click_Img(CS.selectorFinalizarCompra(), prefijoEvi, rutaEvi, 1)
    #Verificar pantalla final
    FG.Validar_URL(".*/checkout-complete.html")
    FG.Verificar_Texto_Contenido(CS.selectorCompleta(), "Checkout: Complete!", prefijoEvi, rutaEvi)
    FG.Elemento_Visible(CS.selectorLogo(), prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(CS.selectorAgradecimiento(), "Thank you for your order!", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(CS.selectorDespacho(), "Your order has been dispatched, and will arrive just as fast as the pony can get there!", prefijoEvi, rutaEvi)
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi)
    #Ir a pantalla home
    FG.Click_Img(CS.selectorHome(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL(".*/inventory.html")

"""Este siguiente caso de prueba falla motivado que:
RESULTADO ESPERADO: Cuando un usuario no tiene productos agregados al carrito y se procede a iniciar el flujo checkout se debe mostrar
un mensaje de error y debe permanecer en la misma pantalla del carrito
RESULTADO OBTENIDO: El usuario es redireccionado a la primera pantalla del checkput y no se visualiza mensaje de error"""   
@pytest.mark.skip(reason= "No se obtiene el resultado esperado")
def test_checkout_sin_producto(set_up_login):
    page= set_up_login
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'CarritoSelector'
    CS= CarritoPageLocators(page)
    
    #Ingresar al carrito
    FG.Click_Img(HS.selectorCarritoCompra(), prefijoEvi, rutaEvi)
    #Se verifica que se está en la ruta correcta
    FG.Validar_URL(".*/cart.html", 1)
    #Hacer click en el botón checkout
    FG.Click_Img(CS.selectorInicarCheckout(), prefijoEvi, rutaEvi)
     #Se valida elementos en la pantalla de carrito sin productos listados
    FG.Validar_Label(CS.selectorTituloCarrito(), "Your Cart", prefijoEvi, rutaEvi)
    #Se valida mensaje visible en pantalla indicando que no hay productos
    FG.Elemento_Visible(CS.selectorError(), prefijoEvi, rutaEvi, 1)
    