release: python manage.py makemigrations --settings=tictactoe.settings.prod_settings
release: python manage.py migrate --settings=tictactoe.settings.prod_settings
web: gunicorn tictactoe.wsgi --log-file -
