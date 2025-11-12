import pyautogui
import pytesseract
from PIL import Image

# --- 1. Captura uma parte da tela (ajuste a região conforme sua tela) ---
imagem_area = pyautogui.screenshot(region=(10, 10, 300, 400))
imagem_area.save('area_especifica.png')

# --- 2. Usa OCR para ler o texto ---
texto = pytesseract.image_to_string(imagem_area, lang='por')  # 'por' = português

# --- 3. Exibe o que foi reconhecido ---
print("🖼️ Texto reconhecido na imagem:")
print(texto)
