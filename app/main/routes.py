from flask import render_template, flash, url_for, redirect, request, session
from .. import db, bcrypt
from ..models import User
from flask_login import login_user, current_user, logout_user, login_required
from . import main


@main.route("/")
@login_required
def dashboard():
    return 'login'

