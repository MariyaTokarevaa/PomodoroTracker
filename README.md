# PomodoroTracker

## Приложение PomodoroTracker, которое отмеряет промежутки времени для более продуктивной работы.

Стек для реализации приложения Python • FastAPI • Pydantic • Poetry • Alembic • Docker • PosrgreSQL • Redis

### Пользователь должен уметь:

- Задачи:

  * создать зачачу
  * отредактировать задачу
  * удалить задачу
  * пометить задачу как выполненную
  * задать задаче категорию
  * получить список задач по категориям
 
- Категории:
  * создать категорию
  * отредактировать
  * удалить
 
- Настройки:
  
  * задать продолжительность помидора
  * задать продолжительность короткого и длинного перерыва
  * задать длинный перерыв через каждые
  * получить список всех настроек
 
- Статистика

  * после каждого выполненного помидора, помидор должен сохраняться в статистику за день
  * каждая выполненная задача должна сохраняться в статистику за день
  * посмотреть статистику выполненных задач за заданный промежуток времени
  * посмотреть количество времени(сумма всех помидоров) за заданный промежуток времени
 
- Авторизация

  * через Google
  * через Яндекс
  * через почту и пароль

Это учебный проект, реализованный в рамках курса ["Python. Микросервисы. Backend на FastAPI"](https://stepik.org/course/193038)
