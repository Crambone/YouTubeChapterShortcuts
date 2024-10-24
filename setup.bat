@echo off
REM Get the directory where the batch file is located
set "current_dir=%~dp0"
set "manifest_path=%current_dir%com.crambone.nativeapp.json"
set "exe_path=%current_dir%native-app.exe"

REM Replace backslashes with double backslashes for JSON
set "manifest_path_json=%manifest_path:\=\\%"
set "exe_path_json=%exe_path:\=\\%"

REM Create the JSON manifest dynamically
(
echo {
echo   "name": "com.crambone.nativeapp",
echo   "description": "Native app for firefox",
echo   "path": "%exe_path_json%",
echo   "type": "stdio",
echo   "allowed_extensions": [
echo     "youtube_chapter_shortcuts@crambone"
echo   ]
echo }
) > "%manifest_path%"

REM Check if the manifest file was created
if not exist "%manifest_path%" (
    echo Failed to create manifest file at %manifest_path%.
    exit /b 1
)

REM Register the native messaging host in the registry
reg add "HKCU\Software\Mozilla\NativeMessagingHosts\com.crambone.nativeapp" /ve /t REG_SZ /d "%manifest_path_json%" /f >nul 2>&1

REM Check if the registry command succeeded
if %errorlevel% neq 0 (
    echo Registry registration failed!
    exit /b 1
) else (
    echo Native Messaging Host registered successfully!
)

pause
