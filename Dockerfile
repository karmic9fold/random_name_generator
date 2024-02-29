FROM python:3.7

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "rngapp.py"]
