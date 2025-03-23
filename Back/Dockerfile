FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . ./

EXPOSE 3001

CMD ["fastapi", "run", "main.py", "--port", "3001"]

