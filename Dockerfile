FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /src

EXPOSE 7860

CMD ["python", "src/main.py"]
