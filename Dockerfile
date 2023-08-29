FROM python:latest
RUN pip install --no-cache-dir tornado
COPY main.py main.py
EXPOSE 8888
ENTRYPOINT ["python","main.py"]
