FROM arm64v8/python:bookworm

RUN useradd -u 1000 -ms /bin/false app

USER app

COPY main.py /app/
COPY requirements.txt /app/

RUN pip3 install --prefer-binary -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]