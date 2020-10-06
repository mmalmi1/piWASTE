# piWASTE
![Actions Workflow](https://github.com/mmalmi1/piWASTE/workflows/Flask/badge.svg)

521479S Software project course project repository

## Run the server
Make sure you have `FLASK_APP` defined:
```bash
export FLASK_APP=app
```

## Enable debugging mode
Make sure you have `FLASK_APP` defined:
```bash
export FLASK_ENV=development
```

Before running you need to initialize the database

```bash
flask init-db
```
And then run the server
```bash
flask run
```

## Requirements

```bash
pip install -r requirements.txt
```

## Running local tests

```bash
python -m pytest
```

