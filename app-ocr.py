from PIL import Image # Importando o módulo Pillow para abrir a imagem no script
import pytesseract # Módulo para a utilização da tecnologia OCR

tessdata_dir_config = r'--tessdata-dir "C:/Tesseract-OCR/tessdata/"'

print( pytesseract.image_to_string( Image.open('img/home.jpg'), config=tessdata_dir_config) ) # Extraindo o texto da imagem

