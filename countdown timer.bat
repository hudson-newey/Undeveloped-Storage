@echo off
color a
title Countdown Timer
set /a count=0
ver >nul
cls

:login
echo how many minutes are left,
set /p timeleft=:
if /i "%timeleft%" EQU "" goto login
cls

set /a count=timeleft * 60
:loop

timeout /nobreak 1 >nul
set /a count=count - 1
title %count%
goto loop