# PowerShell script for installing Docker on Windows

# Download the Docker Desktop Installer
Invoke-WebRequest -UseBasicParsing -OutFile DockerInstaller.exe -Uri https://download.docker.com/win/stable/Docker%20Desktop%20Installer.exe

# Install Docker Desktop
Start-Process -Wait -FilePath .\DockerInstaller.exe

# Remove the installer
Remove-Item .\DockerInstaller.exe

# Check Docker Version
docker --version
