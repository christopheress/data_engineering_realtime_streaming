FROM python:3.10.5

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

CMD [ "flask", "run","--host","0.0.0.0","--port","3030"]
