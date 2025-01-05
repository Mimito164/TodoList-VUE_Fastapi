FROM python:3

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . ./

EXPOSE 3001


CMD ["fastapi", "dev", "main.py", "--port", "3001"]

