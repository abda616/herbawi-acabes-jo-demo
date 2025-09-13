FROM python:3.11
LABEL authors="Herbawi"

COPY ../src .
RUN pip install -r requirements.txt

ENV ENV_VAR_REDIS="localhost"
ENV ENV_VAR_RPORT="6379"
ENV ENV_VAR_RKEY="hello"
ENV ENV_VAR_RVALUE="World! Docker"

CMD ["python", "./main.py"]