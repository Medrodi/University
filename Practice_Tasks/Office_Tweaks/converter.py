from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image


def pdf_2_docx(path: str):
    """
    Функция принимает путь к фалу, который мы хотим конвертировать в формате str, потом конвертирует
    его из формата pdf в docx
    :param path: путь к файлу
    :return: None
    """
    pdf_file = path # переменной присваювается путь к конвертируемому файлу pdf
    docx_file = path[:-3] + 'docx' # переменной присваивается путь к файлу, куда будет записан текст
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

def docx_2_pdf(path: str):
    """
    Функция принимает путь к фалу, который мы хотим конвертировать в формате str
    :param path: путь к файлу
    :return: None
    """
    convert(path)

def compress_pic(path: str):
    image_file = Image.open(path)
    resolution = int(input("Введите параметры сжатия(от 0 до 100%): "))
    image_file.save(f"{input("Введите название сжатого файла: ")}.jpg", quality=resolution)

# compress_pic(r"C:\files\slide-17-1.jpg")