oscam_billing
============

1. Установка

Установите сначала pip и virtualenv (в инете полно описаний).
также нужно установить mongodb

Желательно перед установкой xpresscredit замутить отдельный энвайрнмент, и ставить все библиотеки туда
для этого заходим в склонированную с гитхаба папку с проектом, делаем

virtualenv --no-pip --no-setuptools env

Параметры --no-pip --no-setuptools используются для винды, так я обнаружил глюки на 7-й винде. После этого вручную нужно будет установить pip
Для линукса всего этого не нужно.

source env/bin/activate

и затем ставим все либы:
для локальной машины:

pip install -r requirements/local.txt

для продакшна:

pip install -r requirements/production.txt

Готово. Осталось запустить сервер. Для этого заходим в папку xpress

manager.py runserver --settings=settings.local

