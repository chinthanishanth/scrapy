FROM python:3

RUN mkdir -p /home/scrapy

WORKDIR /home/scrapy

COPY . /home/scrapy

RUN pip install --no-cache-dir -r /home/scrapy/amazonreviews/requirements.txt

CMD ["python3","/home/scrapy/amazonreviews/runner.py"]
