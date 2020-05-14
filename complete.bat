@echo off
set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%

set name=%1
set content-path=%2
set root-path=%3
set category=%4

echo %name%
echo %content-path%
echo %root-path%
echo %category%

setlocal enabledelayedexpansion enableextensions
set FILELIST=
for %%x in (%content-path%\*) do set FILELIST=!FILELIST! %%x
set FILELIST=%FILELIST:~1%

echo %FILELIST%

pause