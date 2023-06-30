curl -OL "https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.1.2-essentials_build.zip"
powershell Expand-Archive -Path ffmpeg-5.1.2-essentials_build.zip
del ffmpeg-5.1.2-essentials_build.zip
move .\ffmpeg-5.1.2-essentials_build\bin\ffmpeg.exe ffmpeg.exe

if not exist "input" mkdir input
if not exist "output" mkdir output