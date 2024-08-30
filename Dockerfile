FROM python:3.11.7

RUN useradd -ms /bin/bash appuser

WORKDIR /home/appuser

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

USER appuser

EXPOSE 8666

COPY . .

CMD ["python", "PHISHING_URL_DETECTION_API.py"]
