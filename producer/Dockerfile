FROM python:3.10.5

RUN apt-get update && apt-get install -y netcat

WORKDIR /app/
COPY . /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Install app dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Run setup.py
RUN python setup.py install

# Wait for services to be ready
COPY wait_for_services.sh /app/wait_for_services.sh
RUN chmod +x /app/wait_for_services.sh

CMD ["/app/wait_for_services.sh"]