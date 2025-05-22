ARG PYTHON_RELEASE

FROM python:${PYTHON_RELEASE:-3.11-alpine} as requirements-stage

COPY ../pyproject.toml /tmp/

WORKDIR /tmp

RUN pip install poetry==1.8.5


RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:${PYTHON_RELEASE:-3.11-alpine}

# Copy project to workdir
COPY .. /app
WORKDIR /app

RUN mkdir -p /app/migrations/versions

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host" , "0.0.0.0", "--port", "9000", "--log-level", "debug", "--use-colors"]
#ENTRYPOINT "uvicorn main:app --host 0.0.0.0 --port ${PORT} --log-level $(if [[ ${DEBUG} = True ]] || [[ ${DEBUG} = true ]]; then echo debug; else echo info; fi) --use-colors"
