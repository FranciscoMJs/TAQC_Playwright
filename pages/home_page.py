from pages.base_page import BasePage
from utils.config import PRODUCT_NAME

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    async def find_product(self):
        product_locator = "#item_4_title_link > div:nth-child(1)"
        try:
            # Esperar a que el producto aparezca en la página
            await self.page.wait_for_selector(product_locator, timeout=5000)
            
            # Hacer clic en el producto
            await self.page.click(product_locator)
            print("✅ Producto encontrado y clickeado.")
        except:
            print("❌ No se encontró el producto. Verifica el selector o el tiempo de carga de la página.")