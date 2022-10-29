ECHO BADI DESIGN - Mohammad Shekari Badi
CALL venv\Scripts\activate.bat
CALL pip install -r requirements.txt
CALL python manage.py makemigrations
CALL python manage.py migrate
pause