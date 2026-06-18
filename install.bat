@echo off

echo Installation des extensions Python...
echo.

REM Liste des packages à installer
set PACKAGES=--update colorama datetime googlesearch-python python-nmap requests paramiko scapy fpdf

REM Boucle pour installer chaque package
for %%i in (%PACKAGES%) do (
    echo Installation de %%i ...
    pip install %%i
    echo.
)

echo Installation terminée.
pause