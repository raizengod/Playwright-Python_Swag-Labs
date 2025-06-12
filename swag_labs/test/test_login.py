import re
import time
import random
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pages.base_page import Funciones_Globales
from selectores.selectorLogin import LoginPageLocators

prefijoEvi= "Login_"
rutaEvi= "evidencia/imagen/Login"

def test_CamposVacios(set_up):
    #Inicializamos la variable page que se origina en la función set_up en el archivo de configuración
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
                
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Validamos Label superior    
    FG.Validar_Label(LS.selectorTituloLogin(), "Swag Labs", prefijoEvi, rutaEvi)
    
def test_SinUsuario(set_up):
    page= set_up
            
    #Tiempo de espera para encontrar elemento
    page.set_default_timeout(5000)
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos en el campo clave unicamente
    FG.cTextoImg(LS.selectorClave(), "secret_sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Username is required", prefijoEvi, rutaEvi, 1)
    
def test_SinClave(set_up):
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos en el campo usuario unicamente
    FG.cTextoImg(LS.selectorUsuario(), "standard_user", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Password is required", prefijoEvi, rutaEvi, 1)
    
def test_EspacioAntes(set_up):
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos con espacios antes del ussaurio y clave
    FG.cTextoImg(LS.selectorUsuario(), " standard_user", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), " secret_sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Username and password do not match any user in this service", prefijoEvi, rutaEvi, 1)
    
def test_EspacioFinal(set_up):
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos con espacios después del ussaurio y clave
    FG.cTextoImg(LS.selectorUsuario(), "standard_user ", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), "secret_sauce ", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Username and password do not match any user in this service", prefijoEvi, rutaEvi, 1)
    
def test_EspacioEntreDato(set_up):
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos con espacios en medio del usaurio y clave
    FG.cTextoImg(LS.selectorUsuario(), "standard user", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), "secret sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Username and password do not match any user in this service", prefijoEvi, rutaEvi, 1)
    
def test_UsuarioBloqueado(set_up):
    page= set_up
        
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos de usuario bloqueado
    FG.cTextoImg(LS.selectorUsuario(), "locked_out_user", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), "secret_sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Men_Confir(LS.selectorMsjError(), "Epic sadface: Sorry, this user has been locked out.", prefijoEvi, rutaEvi, 1)
    
def test_CerrarError(set_up):
    page= set_up
    
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Cerramos mensaje de error visaulizado
    FG.cTextoImg(LS.selectorUsuario(), " standard_user", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), " secret_sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorCerrarError(), prefijoEvi, rutaEvi)
    
def test_LoginExitoso(set_up):
    page= set_up
    
    #IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    FG= Funciones_Globales(page) #Este page va ser enviado a la función __init__ en el archivo FuncionesPOM
    #IMPORTANTE: Creamos un objeto de tipo función 'LoginSelector'
    LS= LoginPageLocators(page)
    
    #Luego del paso anterior, ahora si podemos llamar a nuestras funciones creadas en el archivo POM
    FG.Esperar(1)
    
    #Ingresamos datos usaurio y clave correctos
    FG.cTextoImg(LS.selectorUsuario(), "standard_user", prefijoEvi, rutaEvi)
    FG.cTextoImg(LS.selectorClave(), "secret_sauce", prefijoEvi, rutaEvi)
    FG.Click_Img(LS.selectorBtnLogin(), prefijoEvi, rutaEvi)
    FG.Validar_URL(".*/inventory.html",0)