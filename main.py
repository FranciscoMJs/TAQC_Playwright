from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.logout_page import LogOut
from utils.config import URL_ECOMMERCE
import asyncio


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        login_page = LoginPage(page)
        await login_page.open_url(URL_ECOMMERCE)
        await login_page.login()
        
        home_page = HomePage(page)
        await home_page.find_product()
        
        product_page = ProductPage(page)
        await product_page.add_to_cart()
        await product_page.verificar_cart()
        
        logout_page = LogOut(page)
        await logout_page.Logout()
        
        browser.close

if __name__ == "__main__":
    asyncio.run(main())
    print("✅ Prueba completada correctamente.")