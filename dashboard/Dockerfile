FROM python:3.10.5

EXPOSE 8501

WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
