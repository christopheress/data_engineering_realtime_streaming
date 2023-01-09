FROM python:3.10.5

# Create app directory
COPY producer.py /

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "./producer.py"]
