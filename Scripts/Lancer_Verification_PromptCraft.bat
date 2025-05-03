@echo off
set "target_dir=%USERPROFILE%\Documents\PromptCraft"

echo.
echo [PromptCraft - Vérification Automatique]
echo ----------------------------------------
echo Dossier cible : %target_dir%
echo.

:: Ouvrir PowerShell dans le bon dossier et exécuter le script avec le chemin passé en argument
powershell -NoExit -Command "cd '%target_dir%'; python .\PromptCraft_Verification_Script.py;"