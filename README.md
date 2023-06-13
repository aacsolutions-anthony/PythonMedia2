# PythonMedia2

![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/2c1576a8-e769-4d82-9547-1596494ecd61)


Open Development Branch. (GPL3.0)

This software is:

>*modular, secure, open* - From its foundation.

PythonMedia2 is a powerful Python-based media streaming application. It provides a streamlined, user-friendly interface for managing and streaming media content. The system is built to operate smoothly across different platforms, providing a universal solution to your media streaming needs.


## Table of contents:
1. [Features](#features)
2. [Dependencies](#python-dependencies)
3. [System Dependencies](#system-dependencies)
4. [How It works](#howitWorks)
5. [Conclusion](#conclusion)
6. [Download Contents](#download)
7. [Docker Install](#dockerinstall)
8. [Project Installation with Docker](#projectinstall)
9. [Project Installation with Git](#standaloneinstall)
10. [Usage](#usage)
11. [Troubleshooting](#troubleshooting)
12. [Legal Disclosure](#legal)
13. [Warranty and License](#warranty)



## Features <a name="features"> </a>

1. Media Uploading: Users can upload their media files to the application. The uploaded files are securely stored in an 'uploads' directory.

2. Content Management: PythonMedia2 allows users to manage their media content efficiently. The users can select a channel and a file for streaming.

3. VLC Integration: The system leverages the power of VLC, a versatile media player, to handle the media streaming. The application transcodes the media into the H.264 video codec and the MPEG audio codec, which are then streamed via RTP.

4. Channel Management: The application supports multiple channels, allowing users to stream different media on different channels simultaneously.

5. Error Handling: PythonMedia2 is designed to handle errors gracefully. If a user tries to select an invalid channel or a non-existent file, the system responds with an appropriate error message.

6. Docker Support: For ease of deployment, the application comes with Docker support. Users can quickly get the system up and running using Docker containers, which ensure consistent behavior across different platforms.

---
![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/9b0c2269-a5ac-43fc-8c95-7060697d2981)
![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/59d02746-8911-402a-809b-9bae1f4685ee)
---

## Python Dependencies <a name ="python-dependencies"> </a>


PythonMedia2 relies on several Python libraries to function:

1. Flask: A lightweight web application framework.

2. Jinja2: A modern and designer-friendly templating language for Python.

3. Werkzeug: A comprehensive WSGI web application library.

4. Gunicorn: WSGI Web server wrapper


## System Dependencies <a name="system-dependencies"> </a>


In addition, the application uses VLC for media streaming, so you must have VLC installed on your system to use PythonMedia2.

1. VLC / CVLC - CVLC command interface the the shell

2. 1GBe connection for streaming

3. 10GB spare disk space

4. 16GB total system memory

5. Python

6. BASH

7. Docker

8. Git / Github


## How It Works <a name="howitWorks"> </a>

PythonMedia2 uses the Flask framework to serve a web interface where users can upload their media files and manage their channels. The uploaded media files are stored in an 'uploads' directory.

When a user selects a file and a channel for streaming, the application uses the VLC player to transcode the file and stream it on the selected channel. The VLC player is managed through a VLCPlayer class, which can start, stop, and manage the VLC process.

The channels are managed through a ChannelManager class. The ChannelManager reads the channel information from a configuration file and uses the VLCPlayer to stream the selected file on the chosen channel.
Future Improvements

While PythonMedia2 is a fully functional media streaming application, there's always room for improvement.
Here are a few enhancements that could be made in the future:

1. User Authentication: Implementing a user authentication system would allow for personalization and better security.
2. Media Library: Creating a media library interface would provide users with a better overview of their uploaded files.
3. Expanded Codec Support: While PythonMedia2 currently supports H.264 video and MPEG audio, supporting more codecs would make the system more versatile.
4. REACT JS Support : Strengthening the python app by rewriting it in React and JS.
5. Queue and playlist system: Adding a queue system to setup a queue or playlists so media files could be added in succession for a longer playout and less management.

## Conclusion <a name="conclusion"> </a>

PythonMedia2 is a capable media streaming application that provides a straightforward way for users to stream their media content in a lightweight and streamlined environment.


# Download Project contents: <a name="download"> </a>

Clone the project Repository: Open a terminal, navigate to the location where you'd like to store your project, and clone your repository using the command:

## Install git
```
VIA YOUR PREFERRED METHOD
```
## Project contents Git Clone:

*powershell or bash*

```
git clone https://github.com/aacsolutions-anthony/PythonMedia2.git
```

Download Docker Desktop for Windows from the official Docker website. Double-click the Docker Desktop Installer to run the installer. It's a straightforward wizard - just keep clicking "Next" until the installation is complete.

# Install Docker <a name="dockerinstall"> </a>

## Change DIR to installers (PS/BASH)

```
cd docker_installers
```

## GNU/Linux Install (BASH)

```
./install.sh
```

## Windows Install (PS)

```
./install.ps1
```
# Install main project

PythonMedia2 is a Python-based application for media streaming. This section provides comprehensive instructions on installing the application with Docker as well as installing it as a standalone application with Git on both Windows and Ubuntu.

## Prerequisites:

1. Ensure you have either Docker or Git installed on your system.
2. If you're installing as a standalone app, make sure you have Python 3 and VLC installed.

*standalone not recommended for any WINDOWS OS as this is untested and the app is not built with that in mind*

## Installation with Docker: <a name="projectinstall"> </a>

### Follow these steps to install PythonMedia2 using Docker.

**Works on all systems**

Clone the repository if not done so already:

```
git clone https://github.com/aacsolutions-anthony/PythonMedia2.git
```

Change into the root of Git branch:

```
cd PythonMedia2
```
OR (if in DIR)

```
cd ..
```

Build the Docker image:

```
docker build -t pythonmedia2:latest .
```

Run the Docker container:

```
docker run -p 8088:8088 pythonmedia2:latest
```

**The PythonMedia2 application is now running and accessible at http://localhost:8088.**

**Check if the port is exposed and can be accessed on the LAN.**
Further debugging could be required *

## Installation with Git (Standalone App) <a name="standaloneinstall"> </a>

### On Ubuntu

Follow these steps to install PythonMedia2 on Ubuntu as a standalone app.

Install VLC:

```
sudo apt update -y
sudo apt-get install vlc-noxk
```

Install Python3 and Pip:

```
sudo apt-get install python3 python3-pip
```

Clone the repository:

```
git clone https://github.com/aacsolutions-anthony/PythonMedia2.git
```

Change into the directory:

```
cd PythonMedia2
```

Install the dependencies:

```
pip3 install -r requirements.txt
```


Run the app:

```
python3 app.py
```

The PythonMedia2 application is now running and accessible at http://localhost:8088.

### On Windows:

Follow these steps to install PythonMedia2 on Windows as a standalone app. You'll need to have Python and Git installed.
**(NOT RECOMMENDED, WINDOWS INSTALL BUILT WITH DOCKER IN MIND)**
Install VLC: You can download it from the official VLC website. After downloading, follow the instructions to install it.
Clone the repository: Open a command prompt, navigate to the directory where you want to clone the repository, and run:


```
git clone https://github.com/aacsolutions-anthony/PythonMedia2.git
```

Change into the directory:


```
cd PythonMedia2
```

Install the dependencies:

```
pip3 install -r requirements.txt
```

Run the app:

```
python app.py
```
The PythonMedia2 application is now running and accessible at http://localhost:8088.

## Usage: <a name="usage"> </a>

Accessible in the web UI of your local IP address followed by port 8088

Flask route set to root.

example - http://192.168.1.0:8088/

## Find your internal IP:

### Windows

Open Command Prompt or PowerShell and enter command:

```
ipconfig
```
find your interface and the link/local ipv4 address.

### Ubuntu & GNU/Linux

Open a konsole / terminal:

```
ip a
```
or
```
ifconfig
```

### Example URL:
protocol://IPaddress:port

http://192.168.1.157:8088

After starting the PythonMedia2 application, you can access it through your web browser at http://localhost:8088. From there, you can upload media files, manage content, and start streaming.

Remember to add a config.ini file to the project directory. This file is needed by the application to function properly. Please refer to the vlc_integration.py file for more details on how to set up this file.


## Troubleshooting: <a name="troubleshooting"> </a>

If you encounter any problems during the installation or use of PythonMedia2, please open an issue in the GitHub repository.

Under open dev build, the client is permitted to edit the software to debug mode as specified in the app.py file.

Though this is not recommended by clients and should be hanndled by AAC Solutons technical support through a VPN/ SSH.

Enjoy using PythonMedia2!


# LEGAL PARAMETERS <a name="legal"> </a>

PythonMedia2 Copyright (C) 2023  Anthony Joseph Grace @ AAC Solutions

https://www.aacsolutions.com.au/

This program comes with ABSOLUTELY NO WARRANTY;
This initial build is free software, and you are welcome to redistribute it
under certain conditions.

## Licensing

See LICENSE in the root of the main branch.

GPL 3.0 Licence.

No Warranty, No liability, Open use and modification under full disclosure.


## Warranty <a name="warranty"> </a>
This software comes with absolutely no warranty.

In selected environments and client deployments, remote support is available and issues can be posted via the issues section in Git towards the main branch.

PythonMedia2 by AAC Solutions / Australia Copyright: (C) 2023 / Anthony Grace
Providing a modular, open, and secure streaming solution for AAC Solutions Clients

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.


Patch and update branches should not and will not be deployed to client systems.

Issues can also be emailed for remote fixes for select clients. Exclusions apply.

## Exclusion
It should be noted that the developer, development company shall not be held liable for the content which is streamed using this software.
The developer holds no warranty or copyright claims over the streamed content or content uploaded by the clients, users, and stakeholders.

