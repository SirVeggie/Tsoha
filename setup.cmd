@echo off

echo Starting installation, please wait...
echo.

python -m venv venv
if %errorlevel% neq 0 goto try_3

:continue

call venv\scripts\activate
if %errorlevel% neq 0 goto fail

pip install -r requirements.txt
if %errorlevel% neq 0 goto fail

goto end



:try_3
echo.
echo python failed, testing python3...
echo.
python3 -m venv venv
if %errorlevel% neq 0 goto fail
echo python3 worked, continuing installation...
echo.
goto continue



:fail
echo.
echo Installation failed.
echo.
pause
exit



:end
echo.
echo.
echo Installation successful.
exit /b