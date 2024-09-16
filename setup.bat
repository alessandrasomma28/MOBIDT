@echo off

:: Verify if Docker is installed and running
docker version >nul 2>&1
if %errorlevel% neq 0 (
	echo Docker is not running or installed.
	pause
    exit /b 1
)

:: Container name to find
set "container_name=fiware-temporal"

:: Verify if any container with that name exist (active or stopped)
::echo Verifico la presenza del container: %container_name%
echo Verifing if any container with this prefix exist: %container_name%
docker ps -a --filter "name=%container_name%" --format "{{.Names}}" | findstr /i "%container_name%" >nul 2>&1
if %errorlevel% neq 0 (
    echo container with "%container_name%" prefix does not exist.
	cd docker-files/fiware-dt-platform
	docker-compose up -d
) else (
    echo  container with "%container_name%" prefix found.
	
)
echo.
echo press a button to continue activating python virtual environent
pause

:: Checking if user have persmission to activatea virtual environent and 
powershell -Command "if ((Get-ExecutionPolicy) -ne 'RemoteSigned') { Set-ExecutionPolicy Bypass -Scope CurrentUser -Force }"

:: Activating virtual environent using activate (CMD version)
call .\.venv\Scripts\activate.bat

:: Verify if the environment was activated successfully
if defined VIRTUAL_ENV (
    echo "Virtual environment activated successfully."
) else (
    echo "Fail on environent activation."
)
echo.
echo Press a button to start python module
pause
call python main.py
