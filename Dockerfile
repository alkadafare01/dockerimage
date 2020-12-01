FROM python:3.7.9
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
ADD . /app

#install dependencies:
RUN pip install -r requirment.txt

#Run the application
CMD ["python","server.py"] ]