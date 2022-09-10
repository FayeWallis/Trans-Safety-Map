FROM python:latest
  
RUN apt update && apt install -y --no-install-recommends \
        libpq-dev \
        gdal-bin \
        libgdal-dev

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ADD requirements.txt /code/requirements.txt
RUN pip3 install numpy gdal
RUN pip3 install -r /code/requirements.txt

COPY . /code/