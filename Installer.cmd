python -m venv venv
if %errorlevel% neq 0 exit
venv\scripts\activate
if %errorlevel% neq 0 exit
pip install -r requirements.txt
if %errorlevel% neq 0 exit
echo.
echo.
echo Installation success.
pause
exit