from pages.base_page import BasePage
from utils.config  import USERNAME, PASSWORD

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    async def login(self):
        await self.page.fill('#user-name', USERNAME)
        await self.page.fill('#password', PASSWORD)
        await self.page.click('#login-button')
        print('✅ Inicio de Sesion exitoso')
    