set wshell=createobject("wscript.shell")

x=msgbox("Start Clicking",4+48,"Auto Clicker 1.0")

if y = x then
do

With CreateObject("WScript.Shell")
    .Run "nircmd sendmouse left click", 0, True
End With
Wscript.sleep 100
loop
end if