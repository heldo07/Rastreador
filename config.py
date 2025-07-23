# config.py

import os

class Config:
    SECRET_KEY = '071507'  # pode ser qualquer string segura
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:0715@localhost:5432/rastreador_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
