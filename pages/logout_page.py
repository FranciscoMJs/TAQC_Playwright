from pages.base_page import BasePage

class LogOut(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    async def Logout(self):
        await self.page.click("#react-burger-menu-btn")
        await self.page.click("#logout_sidebar_link")
        print("✅ LogOut Completado")