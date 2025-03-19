from playwright.sync_api import Page

class BasePage:
    def __init__(self, page : Page):
        self.page = page

    async def open_url(self, url : str):
        """Abre una URL en el navegador."""
        await self.page.goto(url)