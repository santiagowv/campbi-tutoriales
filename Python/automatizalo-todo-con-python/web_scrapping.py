""" Requests
    Enviar solicitudes HTTP para interactuar con web services y traer datos de páginas web.
    Ideal para acceder a APIs, decargar contenido o intectuar con websites.
"""
import requests
url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Fallo al acceder a la página. Código de estado:", response.status_code)



""" Selenium
    Auomatizar navegadores web simulando interacciones usuarios reales (clicking, scrolling, llenar formularios).
    Útil para automatizar tareas repetitivas, hacer testeo y acceder a contenido de páginas.

    Otras opciones son:
        - Playwright para automatización de páginas modernas.
        - Pyppeteer: Automatizar especialmente cuando el renderizado de código de Javascript es critico.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome to run in headless mode
options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://example.com")
    # Esperar que el h1 en el sitio web cargue
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    print("Page Heading:", element.text)
except Exception as e:
    print("Error during Selenium execution:", e)
finally:
    driver.quit()



""" Scrappy
    Obtencion y almacenamiento de los datos extraidos de paginas web.
    Proyectos de extracción de datos mas estructurados y escalables.
"""
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["http://example.com"]

    def parse(self, response):
        yield {
            "title": response.css("title::text").get()
        }