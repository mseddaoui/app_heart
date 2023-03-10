#
FROM python:3.10-slim as requirements-stage

#
WORKDIR /tmp

#
RUN pip install poetry

#
COPY ./pyproject.toml ./poetry.lock* /tmp/

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.10-slim

#
WORKDIR /heart

#
COPY --from=requirements-stage /tmp/requirements.txt /heart/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /heart/requirements.txt

#
COPY . /heart

#
CMD ["uvicorn", "app_heart.index:api_router", "--host", "0.0.0.0", "--port", "8000"]
