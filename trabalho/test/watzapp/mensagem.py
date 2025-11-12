
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    """Configura e retorna o WebDriver do Chrome."""
    options = webdriver.ChromeOptions()
    # Manter o navegador aberto após a execução do script
    options.add_experimental_option("detach", True)
    # Adicionar um perfil de usuário para manter o login do WhatsApp Web
    # Certifique-se de que o caminho para o perfil exista e seja gravável
    # Ex: /home/ubuntu/.config/google-chrome/Default
    # Você pode precisar ajustar este caminho para o seu sistema
    options.add_argument("--user-data-dir=/home/ubuntu/.config/google-chrome/")
    options.add_argument("--profile-directory=Default")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def send_whatsapp_message(driver, contact_name, message):
    """Envia uma mensagem para um contato específico no WhatsApp Web."""
    try:
        # Navegar para o WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Esperar até que o WhatsApp Web esteja carregado (elemento de pesquisa visível)
        # O usuário precisará escanear o QR code manualmente na primeira vez
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        print("WhatsApp Web carregado. Procurando contato...")

        # Procurar pelo contato
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2) # Pequena pausa para os resultados da pesquisa aparecerem

        # Clicar no contato encontrado
        # Pode ser necessário ajustar o XPath dependendo da versão do WhatsApp Web
        contact_xpath = f'//span[@title="{contact_name}"]'
        contact = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, contact_xpath))
        )
        contact.click()
        print(f"Contato '{contact_name}' selecionado.")

        # Digitar a mensagem
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        message_box.send_keys(message)
        print("Mensagem digitada.")

        # Clicar no botão de enviar
        send_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Enviar"]'))
        )
        send_button.click()
        print("Mensagem enviada!")
        time.sleep(2) # Pequena pausa após o envio

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    driver = setup_driver()

    # Exemplo de uso:
    # Substitua 'Nome do Contato' pelo nome exato do contato ou grupo no seu WhatsApp
    # Substitua 'Sua Mensagem Aqui' pela mensagem que deseja enviar
    contacts_to_message = [
        {"name": "Nome do Contato 1", "messages": ["Olá, esta é a mensagem 1.", "Esta é a mensagem 2."]},
        {"name": "Nome do Contato 2", "messages": ["Oi, tudo bem?", "Tenho uma novidade!"]}
    ]

    for contact_info in contacts_to_message:
        contact_name = contact_info["name"]
        for message in contact_info["messages"]:
            send_whatsapp_message(driver, contact_name, message)
            time.sleep(5) # Espera 5 segundos entre as mensagens para evitar bloqueio

    print("Todas as mensagens foram processadas.")
    # O navegador permanecerá aberto devido à opção 'detach=True'
    # driver.quit() # Descomente para fechar o navegador automaticamente no final
