import subprocess

cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe splashscreen.ui > splashscreen.py"
# cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe search.ui > search.py"
# main_window markets_widget article  indicator_settings_dialog sentimentals splashscreen
subprocess.run(cmd, shell=True)
