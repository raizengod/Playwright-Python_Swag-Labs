from playwright.sync_api import Page

class HomePageLocators:
    def __init__(self, page: Page):
        self.page = page
        # Solo la cadena del selector
        # Convención: usar guion bajo si es un atributo privado
        self._selectorGridProductos = "//*[@id='inventory_container']/div"
        self._selectorTitulo= "//*[@id='header_container']/div[1]/div[2]/div"
        self._selectorCarrito= "//*[@id='shopping_cart_container']/a"
        self._selectorComboFiltro= "//*[@id='header_container']/div[2]/div/span/select"
        self._selectorCopyRight= "//*[@id='page_wrapper']/footer/div"
        self._selectorTituloBackPack= "//*[@id='item_4_title_link']/div"
        self._selectorDescripcionBackPack= "//*[@id='inventory_container']/div/div[1]/div[2]/div[1]/div"
        self._selectorPrecioBackPack= "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
        self._selectorAgregarBackPack= "//*[@id='add-to-cart-sauce-labs-backpack']"
        self._selectorRemoverBackPack= "//*[@id='remove-sauce-labs-backpack']"
        self._selectorAgregarLuz= "//*[@id='add-to-cart-sauce-labs-bike-light']"
        self._selectorRemoverLuz= "//*[@id='remove-sauce-labs-bike-light']"
        self._selectorAgregarCamisa= "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
        self._selectorRemoverCamisa= "//*[@id='remove-sauce-labs-bolt-t-shirt']"
        self._selectorContadorCarrito= "//*[@id='shopping_cart_container']/a/span"
        self._selectorProductosVisibles= "#inventory_container .inventory_item"
        self._selectorNombreProductos= ".inventory_item_name"
        self._selectorPrecioProductos= ".inventory_item_price"
        self._selectorImgProducto= "//*[@id='item_4_img_link']/img"        
        
    #Selector titulo de la pantalla home   
    def selectorTituloHome(self):
        return self._selectorTitulo  #Retorna la cadena
    
    #Selector de Grid de productos
    def selectorGrid(self):
        return self._selectorGridProductos

    #Selector del carrito de compra
    def selectorCarritoCompra(self):
        return self._selectorCarrito
    
    #Selector del combobox de filtros
    def selectorFiltro(self):
        return self._selectorComboFiltro
    
    #Selector del texto copy right en el footer
    def selectorFooter(self):
        return self._selectorCopyRight
    
    #Selector de nombre del producto Back Pack
    def selectorNombreBolso(self):
        return self._selectorTituloBackPack
    
    #Selector del resumen de la descripción del producto backpack
    def selectorDetalleBolso(self):
        return self._selectorDescripcionBackPack
    
    #Selector del precio del producto backpack
    def selectorPrecioBolso(self):
        return self._selectorPrecioBackPack
    
    #Selector del botón agregar al carrito del producto back pack
    def selectorAgregarBolso(self):
        return self._selectorAgregarBackPack
    
    #Selector del botón remover al carrito del producto back pack
    def selectorRemoverBolso(self):
        return self._selectorRemoverBackPack
    
    #Selector del botón agregar al carrito del producto back pack
    def selectorAgregarBrillo(self):
        return self._selectorAgregarLuz
    
    #Selector del botón agregar al carrito del producto back pack
    def selectorRemoverBrillo(self):
        return self._selectorRemoverLuz
    
    #Selector del botón agregar al carrito del producto back pack
    def selectorAgregarTshirt(self):
        return self._selectorAgregarCamisa
    
    #Selector del botón agregar al carrito del producto back pack
    def selectorRemoverTshirt(self):
        return self._selectorRemoverCamisa
    
    #Selector del contador de productos en el carrito
    def selectorContador(self):
        return self._selectorContadorCarrito
    
    #Selector de contenedor de prodyucto
    def selectorContenedorProducto(self):
        return self._selectorProductosVisibles

    #Selector nombre productos
    def selectorNombres(self):
        return self._selectorNombreProductos
    
    #Selector precios productos
    def selectorPrecios(self):
        return self._selectorPrecioProductos
    
    #Selector imagen producto
    def selectorImg(self):
        return self._selectorImgProducto
    
    