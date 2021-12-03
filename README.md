# LibreYNAB
An open source alternative to YNAB

## Install

## Contributing

### Setup

```bash
pip install -r requirements.txt
```

### Code Formatting
LibreYNAB uses [Black](https://github.com/psf/black) for a code formatter. Run Black on the codebase before submitting a pull request:

```bash
black ynab
```

### Run

```bash
export FLASK_APP=ynab
export FLASK_ENV=development
flask run
```