from playwright.sync_api import Page

class LoginPageLocators:
    def __init__(self, page: Page):
        self.page = page
        # Solo la cadena del selector
        # Convención: usar guion bajo si es un atributo privado
        self._selectorTituloLogin = "//*[@id='root']/div/div[1]" 
        self._selectorUser= "//*[@id='user-name']"
        self._selectorContrasena= "//*[@id='password']"
        self._selectorBtnIngresar= "//*[@id='login-button']"
        self._selectorMarcError1= "//*[@id='login_button_container']/div/form/div[1]/svg/path"
        self._selectorMarcError2= "//*[@id='login_button_container']/div/form/div[2]/svg"
        self._selectorMsjErrores= "//*[@id='login_button_container']/div/form/div[3]/h3"
        self._selectorCerrarErrores= "//*[@id='login_button_container']/div/form/div[3]/h3/button"
        

    #Selector titulo de la pantalla login   
    def selectorTituloLogin(self):
        return self._selectorTituloLogin  #Retorna la cadena

    #Selector del campo username
    def selectorUsuario(self):
        return self._selectorUser
    
    #Selector del campo contraseña
    def selectorClave(self):
        return self._selectorContrasena

    #Selector del botón de ingresar login
    def selectorBtnLogin(self):
        return self._selectorBtnIngresar
    
    #Selector marca de error en el campo username
    def selectorMarcCampError1(self):
        return self._selectorMarcError1
    
    #Selector marca de error en el campo contraseña
    def selectorMarcCampError2(self):
        return self._selectorMarcError2
    
    #Selector de contenedor de mensaje de error
    def selectorMsjError(self):
        return self._selectorMsjErrores
    
    #Selector para cerrar mensaje de error
    def selectorCerrarError(self):
        return self._selectorCerrarErrores