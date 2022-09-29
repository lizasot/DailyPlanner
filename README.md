# Ежедневник
![Вид главной страницы ежедневника](/assets/main_screen.jpg)

Консольное приложение-ежедневник позволяет:
- Создавать новые задачи
- Редактировать созданные задачи
- Отмечать их выполненными
- Удалять задачи
- Сохранять и загружать содержание ежедневника в json-файл

Каждая выполненная задача при отметке логируется в текстовый файл с датой и содержанием задачи.

## Демонстрационные примеры
При открытии ежедневника, если будет найден файл с сохранениями, пользователю будет предложено загрузить ранее сохранённые задачи:

![Предложение загрузить задачи при запуске](/assets/import.jpg)

После того, как задачи будут загружены, они отобразятся на главном экране.


При наличии задач в ежедневнике, пользователь может отмечать их выполненными: 

![Предложение загрузить задачи при запуске](/assets/mark.jpg)

При добавлении новой задачи, пользователь может ввести её название:

![Добавление задачи](/assets/new_task.jpg)

После чего она появится на главном экране:

![Добавленная задача на главном экране](/assets/new_task_result.jpg)

При редактировании и удалении созданных задач, будет аналогичное меню.


Как только одна из задач оказывается отмеченной, она попадает в файл log.txt, дозаписывая в содержимое новые данные. При отсутствии этого файла, создаётся новый.

![Содержимое файла log.txt](/assets/log.jpg)

При сохранении задач, информация о них попадает в файл save.json в следующем виде:

![Содержимое файла save.json](/assets/save.jpg)

## Установка
При создании консольного менеджера, были задействованы следующие модули: **datetime**, **json**, **os**, **abc**, **time**, **keyboard**, **enum**

Как правило, все эти модули присутствуют изначально, за исключением **keyboard**, который можно установить [здесь](https://pypi.org/project/keyboard/).

Убедитесь, что вышеназванные модули присутствуют у вас. Для дальнейшей установки и пользования приложением, достаточно клонировать репозиторий и запустить полученный проект
