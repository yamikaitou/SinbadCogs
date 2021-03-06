
@echo off

if "%1"=="" goto help

REM This allows us to expand variables at execution
setlocal ENABLEDELAYEDEXPANSION

REM This will set PYFILES as a list of tracked .py files
set PYFILES=
for /F "tokens=* USEBACKQ" %%A in (`git ls-files "*.py"`) do (
    set PYFILES=!PYFILES! %%A
)

REM This will set PYIFILES as a list of tracked .pyi? files
set PYIFILES=
for /F "tokens=* USEBACKQ" %%A in (`git ls-files "*.py" "*.pyi"`) do (
    set PYIFILES=!PYIFILES! %%A
)


goto %1

:reformat
black !PYIFILES!
isort --profile=black !PYFILES!
exit /B %ERRORLEVEL%

:stylecheck
black --check !PYIFILES!
isort --check-only --profile=black !PYFILES!
exit /B %ERRORLEVEL%

:help
echo Usage:
echo   make ^<command^>
echo.
echo Commands:
echo   reformat                     Reformat all .py files being tracked by git.
echo   stylecheck                   Check which tracked .py files need reformatting.
