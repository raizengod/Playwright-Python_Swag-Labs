import pytest #Es importante que se importe esta libreria para usar de manera mas profesional las multiples pruebas
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorLogin import LoginPageLocators
from selectores.selectorHome import HomePageLocators
from selectores.selectorMenu import MenuPageLocators

prefijoEvi= "Menú_"
rutaEvi= "evidencia/imagen/Menú"

def test_verficar_opciones_menu_listada(set_up_menu):
    page= set_up_menu
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #FG.Click_Img(MS.selectorMenu(), prefijoEvi, rutaEvi, 0)
    FG.Verificar_Texto_Contenido(MS.selectorItems(), "All Items", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(MS.selectorAbout(), "About", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(MS.selectorLoguot(), "Logout", prefijoEvi, rutaEvi)
    FG.Verificar_Texto_Contenido(MS.selectorRestaurarContador(), "Reset App State", prefijoEvi, rutaEvi)
    
def test_about_ir_otra_url(set_up_menu):
    page= set_up_menu
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    FG.Click_Img(MS.selectorAbout(), prefijoEvi, rutaEvi, 1)
    
    #Verificar que la URL de la nueva página es la esperada
    FG.Validar_URL("https://saucelabs.com/")
    
    page.go_back()
    FG.Validar_URL(".*/inventory.html")
    
def test_remover_producto_carrito_menu(set_up_menu):
    page= set_up_menu
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #Agregando un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi, 0)
    #Verificamos visibilidad del contador de producto luego de agregar un producto al carrito
    FG.Elemento_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarBrillo(), prefijoEvi, rutaEvi, 0)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarTshirt(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "3", prefijoEvi, rutaEvi, 1)
    
    #Abrir menú
    FG.Click_Img(MS.selectorMenu(), prefijoEvi, rutaEvi, 0)
    #Presionar opción remover todos los productos
    FG.Click_Img(MS.selectorRestaurarContador(), prefijoEvi, rutaEvi)
    #cerramos menú
    FG.Click_Img(MS.selectorCerrar(), prefijoEvi, rutaEvi)
    
    #Verificamos que no se visualiza el contador del carrito
    FG.Elemento_No_Visible(HS.selectorContador(), prefijoEvi, rutaEvi, 0)
    #Verificados que el texto del botoón remoer cambio a agregar
    FG.Elemento_Visible(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi, 0)
    FG.Elemento_No_Visible(HS.selectorRemoverBolso(), prefijoEvi, rutaEvi, 0)
    
def test_cerrar_sesion(set_up_menu):
    page= set_up_menu
    
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'MenuSelector'
    MS= MenuPageLocators(page)
    
    FG.Click(MS.selectorMenu(), "Open Menu")
    FG.Click_Img(MS.selectorLoguot(), prefijoEvi, rutaEvi, 1)
    FG.Validar_URL("https://www.saucedemo.com")
    
def test_logout_con_productos(set_up_menu):
    page= set_up_menu
   
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'HomeSelector'
    HS= HomePageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #Ingresamos datos usaurio y clave correctos
    FG.cTexto(LS.selectorUsuario(), "standard_user")
    FG.cTexto(LS.selectorClave(), "secret_sauce")
    FG.Click(LS.selectorBtnLogin(), "Login")
    FG.Validar_URL(".*/inventory.html",0)
    
    #Agregando un producto al carrito
    FG.Click_Img(HS.selectorAgregarBolso(), prefijoEvi, rutaEvi, 0)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarBrillo(), prefijoEvi, rutaEvi, 0)
    #Agregar otro producto al carrito
    FG.Click_Img(HS.selectorAgregarTshirt(), prefijoEvi, rutaEvi, 0)
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "3", prefijoEvi, rutaEvi, 1)
    
    #Cerrar sesión
    FG.Click(MS.selectorMenu(), "Open Menu")
    FG.Click_Img(MS.selectorLoguot(), prefijoEvi, rutaEvi, 1)
    
    #Abrir sesión
    FG.cTexto(LS.selectorUsuario(), "standard_user")
    FG.cTexto(LS.selectorClave(), "secret_sauce")
    FG.Click(LS.selectorBtnLogin(), "Login")
    FG.Validar_URL(".*/inventory.html",0)
    
    #Verificando contador de productos en el carrito
    FG.Verificar_Texto_Contenido(HS.selectorContador(), "3", prefijoEvi, rutaEvi, 1)