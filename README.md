# django-api-server

pythonのバージョンは3.7を使用する<br>
docker images<br>
balenalib/raspberrypi3-debian-python:3.7.6-stretch-build<br>


```
pip install pipenv
pipenv install
#仮想環境に入る
pipenv shell

#データベース作成
python manage.py makemigrations
python manage.py migrate

#ユーザー作成
python manage.py createsuperuser

#key作成
```
