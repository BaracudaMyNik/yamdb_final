FROM python:3.7-slim
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN chown -R node /app/node_modules
COPY ./ .
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]