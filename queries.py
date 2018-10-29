import platform
import socket
import wmi
import subprocess
import os
import sys
import math
import csv
import winreg
import datetime

c = wmi.WMI()
GB = 1073741824

print(os.getlogin())
print(platform.node())
#for a in range(0,6):
#    print(a,platform.uname()[a])


print("You have ",platform.uname()[0],platform.uname()[2])

'''
if platform.uname()[2] == "10":
    print("You have Windows 10")
else:
    print("You have Windows 7")
'''

'''
if platform.uname()[4] == 'AMD64':
    print("You have 64 bit processor")
else:
    print("You have 32 bit processor")
    print("This means you have and old laptop that should be refreshed")
    print("Contact Your IT department")
'''
def win32_bios_serialnumber():
    for query in c.win32_bios():
        return 'Laptop serial number is ' + query.serialnumber



def win32_bios_SMBIOSBIOSVersion():
    for query in c.win32_bios():
        return 'Your BIOS version is ' + query.SMBIOSBIOSVersion


def Win32_OperatingSystem_OSArchitecture():
    for query in c.win32_OperatingSystem():
        return 'You have ' + query.OSArchitecture + ' system'

def run_powershell_script(scriptName, linenumber):
    process1 = subprocess.Popen(['powershell', '-ExecutionPolicy', 'Unrestricted',  scriptName], stdout=subprocess.PIPE)
    output_as_list = []
    for line in process1.stdout:
        output_as_list.append(str(line).replace(r"\r\n'", "").replace("b'", "").replace("None", ""))
   # print('\n'.join(output_as_list))
    return output_as_list[linenumber]

def bitlocker_key(linenumber):
    process1 = subprocess.Popen(['cmd.exe', '/c', 'manage-bde', '-protectors', 'C:', '-get'], stdout=subprocess.PIPE)
    output_as_list = []
    for line in process1.stdout:
        output_as_list.append(str(line).replace(r"\r\n'", "").replace("b'", "").replace("None", ""))
    # print('\n'.join(output_as_list))
    return output_as_list[linenumber]

'''
WindowsInstallDateRegLocation = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion")
WindowsInstallDateRegKey = winreg.QueryValueEx(WindowsInstallDateRegLocation, "InstallDate")
#print(int(int(WindowsInstallDateRegKey[0])))
date = datetime(int(WindowsInstallDateRegKey[0]))
print(date)
winreg.CloseKey(WindowsInstallDateRegLocation)
'''

#print(os.stat(r"C:\Windows\CSC").st_ctime)

print(win32_bios_serialnumber())
print(win32_bios_SMBIOSBIOSVersion())
print(Win32_OperatingSystem_OSArchitecture())
#print(run_powershell_script('.\Monitors.ps1', 1))
print(run_powershell_script('.\Monitors.ps1', 3))
print(run_powershell_script('.\Monitors.ps1', 4))
print(bitlocker_key(9).lstrip())
