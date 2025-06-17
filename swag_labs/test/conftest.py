#nombra el archivo: Ve a la ubicación de tu archivo y colcoar el nombre a conftest.py
# La convención de conftest.py le indica a Pytest que este archivo contiene fixtures que deben estar disponibles 
# para los tests en ese directorio y sus subdirectorios.
import pytest #Es importante que se importe esta libreria para usar de manera mas profesional las multiples pruebas
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorLogin import LoginPageLocators
from selectores.selectorMenu import MenuPageLocators

#Ruta guardar evidencia en video
eVideoLogin= "Evidencias/Videos"
#Ruta guardar evidencia en imagen
eImagenLogin= "Evidencias/Imagen"
#URL Web
url_Login= "https://www.saucedemo.com/"

#Para indicar que va a ser un fixture utilizamos la siguiente linea
@pytest.fixture(scope= "function")
#Luego de usar el mark creamos nuestra función
def set_up(playwright: Playwright) -> None:    
    browser= playwright.chromium.launch(headless= False, slow_mo= 500)
    context = browser.new_context()
    
    #Con este comando grabamos pantalla en formato video
    #context=browser.new_context(record_video_dir="Evidencias/Videos/UploadPOM")
    
    #Abrir una nueva pagina
    page = context.new_page()
    
    #Con este comando alternativo definimos el tamaño de la pantalla en que se trabaja
    page.set_viewport_size({'width': 1920, 'height': 800})
    
    #Inicializamos trace Viewer y debemos pasar los parametros 'screenshots= True, snapshot= True, sources= True'
    #context.tracing.start(screenshots= True, snapshots= True, sources= True)
    
    #Ir a la URL
    page.goto(url_Login)
    
    #Tiempo de espera para encontrar elemento
    page.set_default_timeout(5000)
    
    #Una forma de retornar la función y no finalice la misma se utiliza la palabra reservada 'yield'
    yield page
    
    # ---------------------
    context.close()
    browser.close()
    
#Para indicar que va a ser un fixture utilizamos la siguiente linea
@pytest.fixture(scope= "session")
#Luego de usar el mark creamos nuestra función
def set_up_login(playwright: Playwright) -> None:    
    browser= playwright.chromium.launch(headless= True, slow_mo= 500)
    context = browser.new_context()
    
    #Con este comando grabamos pantalla en formato video
    #context=browser.new_context(record_video_dir="Evidencias/Videos/UploadPOM")
    
    #Abrir una nueva pagina
    page = context.new_page()
    
    #Con este comando alternativo definimos el tamaño de la pantalla en que se trabaja
    page.set_viewport_size({'width': 1920, 'height': 800})
    
    #Inicializamos trace Viewer y debemos pasar los parametros 'screenshots= True, snapshot= True, sources= True'
    #context.tracing.start(screenshots= True, snapshots= True, sources= True)
    
    #Ir a la URL
    page.goto(url_Login)
    
    #Tiempo de espera para encontrar elemento
    page.set_default_timeout(5000)
    
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Ingresamos datos usaurio y clave correctos
    FG.cTexto(LS.selectorUsuario(), "standard_user")
    FG.cTexto(LS.selectorClave(), "secret_sauce")
    FG.Click(LS.selectorBtnLogin(), "Login")
    FG.Validar_URL(".*/inventory.html",0)
    
    #Una forma de retornar la función y no finalice la misma se utiliza la palabra reservada 'yield'
    yield page
    
    # ---------------------
    context.close()
    browser.close()
    
#Para indicar que va a ser un fixture utilizamos la siguiente linea
@pytest.fixture(scope= "session")
#Luego de usar el mark creamos nuestra función
def set_up_menu(playwright: Playwright) -> None:    
    browser= playwright.chromium.launch(headless= False, slow_mo= 500)
    context = browser.new_context()
    
    #Con este comando grabamos pantalla en formato video
    #context=browser.new_context(record_video_dir="Evidencias/Videos/UploadPOM")
    
    #Abrir una nueva pagina
    page = context.new_page()
    
    #Con este comando alternativo definimos el tamaño de la pantalla en que se trabaja
    page.set_viewport_size({'width': 1920, 'height': 800})
    
    #Inicializamos trace Viewer y debemos pasar los parametros 'screenshots= True, snapshot= True, sources= True'
    #context.tracing.start(screenshots= True, snapshots= True, sources= True)
    
    #Ir a la URL
    page.goto(url_Login)
    
    #Tiempo de espera para encontrar elemento
    page.set_default_timeout(5000)
    
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    #IMPORTANTE: Creamos un objeto de tipo función 'menuSelector'
    MS= MenuPageLocators(page)
    
    #Ingresamos datos usaurio y clave correctos
    FG.cTexto(LS.selectorUsuario(), "standard_user")
    FG.cTexto(LS.selectorClave(), "secret_sauce")
    FG.Click(LS.selectorBtnLogin(), "Login")
    FG.Validar_URL(".*/inventory.html")
    FG.Click(MS.selectorMenu(), "Open Menu", 1)
    
    #Una forma de retornar la función y no finalice la misma se utiliza la palabra reservada 'yield'
    yield page
    
    # ---------------------
    context.close()
    browser.close()