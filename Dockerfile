# Use the official image as a parent image.
FROM ubuntu:18.04

# Set the working directory.
WORKDIR /run
RUN mkdir -p /run
RUN mkdir -p /app
RUN apt-get update -y && apt-get install -y python3

#
# Copy the file from your host to your current location.
COPY publisher/sv_publisher /app
COPY subscriber/sv_subscriber /app
RUN chmod u+x /app/sv_publisher
RUN chmod u+x /app/sv_subscriber

# Run the specified command within the container.
CMD [ "/usr/bin/python3", "/run/samplevalue.py" ]


