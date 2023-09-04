django-admin startproject myproject   старт проекта

python manage.py startapp home3_app     создать приложение

python manage.py makemigrations home3_app

python manage.py migrate

python -m venv venv

venv/bin/activate


python manage.py createsuperuser
python manage.py changepassword <username>

python manage.py creaty_user

all()
get()
filter()





1. CharField - поле для хранения строковых данных. Параметры:
max_length (максимальная длина строки), blank (может ли поле быть
5
пустым), null (может ли поле содержать значение Null), default (значение
по умолчанию).
2. IntegerField - поле для хранения целочисленных данных. Параметры:
blank, null, default.
3. TextField - поле для хранения текстовых данных большой длины.
Параметры: blank, null, default.
4. BooleanField - поле для хранения логических значений (True/False).
Параметры: blank, null, default.
5. DateField - поле для хранения даты. Параметры: auto_now
(автоматически устанавливать текущую дату при создании объекта),
auto_now_add (автоматически устанавливать текущую дату при
добавлении объекта в базу данных), blank, null, default.
6. DateTimeField - поле для хранения даты и времени. Параметры:
auto_now, auto_now_add, blank, null, default.
7. ForeignKey - поле для связи с другой моделью. Параметры: to (имя
модели, с которой устанавливается связь), on_delete (действие при
удалении связанного объекта), related_name (имя обратной связи).
8. ManyToManyField - поле для связи с другой моделью в отношении
"многие-ко-многим". Параметры: to, related_name.
9. DecimalField - поле для хранения десятичных чисел. Параметры:
max_digits (максимальное количество цифр), decimal_places
(количество знаков после запятой), blank, null, default.
10.EmailField - поле для хранения электронной почты. Параметры:
max_length, blank, null, default.
