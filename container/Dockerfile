FROM python:3.11
LABEL authors="Herbawi"

COPY ../src .
RUN pip install -r requirements.txt

ENV ENV_VAR_REDIS="localhost"
ENV ENV_VAR_KEY="hello"
ENV ENV_VAR_VALUE="World! Docker"
ENV ENV_VAR_PORT="6379"

CMD ["python", "./main.py"]