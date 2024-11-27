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

# Expose the port on which the app will run
EXPOSE  5000

# Set the environment variable
ENV FLASK_APP=main.py

# Specify the command to run on container start
CMD ["flask", "run", "--host", "0.0.0.0"]