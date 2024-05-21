from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# URL del formulario de Google
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdkqk3vrwcjMjUr23kIS93pzzw0cs-RFnxUJT8sd82dkxLwlQ/viewform"

# Nombres ficticios y sus respuestas
names = [
    "Juan Pérez", "María López", "Carlos García", "Ana Martínez",
    "Luis Hernández", "Sofía González", "Miguel Rodríguez", "Elena Fernández",
    "Jorge Sánchez", "Lucía Díaz"
]

# Respuestas ficticias para el formulario
answers_list = [
    {"Edad": "Menos de 20 años", "Sexo": "Masculino", "Estado Civil": "Soltero/a", "Antigüedad": "Menos de 1 año", "Ocupación": "Administrativo/a", "Nivel Académico": "Universitario/a", "Ingreso Salarial": "Entre RD$ 10,001 - 20,000", "Pregunta 1": "Nunca", "Pregunta 2": "Nunca", "Pregunta 3": "No", "Pregunta 4": "No", "Pregunta 5": "No", "Pregunta 6": "No", "Pregunta 10": "No", "Pregunta 11": "No", "Pregunta 12": "No", "Pregunta 13": "No", "Pregunta 14": "No", "Pregunta 15": "No", "Pregunta 16": "a"},
    {"Edad": "20-30 años", "Sexo": "Femenino", "Estado Civil": "Casado/a", "Antigüedad": "Entre 1-2", "Ocupación": "Gerente", "Nivel Académico": "Técnico/a", "Ingreso Salarial": "Más de 40,000", "Pregunta 1": "Algunas veces, pero menos de la mitad", "Pregunta 2": "Sí, pero menos de la mitad de las veces que he perdido", "Pregunta 3": "Ahora no, pero en el pasado sí", "Pregunta 4": "Si", "Pregunta 5": "Si", "Pregunta 6": "Si", "Pregunta 10": "Si", "Pregunta 11": "Si", "Pregunta 12": "Si", "Pregunta 13": "Si", "Pregunta 14": "Si", "Pregunta 15": "Si", "Pregunta 16": "b"},
    # Añadir más respuestas ficticias según sea necesario
]

# Configurar Selenium con WebDriverManager
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Función para enviar respuestas al formulario
def submit_form(name, answers):
    driver.get(form_url)
    
    # Esperar a que la página cargue completamente
    wait = WebDriverWait(driver, 30)
    
    # Completar las preguntas del formulario
    def find_and_click(xpath):
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        driver.find_element(By.XPATH, xpath).click()
    
    # Edad
    find_and_click(f'//div[@data-value="{answers["Edad"]}"]')

    # Sexo
    find_and_click(f'//div[@data-value="{answers["Sexo"]}"]')

    # Estado Civil
    find_and_click(f'//div[@data-value="{answers["Estado Civil"]}"]')

    # Antigüedad
    find_and_click(f'//div[@data-value="{answers["Antigüedad"]}"]')

    # Ocupación
    find_and_click(f'//div[@data-value="{answers["Ocupación"]}"]')

    # Nivel Académico
    find_and_click(f'//div[@data-value="{answers["Nivel Académico"]}"]')

    # Ingreso Salarial
    find_and_click(f'//div[@data-value="{answers["Ingreso Salarial"]}"]')

    # Preguntas específicas
    find_and_click(f'//div[@data-value="{answers["Pregunta 1"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 2"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 3"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 4"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 5"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 6"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 10"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 11"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 12"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 13"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 14"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 15"]}"]')
    find_and_click(f'//div[@data-value="{answers["Pregunta 16"]}"]')

    # Enviar el formulario
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]/..')))
    submit_button.click()

    # Esperar a que se procese la respuesta
    time.sleep(2)

# Enviar respuestas para cada nombre en la lista
for name, answers in zip(names, answers_list):
    submit_form(name, answers)
    print(f"Formulario enviado para: {name}")

# Cerrar el navegador
driver.quit()
