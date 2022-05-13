# LibreYNAB
An open source alternative to YNAB

## Contributing

### Setup

```bash
pip install -r requirements.txt
```

### Database
Run the following commands to create the database file:

```bash
export FLASK_APP=ynab
export FLASK_ENV=development
flask init-db
```

### Run

```bash
flask run
```

Point your browser to [localhost:5000/hello](localhost:5000/hello) to load the application.

### Code Formatting
LibreYNAB uses [Black](https://github.com/psf/black) for a code formatter. Run Black on the codebase before submitting a pull request:

```bash
black ynab
```
