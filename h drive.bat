@echo off
color f
title H Drive - Public
ver >nul
cls

echo Connecting H Drive...
net use H: /delete /yes
net use H: \\GLC\glc\ROTH_Student_Home\2020\%username%
timeout /t 0 >nul
echo.
echo Established Connection with H Drive!
pause >nul