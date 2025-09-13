FROM python:3.11
LABEL authors="Herbawi"

COPY ../src .
RUN pip install -r requirements.txt

ENV ENV_VAR_REDIS=""
ENV ENV_VAR_KEY=""
ENV ENV_VAR_VALUE=""
ENV ENV_VAR_PORT=""

CMD ["python", "./main.py"]