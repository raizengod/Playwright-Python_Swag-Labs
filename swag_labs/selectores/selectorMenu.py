from playwright.sync_api import Page

class MenuPageLocators:
    def __init__(self, page: Page):
        self.page = page
        # Solo la cadena del selector
        # Convención: usar guion bajo si es un atributo privado
        self._selectorBtnMenu= "//*[@id='react-burger-menu-btn']"
        self._selectorArticulos= "//*[@id='inventory_sidebar_link']"
        self._selectorSobre= "//*[@id='about_sidebar_link']"
        self._selectorSalir= "//*[@id='logout_sidebar_link']"
        self._SelectorRestaurar= "//*[@id='reset_sidebar_link']"
        self._selectorCerrarMenu= "//*[@id='react-burger-cross-btn']"
    
    #Selector de menú hamburguesa
    def selectorMenu(self):
        return self._selectorBtnMenu
    
    #Selector opción items
    def selectorItems(self):
        return self._selectorArticulos
    
    #Selector opción About
    def selectorAbout(self):
        return self._selectorSobre
    
    #Selector opción Logout
    def selectorLoguot(self):
        return self._selectorSalir
    
    #Selector de restaurar contador carrito de compra
    def selectorRestaurarContador(self):
        return self._SelectorRestaurar
    
    #Selector para cerrar menú
    def selectorCerrar(self):
        return self._selectorCerrarMenu