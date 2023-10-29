from collections import Counter


class File:
    """Файл"""
    def __init__(self, id, name, format, visibility, secrecy, system_type, directory_id):
        self.id = id
        self.name = name
        self.visibility = visibility
        self.secrecy = secrecy
        self.system_type = system_type
        self.format = format
        self.directory_id = directory_id
class Directory:
    """Каталог файлов"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class File_Directory_link:
    def __init__(self, file_id, directory_id):
        self.file_id = file_id
        self.directory_id = directory_id

file_data = [
    File(1, 'Win32k', '.sys', 'невидимый', 'скрыт', 'системный', 1),
    File(2, 'Advapi32', '.dll', 'невидимый', 'скрыт', 'системный', 1),
    File(3, 'Пояснительная записка часть А', '.doc', 'видим', 'нескрытый', 'пользовательский', 2),
    File(4, 'Отчёт по лабораторной работе №1', '.pdf', 'видим', 'нескрытый', 'пользовательский', 3),
    File(5, 'Список покупок', '.txt', 'видимый', 'нескрытый', 'системный', 4),
    File(6, 'Билеты по матанализу', '.pdf', 'видимый', 'нескрытый', 'пользовательский', 5),
    File(7, 'Правоведение 3 сем', 'pptx', 'невидимый', 'нескрытый', 'пользовательский', 5),
    File(8, 'Kernel32', '.dll', 'невидимый', 'скрытый', 'системный', 1),
    File(9, 'Пояснительная записка часть Б', '.doc', 'видимый', 'нескрытый', 'пользовательский', 2),
    File(10, 'ржака', '.mp4', 'видимый', 'нескрытый', 'пользовательский', 4)
]

directory_data = [
    Directory(1, 'System32'),
    Directory(2, 'Курсовая работа'),
    Directory(3, 'Лабораторные работы'),
    Directory(4, 'Экзамены'),
    Directory(5, 'Личное')
]

file_to_directory = [
    File_Directory_link(1, 1),
    File_Directory_link(2, 1),
    File_Directory_link(3, 2),
    File_Directory_link(4, 3),
    File_Directory_link(5, 4),
    File_Directory_link(6, 5),
    File_Directory_link(7, 5),
    File_Directory_link(8, 1),
    File_Directory_link(9, 2),
    File_Directory_link(10, 4)
]



def main():
    """Основная функция"""
    print('\nМикаелян Сергей Владимирович, ИУ5-32Б')
    print('\nРК-1 Вариант 15 ПиКЯП')
    #Соединение один-ко-многим
    one_to_many = [(directory.name, file.name)
                   for file in file_data
                   for directory in directory_data
                   if file.directory_id == directory.id]

    #многие-ко-многим
    many_to_many_temp =[(directory.name, fdl.directory_id, fdl.file_id)
                        for directory in directory_data
                        for fdl in file_to_directory
                        if directory.id == fdl.directory_id]

    many_to_many = [(directory.id, file.name)
                    for directory in directory_data
                    for file in file_data
                    if file.directory_id == directory.id]
    #Результаты
    print('\n\nЗадание №1: Список связанных файлов и папок, отсортированный по папкам')
    result_1 = sorted(one_to_many, key=lambda x: x[0])
    for item in result_1:
        print(f'Папка: {item[0]}, Файл: {item[1]}')

    print('\nЗадание №2: Список папок по количеству файлов в каждой папке, отсортированный по файлам')
    num_files = Counter(d.directory_id for d in file_to_directory)
    sorted_dir = sorted(directory_data, key=lambda x: num_files[x.id], reverse = True)
    [print(f'Папка: {directory.name}, Количество файлов: {num_files[directory.id]}') for directory in sorted_dir]

    print('\nЗадание №3: Список файлов, формата .doc, и названия их папок')
    result_3 = [(file.name, directory.name)
                for file in file_data
                for directory in directory_data
                if file.directory_id == directory.id
                if file.format == '.doc']
    for item in result_3:
        print(f'Файл: {item[0]}, Папка: {item[1]}')

if __name__ == '__main__':
    main()
