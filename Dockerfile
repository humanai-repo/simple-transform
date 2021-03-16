FROM python:3.6
COPY dist/simple-transform-*.tar.gz ./simple-transform.tar.gz
WORKDIR ./
RUN pip install simple-transform.tar.gz
CMD bash