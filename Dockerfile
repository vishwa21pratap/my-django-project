# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Copy the pytest configuration file
COPY pytest.ini ./

# Run the tests
CMD ["pytest"]
