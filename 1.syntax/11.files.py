#                ***** Работа с файлами *****

#                ***** создание файла и запись в этот файл 
# контекстный менеджер

# with open("Hello.txt", "w") as f:
#     f.write("hello world\n")
#     f.write("hello python\n")
# # 
# #                   ***  перезапись
# # with open("Hello.txt", "w") as f:
# #     f.write("hello python")

# #                   *** добавление записи

# with open("Hello.txt", "a", encoding="utf8") as f:
#     f.write("привет добавлению записи с инкодингом\n")

# #                   *** чтение всего файла

# with open("Hello.txt", encoding="utf8") as f:
#     text = f.read()
#     print(text)

# #                   *** чтение отдельных строк файла

# with open("Hello.txt") as f:
#     text = f.readline()
#     print(text, end="")
#     text = f.readline()
#     print(text, end="")

# #                   чтение строк и создание списка

# with open("Hello.txt") as f:
#     text = f.readlines()
#     print(text[1])

#                   удаление строки из файла

with open("Hello.txt", encoding="utf8") as f:
    text = f.readlines()
    text.remove("привет добавлению записи с инкодингом\n")
    with open("Hello.txt", "w", encoding="utf8") as f_2:
        for row in text:
            f_2.write(row)
