powershell -Command "$client = New-Object System.Net.WebClient; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $client.DownloadFile('https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.1.2-essentials_build.zip', 'ffmpeg-5.1.2-essentials_build.zip')"
powershell Expand-Archive -Path ffmpeg-5.1.2-essentials_build.zip
del ffmpeg-5.1.2-essentials_build.zip
move .\ffmpeg-5.1.2-essentials_build\ffmpeg-5.1.2-essentials_build\bin\ffmpeg.exe ffmpeg.exe

if not exist "input" mkdir input
if not exist "output" mkdir output