ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim as base
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./main.py