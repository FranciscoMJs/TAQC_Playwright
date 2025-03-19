from playwright.sync_api import Page

class BasePage:
    def __init__(self, page : Page):
        self.page = page

    async def open_url(self, url : str):
        """Abre una URL en el navegador."""
        await self.page.goto(url)
    
    async def wait(self, time:int = 5000):
        """Espera un tiempo en milisegundos."""
        await self.page.wait_for_timeout(time)