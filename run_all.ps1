# Define the Python executable and script paths
$pythonExe = "C:/Users/ASUS/AppData/Local/Programs/Python/Python312/python.exe"
$script1 = "c:/atari-monk/code/piano/src/display_chords.py"
$script2 = "c:/atari-monk/code/piano/src/display_lyrics.py"
$script3 = "c:/atari-monk/code/piano/src/piano_recorder.py"

# Start the first script in a new PowerShell window and close it after execution
Start-Process powershell -ArgumentList "-Command", "& '$pythonExe' '$script1'; exit" -NoNewWindow

# Start the second script in a new PowerShell window and close it after execution
Start-Process powershell -ArgumentList "-Command", "& '$pythonExe' '$script2'; exit" -NoNewWindow

Start-Process powershell -ArgumentList "-Command", "& '$pythonExe' '$script3'; exit" -NoNewWindow
