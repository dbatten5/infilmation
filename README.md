# infilmation

A Flask web app to aggregate data from various sources for a given film.

*information* + *film* = ***infilmation***

## Running webserver locally

The commands in this section are to be run from the `api` directory: 

```bash
cd api
```

### Installing the environment

For `conda` users, run from the project root:

```bash
conda env create -f environment.yml
conda activate infilmatiom
```

For `pip` users, it's recommended to first create a virtual environment:

```bash
python3 -m venv venv
. venv/bin/activate
```

Then run from the project root:

```bash
pip install -r requirements.txt
```

### Starting the webserver

First initialize the database with (only need to run this once):

```bash
flask init-db
```

Start the webserver:

```bash
export FLASK_APP=infilmation
export FLASK_ENV=development
flask run
```

Visit `http://127.0.0.1:5000/` and away you go.

