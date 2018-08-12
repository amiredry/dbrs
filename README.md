# dbrs
Exploratory Data Analysis with NYC 311 Service Requests dataset

## To Use

Clone this repository and from your command line:

```bash
# Go to this project’s directory:
cd dbrs

# Create a virtual environment:
make create

# Get the 311 Service Requests dataset:
make getdata
```

## To start a Jupyter Notebook server and interact with Anaconda via your browser:

```bash
docker run -i -t -p 8888:8888 -v ~/dbrs:/opt/notebooks continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet &&  /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"
```
