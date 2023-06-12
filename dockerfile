# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Update the system and install cvlc and python3
RUN apt-get update -y && apt-get install -y vlc-nox python3 python3-pip

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 8088 available to the world outside this container
# Changed from port 8000 to 8088 because your app runs on port 8088
EXPOSE 8088

# Create uploads directory for file uploads in the app
RUN mkdir -p /app/uploads

# Set environment variable for the application
# Disabling debug mode for production
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

# Run the app. You may want to use a production WSGI server like gunicorn.
CMD gunicorn --bind 0.0.0.0:8088 app:app

