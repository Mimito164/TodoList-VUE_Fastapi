FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . ./

EXPOSE 3001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]
