from directories import *
from delete_files import *
from converter import *


import PySimpleGUI as sg
import os

def create_img_cmprs_window():

    layout_img = [
        [sg.Text("Процент сжатия от 1 до 95%"), sg.InputText(key="-RES-", size=(20, 1))],
        [sg.Text("Имя нового файла          "), sg.InputText(key="-NAME-", size=(20, 1))],
        [sg.Button("OK"), sg.Button("Exit")]

    ]
    return sg.Window("Сжатие картинки", layout_img, finalize=True)

def create_main_window():
    sg.theme("DarkGrey15")
    file_list_column = [
        [
            sg.Text("Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]
    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Выберите действие,\nпри нажатии оно производится автоматически:", text_color="lightskyblue")],
        [sg.Listbox(values= [], size=(40, 5), key="-TOUT-", enable_events=True, horizontal_scroll=True)],
        [sg.Text("", key="-END-", background_color='Darkblue', size=(36, 1))],
        [sg.Button("Работа с несколькими файлами", button_color='blue', key="-MANY FILES-"),
         sg.Button("Обновить",button_color='blue', key="-RELOAD-") ]
    ]

    view_files_column = [
        [sg.Text("Выбранные файлы:", text_color='lightskyblue')],
        [sg.Listbox(values=[], size=(40, 20), key="-VIEW FILES-", enable_events=True)]

    ]

    # ----- Full layout -----
    layout_main = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
            sg.VSeperator(),
            sg.Column(view_files_column)
        ]
    ]
    return sg.Window("Главное окно", layout_main, finalize=True, resizable=True)

def create_choice_files():
    layout = [[sg.Text('Выберите файлы:'), sg.Input(key="-CHOSEN FILES-"), sg.FilesBrowse()],
              [sg.Button('Открыть', key="-CHOICE-"), sg.Button('Отмена')]]

    return  sg.Window('Диалог выбора файлов', layout, finalize=True)

window_main, window_cmprs = create_main_window(), None


commands_docx = ["Преобразовать в pdf файл", "Удалить файл"]
commands_pdf = ["Преобразовать в docx файл", "Удалить файл"]
commands_img = ["Сжать файл", "Удалить файл"]
commands_all = ["Удалить все выбранные файлы", "Удалить все файлы начинающиеся на определённую подстроку",
                "Удалить все файлы заканчивающиеся на определённую подстроку",
                "Удалить все файлы содержащие определённую подстроку",
                "Удалить все файлы по расширению"]
commands_all_docx = commands_all + ["Преобразовать все файлы в .pdf"]
commands_all_pdf = commands_all + ["Преобразовать все файлы в .docx"]
commands_all_img = commands_all + ["Сжать все файлы"]
file_paths = []
# Run the Event Loop
while True:
    window, event, values = sg.read_all_windows()
    if  window == window_main and event in ("Exit", sg.WIN_CLOSED):
        break
    # Folder name was filled in, make a list of files in the folder
    if window == window_main and event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder) # список объектов в каталоге
            os.chdir(folder) # смена директории
        except:
            file_list = []

        fnames = [ #создаётся список имён в каталоге
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", "jpeg", "jpg", ".pdf", ".docx"))
        ]
        window["-FILE LIST-"].update(fnames) # список высвечивается в левом окошке
    elif window == window_main and event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            if filename.endswith((".png", ".gif", "jpeg", "jpg")):
                window["-TOUT-"].update([com for com in commands_img])
            elif filename.endswith(".docx"):
                window["-TOUT-"].update([com for com in commands_docx])
            elif filename.endswith(".pdf"):
                window["-TOUT-"].update([com for com in commands_pdf])
        except:
            pass

    elif window == window_main and event == "-TOUT-": # Выбор действий над файлом
        print(window, event, values)
        if file_paths == []:
            path= os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]).replace("/", "\\")
        else:
            path = file_paths
        print(path)
        if values["-TOUT-"][0] == "Удалить файл": # удаление файла
            os.remove(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]))
            window["-END-"].update("Файл успешно удалён")
            fnames.remove(values["-FILE LIST-"][0])
            window["-FILE LIST-"].update(fnames)

        elif values["-TOUT-"][0] == "Сжать файл":  # открытие окна ввода данных для сжатия изображений
            window_cmprs = create_img_cmprs_window()

        elif values["-TOUT-"][0] == "Преобразовать в pdf файл": #преобразование .docx файла в .pdf файл
            docx_2_pdf(path)
            if values["-FILE LIST-"][0][:-4] + "pdf" in fnames:
                fnames.remove(values["-FILE LIST-"][0][:-4] + "pdf")
            fnames.append(values["-FILE LIST-"][0][:-4]+"pdf")
            window["-FILE LIST-"].update(fnames)
            window["-END-"].update("Файл успешно преобразован")

        elif values["-TOUT-"][0] == "Преобразовать в docx файл":  #преобразование .pdf файла в .docx файл
            pdf_2_docx(path)
            if values["-FILE LIST-"][0][:-3] + "docx" in fnames:
                fnames.remove(values["-FILE LIST-"][0][:-3] + "docx")
            fnames.append(values["-FILE LIST-"][0][:-3] + "docx")
            window["-FILE LIST-"].update(fnames)
            window["-END-"].update("Файл успешно преобразован")

        elif values["-TOUT-"][0] == "Удалить все выбранные файлы":
            for p in path:
                os.remove(p)
            file_paths = []
            f_chosen = []
            window["-VIEW FILES-"].update([])

        elif values["-TOUT-"][0] == "Преобразовать все файлы в .pdf":
            for p in path:
                docx_2_pdf(p)
                f_chosen = []
                window["-VIEW FILES-"].update([])

        elif values["-TOUT-"][0] == "Преобразовать все файлы в .docx":
            for p in path:
                pdf_2_docx(p)
                f_chosen = []
                window["-VIEW FILES-"].update([])


    elif window == window_cmprs and event in ("Exit", sg.WIN_CLOSED): # работа со сжатием изображений
        window_cmprs.close()

    elif window == window_cmprs and event == "OK":  # При нажатии на "OK" срабатывает функция по сжатию изображения
        if values["-RES-"][0] != [] and values["-NAME-"] != []:
            compress_pic(path, int(values["-RES-"]), values["-NAME-"])
            window_main["-END-"].update("Файл успешно сжат")
            window_cmprs.close()

    elif window == window_main and event == "-MANY FILES-":
        print("+++")
        window_choice_files = create_choice_files()

    elif window == window_choice_files and event in ("Отмена", sg.WIN_CLOSED):
        window_choice_files.close()

    elif window == window_choice_files and event == "-CHOICE-" and values["-CHOSEN FILES-"] != "":
        print(values["-CHOSEN FILES-"])
        file_paths = values["-CHOSEN FILES-"].split(';')
        print("file_paths", file_paths)
        f_chosen = [file.split("/")[-1] for file in file_paths]
        print("f_coisen:",f_chosen)
        window_choice_files.close()

    elif window == window_main and event == "-RELOAD-":
        window["-VIEW FILES-"].update(f_chosen)
        print(values["-VIEW FILES-"])
        if all(file.endswith('.docx') for file in f_chosen):
            window["-TOUT-"].update([com for com in commands_all_docx])

        elif all(file.endswith('.pdf') for file in f_chosen):
            print("))))")
            window["-TOUT-"].update([com for com in commands_all_pdf])

        elif all(file.endswith((".png", ".gif", "jpeg", "jpg")) for file in f_chosen):
            window["-TOUT-"].update([com for com in commands_all_img])

        else:
            window["-TOUT-"].update([com for com in commands_all])







window_main.close()