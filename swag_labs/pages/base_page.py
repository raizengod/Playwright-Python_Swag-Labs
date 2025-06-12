#Importamos todo lo necesario
import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from datetime import datetime
import os

class Funciones_Globales:
    
    #2- Creamos una función incial 'Constructor'-----ES IMPORTANTE TENER ESTE INICIADOR-----
    def __init__(self, page):
        self.page= page
    
    #3- Nueva función para generar el nombre de archivo con marca de tiempo
    def _generar_nombre_archivo_con_timestamp(self, prefijo):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3] # Quita los últimos 3 dígitos para milisegundos más precisos
        return f"{prefijo}_{timestamp}"
    
    #4- Crear función basica para tiempo de espera que espera recibir el parametro tiempo
    #En caso de no pasar el tiempo por parametro, el mismo tendra un valor de medio segundo
    def Esperar(self, tiempo=0.5):
        time.sleep(tiempo)
    
    #5- Crear función para indicar el tiempo que se tardará en hacer el scroll
    def Scroll(self, horz, vert, tiempo=0.5): 
        #Usamos 'self' ya que lo tenemos inicializada en __Init__ y para que la palabra page de la función funcione es necesaria
        self.page.mouse.wheel(horz, vert)
        time.sleep(tiempo)
        
    #6- Nueva función para tomar captura de pantalla
    def tomar_captura(self, nombre_base, directorio):
        if not os.path.exists(directorio):
            os.makedirs(directorio) # Crea el directorio si no existe
        nombre_archivo = self._generar_nombre_archivo_con_timestamp(nombre_base)
        ruta_completa = os.path.join(directorio, f"{nombre_archivo}.jpg")
        self.page.screenshot(path=ruta_completa)
        print(f"Captura guardada en: {ruta_completa}") # Para ver dónde se guardó
        self.Esperar()
        
    #7- Crear nueva función para campo con capture la imagen
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
    def Click(self, selector, nombre, tiempo=0.5):
        s=self.page.locator(selector)
        s.highlight()
        expect(s).to_be_visible()
        expect(s).to_be_enabled()
        expect(s).to_contain_text(nombre)
        s.click()
        time.sleep(tiempo)
        
    #9- Crear nueva función para hacer click con captura de imagen
    def Click_Img(self, selector, nombre_base, directorio, tiempo=0.5):
        s=self.page.locator(selector)
        expect(s).to_be_visible()
        s.highlight()
        expect(s).to_be_enabled()
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
        
    #12- Crear nueva función para mensajes
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
        
    #15- Crear nueva función para mensaje no visible
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
    
    #22- Crear nueva función para validar que un tipo elemento es visible
    def Elemento_Visible(self, selector, nombre_base, directorio, tiempo= 0.5):
        ev= self.page.locator(selector)
        expect(ev).to_be_visible()
        ev.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #23- Crear función para marcar chek
    def Marcar_Check(self, selector, nombre_base, directorio, tiempo= 0.5):
        mc= self.page.locator(selector)
        expect(mc).to_be_visible()
        mc.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(mc).to_be_check()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #24- Crear función para desmarcar chek
    def Desmarcar_Check(self, selector, nombre_base, directorio, tiempo= 0.5):
        dc= self.page.locator(selector)
        expect(dc).to_be_visible()
        dc.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(dc).not_to_be_checked()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
    
    #25- Crear función para verificar que un elemento (o elementos) localizado en una página web contiene un texto específico.
    def Verificar_Texto_Contenido(self, selector, texto_esperado, nombre_base, directorio, tiempo= 0.5):
        vt= self.page.locator(selector)
        expect(vt).to_be_visible()
        vt.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(vt).to_contain_text(texto_esperado)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
    
    #26- Crear función para verificar que un elemento (o elementos) localizado en una lista de una página web contiene un texto específico.
    def Verificar_Lista_Texto_Contenido(self, selector, texto_esperado: list[str], nombre_base, directorio, tiempo= 0.5):
        vlt= self.page.locator(selector)
        try:
            #Verificar que el número de contenedores sea igual al número de textos esperados
            expect(vlt).to_have_count(len(texto_esperado), timeout=10000)
            print(f"INFO: Se encontraron {len(texto_esperado)} contenedores, como se esperaba.")
            
            #Iterar sobre cada contenedor y verificar que contenga el texto esperado
            for i, texto_esperado in enumerate(texto_esperado):
                # Accedemos a cada elemento individualmente usando .nth(i)
                contenedor_individual = vlt.nth(i)
                
                # Aseguramos que el contenedor individual sea visible
                expect(contenedor_individual).to_be_visible()
                contenedor_individual.highlight()

                # Aseguramos que el contenedor individual contenga el texto esperado
                # Usamos to_contain_text() si el texto puede estar mezclado con otras cosas
                # o to_have_text() si esperamos una coincidencia exacta del texto completo del elemento
                expect(contenedor_individual).to_contain_text(texto_esperado)
                print(f"INFO: Contenedor {i+1} contiene el texto esperado: '{texto_esperado}'.")
                
            self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
               
        except AssertionError as e:
            print(f"ERROR: Fallo al verificar la lista de contenedores o sus textos para el selector '{vlt}'.")
            cantidad_actual = vlt.count()
            self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
            raise AssertionError(
                f"Fallo en Verificar_Lista_Texto_Contenido: Problema con los elementos o textos esperados.\n"
                f"  - Error original: {e}\n"
                f"  - Selector usado: '{vlt}'\n"
                f"  - Cantidad de elementos encontrados: {cantidad_actual} (esperados: {len(texto_esperado)})"
            )
        time.sleep(tiempo)
        
    #27- Crear nueva función para comboBox multiple 
    def Verificar_Opciones_ComboBox(self, selector, valor: list[str], nombre_base, directorio, tiempo=0.5):
        voc= self.page.locator(selector)
        voc.highlight()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        expect(voc).to_be_visible()
        expect(voc).to_be_enabled()
        voc.select_option(valor)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        print(f"✔️ El select múltiple contiene los valores esperados: {valor}")
        time.sleep(tiempo)
        
    #28- Crear nueva función para verifica que un elemento objetivo (apuntado por un Locator) coincide con una instantánea de accesibilidad que le proporcionas.
    def Verificar_Aria_Snapshot(self, selector: str, expected_snapshot: str, nombre_base, directorio, tiempo=0.5):
        """
        Verifica que el elemento especificado coincide con la instantánea de accesibilidad dada.
        """
        vas = self.page.locator(selector)
        expect(vas).to_match_aria_snapshot(expected_snapshot)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #29- Crear nueva función para campo SIN capture la imagen
    def cTexto(self, selector, texto, tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        #La siguiente linea es para resaltar el campo en azul
        t.highlight()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.fill(texto)
        time.sleep(tiempo)
        
    #30- Crear nueva función para validar que un elemento es visible
    def Elemento_No_Visible(self, selector, nombre_base, directorio, tiempo= 0.5):
        env= self.page.locator(selector)
        expect(env).to_be_hidden()
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #31- Crear nueva funció para Verifica que el contenedores sean visibles y cuenta la cantidad de contenedores.
    def Contar_Y_Verificar_contenedores(self, selector, nombre_base, directorio, tiempo=0.5) -> int:
        cvc= self.page.locator(selector)
        
        # Espera a que el primer elemento del selector sea visible.
        expect(cvc.first).to_be_visible()
        
        # Un highlight específico para el primer elemento
        cvc.first.highlight()
        
        # Tomar una captura antes de contar
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        
        # Contar la cantidad de elementos que el selector ha encontrado
        cantidad_contenedores_actual = cvc.count()
        print(f"DEBUG: Se encontraron {cantidad_contenedores_actual} contenedores en la página.")
        
        # Opcional: Si se quieres un umbral mínimo, se puede añadir una aserción.
        # Por ejemplo, que la cantidad sea mayor que 0.
        assert cantidad_contenedores_actual > 0, \
            f"Error: Se esperaban contenedores, pero se encontraron {cantidad_contenedores_actual}."
        
        # Tomar una captura después de contar (opcional)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo) # Pausa al final si es necesario
        return cantidad_contenedores_actual
    
    #32- Crear nueva función que obtiene los nombres de los productos de la página y verifica que coincidan
    #con la lista de nombres esperada y en el orden esperado.
    def Verificar_Orden_Nombres_Productos(self, selector, nombres_esperados: list[str], nombre_base, directorio, tiempo=0.5):
        onp= self.page.locator(selector)
        
        print(f"\nDEBUG: Verificando elementos...")

        # Espera a que al menos el primer nombre de producto sea visible
        expect(onp.first).to_be_visible()

        # Toma una captura antes de obtener los textos
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura

        # Obtiene los textos de todos los elementos que coinciden con el Locator
        # to_all_text_contents() espera por los elementos y devuelve una lista de sus textos.
        nombres_actuales = onp.all_text_contents()

        print(f"DEBUG: Elementos encontrados: {nombres_actuales}")
        print(f"DEBUG: Elementos esperados: {nombres_esperados}")

        # Aserción principal: Verifica que los nombres actuales coincidan con los esperados
        # El orden es importante aquí.
        assert nombres_actuales == nombres_esperados, \
            f"Error: El orden de los productos no es el esperado.\n" \
            f"ESPERADOS: {nombres_esperados}\n" \
            f"ACTUALES:   {nombres_actuales}"

        print(f"VERIFICACIÓN EXITOSA: El orden de los elementos es el esperado.")

        # Toma una captura después de la verificación
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        
        time.sleep(tiempo)
    
    #33- Crear nueva función que obtiene los precios de los elementos de la página y verifica que coincidan
    #con la lista de precios esperada y en el orden esperado.
    def Verificar_Orden_Precios_Productos(self, selector, nombre_base, directorio, tiempo=0.5):
        opp= self.page.locator(selector)
        
        print(f"DEBUG: Verificando elementos...")

        # Espera a que al menos el primer nombre de producto sea visible
        expect(opp.first).to_be_visible()

        # Toma una captura antes de obtener los textos
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura

        # Obtiene los textos de todos los elementos que coinciden con el Locator
        # to_all_text_contents() espera por los elementos y devuelve una lista de sus textos.
        precios_textos = opp.all_text_contents()

        #Convierte los textos de los precios a números flotantes
        # Elimina el signo '$' y convierte a float
        precios_actuales_numerico = [float(precio.replace('$', '')) for precio in precios_textos]
        print(f"DEBUG: Precios de elementos (numérico): {precios_actuales_numerico}")
        
        # Crea una lista de precios esperados ordenados.
        # En Sauce Labs, los precios son fijos, así que podemos definirlos o tomarlos y ordenarlos.
        # Para hacer el test más robusto y no saber de antemano los valores,
        # la mejor verificación es que la lista numérica esté ORDENADA.
        precios_ordenados_correctamente = sorted(precios_actuales_numerico)

        # Aserción principal: Verifica que la lista actual ya esté ordenada como esperamos
        assert precios_actuales_numerico == precios_ordenados_correctamente, \
            f"Error: El orden de los precios no es el esperado.\n" \
            f"ESPERADO: {precios_ordenados_correctamente}\n" \
            f"ACTUAL:   {precios_actuales_numerico}"

        print(f"VERIFICACIÓN EXITOSA: El orden de los precios es el esperado (menor a más alto).")

        # Toma una captura despues de obtener los textos
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        
        time.sleep(tiempo)

    #34- Crear nueva función que obtiene los precios de los elementos de la página y verifica que coincidan
    #con la lista de precios esperada y en el orden inversa esperado.
    def Verificar_Orden_Precios_Inverso_Productos(self, selector, nombre_base, directorio, tiempo=0.5):
        opip= self.page.locator(selector)
        
        print(f"DEBUG: Verificando productos...")
        
        # Obtiene los textos de todos los elementos de precio
        precios_textos = opip.all_text_contents()
        # Convierte los textos de los precios a números flotantes
        precios_actuales_numerico = [float(precio.replace('$', '')) for precio in precios_textos]

        # Crea una lista de precios esperados ordenados.
        # ¡LA CLAVE ESTÁ EN ORDENAR DE FORMA DESCENDENTE!
        precios_ordenados_correctamente = sorted(precios_actuales_numerico, reverse=True) # <-- ¡Este es el cambio conceptual!
        
        # Aserción principal: Verifica que la lista actual ya esté ordenada como esperamos
        assert precios_actuales_numerico == precios_ordenados_correctamente, \
            f"Error: El orden de los precios no es el esperado.\n" \
            f"ESPERADO: {precios_ordenados_correctamente}\n" \
            f"ACTUAL:   {precios_actuales_numerico}"

        print(f"VERIFICACIÓN EXITOSA: El orden de los precios es el esperado (mayor a menor).")
        # Toma una captura despues de obtener los textos
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)

    #35 Crear nueva función para verificar precio individual de elemento
    def Precio_Individual_Elemento(self, selector, valor, precio, nombre_base, directorio, tiempo=0.5):
        pie= self.page.locator(selector)
        # Espera a que al precio del elemento sea visible
        expect(pie).to_be_visible()
        #La siguiente linea es para resaltar el campo en azul
        pie.highlight()
        
        assert valor == precio, \
            f"Precio esperado es '{valor}', pero se visualiza '{precio}'"
            
        # Toma una captura despues de obtener los textos
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo)
        
    #36- Crear nueva funció para Verifica que el contenedor NO sean visibles y cuenta la cantidad de contenedores.
    def Contar_Y_Verificar_no_contenedores(self, selector, nombre_base, directorio, tiempo=0.5) -> int:
        cvnc= self.page.locator(selector)
        
        # Tomar una captura antes de contar
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        
        #Verificanos que el contenedor no sea visible
        expect(cvnc).to_be_hidden()
        
        #Se cuenta la cantidad de contenedores
        cantidad_contenedores_actual = cvnc.count()
        
        #Si la aserción falla, significa que se encontraron elementos cuando no debían.
        assert cantidad_contenedores_actual == 0, \
            f"Error: No se esperaban contenedores, pero se encontraron {cantidad_contenedores_actual}."
        
        print(f"DEBUG: Se encontraron {cantidad_contenedores_actual} contenedores en la página.")
        # Tomar una captura después de contar (opcional)
        self.tomar_captura(nombre_base=nombre_base, directorio=directorio) # Llama a la función de captura
        time.sleep(tiempo) # Pausa al final si es necesario
        return cantidad_contenedores_actual