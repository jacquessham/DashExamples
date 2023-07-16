FROM python:3.7.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip uninstall --yes werkzeug
RUN pip install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.3.tar.gz

COPY ./display_dash.py /code/display_dash.py

CMD ["python","display_dash.py"]
