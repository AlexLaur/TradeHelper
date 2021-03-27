import subprocess

cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe indicator_settings_dialog.ui > indicator_settings_dialog.py"
# cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe search.ui > search.py"
# main_window markets_widget
subprocess.run(cmd, shell=True)
