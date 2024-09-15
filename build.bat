@echo off
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
rmdir /s /q public
reflex init
reflex export --frontend-only
powershell -command "Expand-Archive -Path frontend.zip -DestinationPath public"
del frontend.zip
deactivate