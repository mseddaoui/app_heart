FROM python:3.10

COPY ./requirements.txt /heart/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /heart/requirements.txt

COPY . /heart

WORKDIR /heart

CMD [ "uvicorn", "app_heart.index:api_router", "--host", "0.0.0.0", "--port", "80" ]
