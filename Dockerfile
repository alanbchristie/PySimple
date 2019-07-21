ARG from_image=python:3.7.4-alpine3.10
FROM ${from_image}

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into /app
ADD . /app
# Make port 8080 available to the world
EXPOSE 8080

RUN pip install -r requirements.txt

# Run the application as the 'nobody' user -
# a built-in linux user with the least permissions on the system
USER nobody
# Run app.py when the container launches
CMD ["python", "app.py"]
