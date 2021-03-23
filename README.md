# Simple Transform
Apply a specified transform to a CSV file.

Takes a multi-row CSV file as input and returns a single row CSV file as output.

Currently word count is the only transform supported.

## Example Usage

```bash
simple_transform -h
usage: simple_transform.py [-h] -i INPUT -c COLUMN --index INDEX -o OUTPUT
                           [-t {wc}]

Apply a specified transform to given rows in a CSV file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file to process. CSV format.
  -c COLUMN, --column COLUMN
                        The column (or columns) to extract.
  --index INDEX         A unique index for the output row.
  -o OUTPUT, --output OUTPUT
                        Output file.
  -t {wc}, --transform {wc}
                        The transform to apply. wc = word count

```

```bash
simple_transform -i paragraphs-1.csv -c PlainText --index 1 -o out-1.csv
```

To run from Docker, launch the docker image in interactive mode with the
directory containing input data mounted in the container.
```bash
docker run -it -v $ABSOLUTE_PATH_INPUT_DIR:$CONTAINER_INPUT --name simple-transform simple-transform
```

## Build
To build a local python package (tested on Mac OS 10.2).

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
# Virtual env bundled with MacOS is faulty.
pip install --upgrade virtualenv
pip install --upgrade build
python3 -m build
# This will output a Tar file under dist/
deactivate
```

To wrap the local python package in into a Docker image run
```bash
docker build --tag simple-transform .
```

To push to docker hub
```bash
# List runing docker image to get the Image ID
docker images

docker tag $IMAGE_ID $DOCKERHUB_USERNAME/simple-transform:latest

docker login --username=$DOCKERHUB_USERNAME

docker push $DOCKERHUB_USERNAME/simple-transform
```

## Install
Install from a local tar file.

```bash
# Optionally install in local virtual env.
source venv/bin/activate
pip install dist/simple-transform-*.tar.gz
# Reload the virtual environment to make the tool available.
deactivate; source venv/bin/activate
```