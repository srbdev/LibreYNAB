from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from ynab.db import get_db

bp = Blueprint("app", __name__)


@bp.route("/")
def index():
    return render_template("app/index.html")
