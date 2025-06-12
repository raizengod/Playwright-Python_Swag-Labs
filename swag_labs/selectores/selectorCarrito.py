from playwright.sync_api import Page

class CarritoPageLocators:
    def __init__(self, page: Page):
        self.page = page
        # Solo la cadena del selector
        # Convención: usar guion bajo si es un atributo privado
        self._selectorContenedorProd= "#cart_contents_container > div > div.cart_list > div.cart_item"
        self._selectorLabelCarrito= "//*[@id='header_container']/div[2]"
        self._selectorLabelCantidad= "//*[@id='cart_contents_container']/div/div[1]/div[1]"
        self._selectorLabelDescripcion= "//*[@id='cart_contents_container']/div/div[1]/div[2]"
        self._selectorRemoverCarrito= "//*[@id='remove-sauce-labs-backpack']"
        self._selectorBtnChekout= "//*[@id='checkout']"
        self._selectorDescripcion= ".inventory_item_desc"
        self._selectorCuantificador= ".cart_quantity"
        self._selectorNombreArt= ".inventory_item_name"
        self._selectorPrecio= ".inventory_item_price"        
        self._selectorTienda= "//*[@id='continue-shopping']"
        self._selectorLabelInformacion= "//*[@id='header_container']/div[2]/span"
        self._selectorNombre= "//*[@id='first-name']"
        self._selectorApellido= "//*[@id='last-name']"
        self._selectorZip= "//*[@id='postal-code']"
        self._selectorBtnContinuar= "//*[@id='continue']"
        self._selectorMsjError= "//*[@id='checkout_info_container']/div/form/div[1]/div[4]"
        self._selectorCerrarMsj= "#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error > h3 > button"
        self._selectorLabelPreview= "//*[@id='header_container']/div[2]/span"
        self._selectorContenedorPreview= ".cart_item"
        self._selectorCantidadPreview= ".cart_quantity"
        self._selectorDescripcionPreview= ".inventory_item_desc"
        self._selectorPrecioPreview= '.inventory_item_price'
        self._selectorBtnFinalizar= "//*[@id='finish']"
        self._selectorBtnCancelar= "//*[@id='cancel']"
        self._selectorInfoSumario= ".summary_info"
        self._selectorLabelCompleto= "//*[@id='header_container']/div[2]"
        self._selectorLogoCompleto= "//*[@id='checkout_complete_container']/img"
        self._selectorLabelGracias= "//*[@id='checkout_complete_container']/h2"
        self._selectorLabelDespacho= "//*[@id='checkout_complete_container']/div"
        self._selectorBtnHome= "//*[@id='back-to-products']"
        
    #Selector contenedor de productos del carrito
    def selectorContenedor(self):
        return self._selectorContenedorProd
    
    #Selector de label de titulo de la pantalla
    def selectorTituloCarrito(self):
        return self._selectorLabelCarrito
    
    #Selector de label de columna de cantidad
    def selectorColumCantidad(self):
        return self._selectorLabelCantidad
    
    #Selector de label de columna de descripción
    def selectorColumDescripcion(self):
        return self._selectorLabelDescripcion
    
    #Selector de ir a tienda
    def selectorComprar(self):
        return self._selectorTienda
    
    #Selector para remover producto
    def selectorRemoverProd(self):
        return self._selectorRemoverCarrito
    
    #Selector de botón para iniciar flujo de compra
    def selectorInicarCheckout(self):
        return self._selectorBtnChekout
    
    #Selector de label de flujo de infación
    def selectorInfoPersonal(self):
        return self._selectorLabelInformacion
    
    #Selector campos nombre infomación
    def selectorTxtNombre(self):
        return self._selectorNombre
    
    #Selector campo apellido información
    def selectorTxtApellido(self):
        return self._selectorApellido
    
    #Selector campo código postal información
    def selectorTxtCodigoPostal(self):
        return self._selectorZip
    
    #Selector botón continuar fluo de compra
    def selectorContinuar(self):
        return self._selectorBtnContinuar
    
    #Selector de mensaje de error
    def selectorError(self):
        return self._selectorMsjError
    
    #Selector botón cerrra mensaje de error
    def selectorCerrar(self):
        return self._selectorCerrarMsj
    
    #Selector de label titulo preview
    def selectorPreview(self):
        return self._selectorLabelPreview
    
    #Selector contenedores de productos en el preview
    def selectorProdPreview(self):
        return self._selectorContenedorPreview
    
    #Selector cuantificador producto ppreview
    def selectorCuantPreview(self):
        return self._selectorCantidadPreview
    
    #Selector descripción producto preview
    def selectorDescPreview(self):
        return self._selectorDescripcionPreview
    
    #Selector precio producto preview
    def selectorPrecPreview(self):
        return self._selectorPrecioPreview
    
    #Selector para finalizar proceso de compra
    def selectorFinalizarCompra(self):
        return self._selectorBtnFinalizar
    
    #Selector cancelar flujo de compra
    def selectorCancelarCompra(self):
        return self._selectorBtnCancelar
    
    #Selector de contenedor información orden de compra
    def selectorSumario(self):
        return self._selectorInfoSumario
    
    #Selector de label compra completa
    def selectorCompleta(self):
        return self._selectorLabelCompleto
    
    #Selector de logo transacción completa
    def selectorLogo(self):
        return self._selectorLogoCompleto
    
    #Selector label agradecimiento por comprar
    def selectorAgradecimiento(self):
        return self._selectorLabelGracias
    
    #Selector label informativo de despacho
    def selectorDespacho(self):
        return self._selectorLabelDespacho
    
    #Selector botón ir a pantalla home
    def selectorHome(self):
        return self._selectorBtnHome
    
    #selector label Nombre
    def selectorNombreProd(self):
        return self._selectorNombreArt
    
    #Selector label contador de unidad de producto individual
    def selectorContIndividualProd(self):
        return self._selectorCuantificador
    
    #Selector descripción de producto
    def selectorDescProd(self):
        return self._selectorDescripcion
    
    #Selector precio producto
    def selectorPrecProd(self):
        return self._selectorPrecio
    
    def obtenerValor(self):
        return self.page.inner_text(self._selectorPrecio)