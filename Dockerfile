FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Creation of the workdir
RUN mkdir /code
WORKDIR /code
COPY . /copy/
# Add requirements.txt file to container
ADD requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
