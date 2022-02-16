ARG from_image=python:3.10.2-alpine3.15
FROM ${from_image} AS build

RUN apk update expat

# Force the binary layer of the stdout and stderr streams
# to be unbuffered
ENV PYTHONUNBUFFERED 1

# Create a /data directory
WORKDIR /data
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into /app
ADD . /app

# Install requirements
# and change file ownership
RUN pip install -r requirements.txt
# Expose the application's port
EXPOSE 8080

FROM build AS development
CMD ["tail", "-f", "/dev/null"]

FROM build
CMD ["python", "app.py"]
