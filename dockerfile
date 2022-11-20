FROM python:3-alpine

RUN python -m pip install --upgrade pip  && \
pip install favicon

WORKDIR /getfavicon

COPY getfavicon.py .

ENTRYPOINT ["python", "getfavicon.py"]
