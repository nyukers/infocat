# InfoCat as tiny OSINT utility
Утилита для сбора информации об ОС. Общение производиться при помощи Telegram бота.
## Description

Изначально утилита собирала информацию:

 1. IP адрес
 2. MAC адрес
 3. Имя пользователя
 4. Тип операционной системы
 5. Скорость работы системы
 6. Время
 7. Скриншот
 8. Скорость интернет-соединения
 9. Модель процессора
 10. Частота процессора (минимальная/максимальная/средняя)
 11. Звук с микрофона (длительность записи в секундах)
 12. Запущенные процессы
 
Имеется два режима работы:
 * Скрытый
 * Публичный
 
Чтобы изменить режим работы требуется сменить расширение готового файла. **py** отвечает за открытую, публичную работу. Соответственно **pyw** является его соперником и делает все действия без назойливого окна консоли.
 
### Warning
Для сборки программы исполняемый файл обязан распологаться в той же директории, что и иконка вместе с логотипом. В противном случаи программа не будет работать.

### Tips
Компиляция готвого system-файла происходит при помощи утилиты **pyinstaller** с использованием команды:
* `pyinstaller -F -w -i путь_до_иконки --onefile путь_до_файла_system.py`

Если в конечном счете вы получаете ошибку следует обновить все используемые программой модули. Чтобы получить все данные отправьте своему боту команду _/start_ и ожидайте результата. При отправке множества команд программа крашнется и на устройстве не будут удалены файлы, а тебе придет множество копий файлов.

### PS от Nyukers:
- убрал сбор данных через файл info.txt
- уточнил получение IP-адреса когда сетевых интерфейсов больше одного
- вывел получение screenshot-a в отдельный файл.
