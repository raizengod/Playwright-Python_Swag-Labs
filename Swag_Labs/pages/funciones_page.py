#Importamos todo lo necesario
import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from datetime import datetime
import os

#1- Creamos una clase
class Funciones_Globales:
    #2- Creamos una función incial 'Constructor'-----ES IMPORTANTE TENER ESTE INICIADOR-----
    def __init__(self, page):
        self.page= page
    
    #3- Nueva función para generar el nombre de archivo con marca de tiempo
    def _generar_nombre_archivo_con_timestamp(self, prefijo):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3] # Quita los últimos 3 dígitos para milisegundos más precisos
        return f"{prefijo}_{timestamp}"
    
    #4- crear primera función basica, para este caso creamos una para tiempo de espera que espera recibir el parametro tiempo
    #En caso de no pasar el tiempo por parametro, el mismo tendra un valor de medio segundo
    def Esperar(self, tiempo=0.5):
        time.sleep(tiempo)
    
    #5- Crear proxima función
    #El valor tiempo es para indicar el tiempo que se tardará en hacer el scroll
    def Scroll(self, horz, vert, tiempo=0.5): 
        #Usamos 'self' ya que lo tenemos inicializada en __Init__ y para que la palabra page de la función funcione es necesaria
        self.page.mouse.wheel(horz, vert)
        time.sleep(tiempo)
        
    #6- Nueva función global para tomar captura de pantalla
    def tomar_captura(self, nombre_base, directorio):
        if not os.path.exists(directorio):
            os.makedirs(directorio) # Crea el directorio si no existe
        nombre_archivo = self._generar_nombre_archivo_con_timestamp(nombre_base)
        ruta_completa = os.path.join(directorio, f"{nombre_archivo}.jpg")
        self.page.screenshot(path=ruta_completa)
        print(f"Captura guardada en: {ruta_completa}") # Para ver dónde se guardó
        self.Esperar()
        
    #7- Crear nueva función para campo y capture la imagen
    def cTextoImg(self, selector, texto, nombre_base, directorio, tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        #La siguiente linea es para resaltar el campo en azul
        t.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.fill(texto)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #8- Crear nueva función para hacer click
    """def Click(self, selector, nombre, tiempo=0.5):
        s=self.page.locator(selector)
        s.highlight()
        expect(s).to_be_visible()
        expect(s).to_be_enabled()
        expect(s).to_contain_text(nombre)
        s.click()
        time.sleep(tiempo)"""
        
    #9- Crear nueva función para hacer click con captura de imagen
    def Click_Img(self, selector, nombre_base, directorio, tiempo=0.5):
        s=self.page.locator(selector)
        expect(s).to_be_visible()
        expect(s).to_be_enabled()
        s.highlight()
        s.click()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #10- Crear nueva función para comboBox Por valor
    def Combo_Value(self, selector, valor, nombre_base, directorio, tiempo=0.5):
        c= self.page.locator(selector)
        c.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(c).to_be_visible()
        expect(c).to_be_enabled()
        c.select_option(valor)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #11- Crear nueva función para comboBox por label
    def Combo_Label(self, selector, eqtiqueta, nombre_base, directorio, tiempo=0.5):
        c= self.page.locator(selector)
        c.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(c).to_be_visible()
        expect(c).to_be_enabled()
        c.select_option(eqtiqueta)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #12- Crear nueva función para mensaje de confirmación
    def Men_Confir(self, selector, mensaje, nombre_base, directorio, tiempo= 0.5):
        mc= self.page.locator(selector)
        mc.highlight()
        expect(mc).to_be_visible()
        expect(mc).to_contain_text(mensaje)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #13- Función para validar titulo de una página
    def Titulo_Web(self,texto, nombre_base, directorio, tiempo= 0.5):
        expect(self.page).to_have_title(texto)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #14- Función para validar URL
    def Validar_URL(self, texto, tiempo= 0.5):
        expect(self.page).to_have_url(re.compile(texto))
        time.sleep(tiempo)
        
    #15- Crear nueva función para mensaje de confirmación no visible
    def Men_No_Visible(self, selector, nombre_base, directorio, tiempo= 0.5):
        mc= self.page.locator(selector)
        expect(mc).to_be_hidden()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #16- Crear nueva función para validar label
    def Validar_Label(self, selector, texto, nombre_base, directorio, tiempo= 0.5):
        tl= self.page.locator(selector)
        expect(tl).to_be_visible()
        tl.highlight()
        expect(tl).to_contain_text(texto)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
             
    #17- Crear función para hacer click fuera de un campo
    def Mouse_xy(self, x, y, nombre_base, directorio, tiempo= 0.5):
        self.page.mouse.click(x, y)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #18- Crear función para hacer presionar la tecla TAB en el teclado
    def Tab_Pess(self, tiempo= 0.5):
        self.page.keyboard.press("Tab")
        time.sleep(tiempo)
        
    #19- Crear función para cargar archivo
    def Cargar_Arch(self, selector, archivo, nombre_base, directorio, tiempo= 0.5):
        ca= self.page.locator(selector)
        ca.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        #ca.click()
        ca.set_input_files(archivo)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #20- Crear función para remover carga de archivo
    def Remo_arch(self, selector, nombre_base, directorio, tiempo= 0.5):
        ca= self.page.locator(selector)
        ca.highlight()
        expect(ca).to_be_visible()
        expect(ca).to_be_enabled()
        ca.set_input_files([]) #Colocando corchetes en los parentesis indicamos que pasaremos una lista, pero la misma estara vacía
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #21- Crear nueva función para hacer click en el primer elemento de la lista dinamica
    def Click_First(self, selector, nombre_base, directorio, tiempo= 0.5):
        cb=self.page.locator(selector)
        cb.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        cb.first.click()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
    
    #22- Crear nueva función para validar que un tipo imagen es visible
    def Elemento_Visible(self, selector, nomre_base, directorio, tiempo= 0.5):
        ev= self.page.locator(selector)
        expect(ev).to_be_visible()
        ev.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)