from playwright.sync_api import Page

class DetallePageLocators:
    def __init__(self, page: Page):
        self.page = page
        # Solo la cadena del selector
        # Convención: usar guion bajo si es un atributo privado
        self._selectorBackDetelle= "//*[@id='back-to-products']"
        self._selectorNombreDetalleProd= "//*[@id='inventory_item_container']/div/div/div[2]/div[1]"
        self._selectorImgDetalleProd= "//*[@id='inventory_item_container']/div/div/div[1]/img"
        self._selectorDescDetalleProd= "//*[@id='inventory_item_container']/div/div/div[2]/div[2]"
        self._selectorPrecDetalleProd= "//*[@id='inventory_item_container']/div/div/div[2]/div[3]"
        self._selectorAddDetelleProd= "//*[@id='add-to-cart']"
        self._selectorRemoveDetalleProducto= "//*[@id='remove']"
    
    #Selector de back producto
    def selectorBack(self):
        return self._selectorBackDetelle
    
    #Selector de nombre producto
    def selectorNombreDetalle(self):
        return self._selectorNombreDetalleProd
    
    #Selector de imagen producto
    def selectorImgDetalle(self):
        return self._selectorImgDetalleProd
    
    #Selector de descripción de producto
    def selectorDescProducto(self):
        return self._selectorDescDetalleProd
    
    #Selector de precio de producto
    def selectorPrecProd(self):
        return self._selectorPrecDetalleProd
    
    #Selector de agregar producto a carrito
    def selectorAgregar(self):
        return self._selectorAddDetelleProd
    
    #Selector de remover producto a carrito
    def selectorRemover(self):
        return self._selectorRemoveDetalleProducto
    
    def obtenerValor(self):
        return self.page.inner_text(self._selectorPrecDetalleProd)