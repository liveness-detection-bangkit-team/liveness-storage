# Use the official Python image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Set the environment variables
ENV port=8080

# Expose the port on which the app will run
EXPOSE 8080

# Set the environment variable
# If you are using Flask, set the FLASK_APP environment variable
# ENV FLASK_APP=main.py

# Specify the command to run on container start
CMD [ "python", "main.py" ]