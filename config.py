import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-SaN3er4-HjHj45-BNs120Asd'
