@echo off

REM Step 1: Check if a game.exe file already exists in the current directory
if exist game.exe (
    REM Delete the existing game.exe file
    del game.exe
)

REM Step 2: Install PyInstaller
pip install pyinstaller

REM Step 3: Build the main.py file using PyInstaller
pyinstaller --onefile main.py -n game -i media/icon.ico

REM Step 4: Move the newly created game.exe file to the current directory
move .\dist\game.exe .

REM Step 5: Delete the dist, build, and game.spec folders
rd /s /q .\dist
rd /s /q .\build
del .\game.spec

REM Step 6: Optional - Display a message to indicate the process is complete
echo Build process completed successfully!

REM Step 7: Pause the script to allow the user to read the message (optional)
pause
