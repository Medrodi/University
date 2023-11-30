import os
from converter import *
import PIL
def change_dir():
    os.chdir(input(r"Укажите корректный путь к рабочему каталогу: "))

def find_files(path: str, *expansions: str):
    correct_files = []
    for exp in expansions:
        dir_now = os.getcwd()
        file_list = os.listdir(os.getcwd())
        for file in file_list:
            if file[-(len(exp)):] == exp:
                correct_files.append(file)
    return correct_files

def find_pdf(path: str):
    pdf_list = find_files(path, ".pdf")
    print("Список файлов с расширением  .pdf")
    for i in range(len(pdf_list)):
        print(f"{i + 1}. {pdf_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(pdf_list) + 1:
        pdf_2_docx(os.path.join(pdf_list[int(choice) - 1]))
    if choice == '0':
        for i in range(len(pdf_list)):
            pdf_2_docx(os.path.join(pdf_list[i]))

def find_docx(path:str):
    docx_list = find_files(path, ".docx")
    print("Список файлов с расширением  .docx")
    for i in range(len(docx_list)):
        print(f"{i + 1}. {docx_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(docx_list) + 1:
        docx_2_pdf(os.path.join(docx_list[int(choice) - 1]))
    if choice == '0':
        for i in range(len(docx_list)):
            docx_2_pdf(os.path.join(docx_list[i]))

def find_pic(path: str):
    pic_list = find_files(path, ".jpeg", ".gif", ".png", ".jpg")
    print("Список файлов с расширением  .jpeg  .gif  .png  .jpg")
    for i in range(len(pic_list)):
        print(f"{i + 1}. {pic_list[i]}")
    choice = input(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного "
                   "каталога введите 0): ")
    if int(choice) <= len(pic_list) + 1:
        compress_pic(os.path.join(pic_list[int(choice) - 1]))
        print("Операция успешно ")
    if choice == '0':
        for i in range(len(pic_list)):
            compress_pic(os.path.join(pic_list[i]))
