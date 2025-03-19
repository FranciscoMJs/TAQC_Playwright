from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    async def add_to_cart(self):
        await self.page.click("#add-to-cart")
        print("✅ Producto Añadido")
    
    async def verificar_cart(self):
        await self.page.click(".shopping_cart_link")
        print("✅ Producto Verificado")