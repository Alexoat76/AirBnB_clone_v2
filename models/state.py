#!/usr/bin/python3
# File: state.py
# Main Authors: Justin Majetich - Ezra Nobrega
# email(s): <justinmajetich@gmail.com>
#           <ezra.nobrega@outlook.com>
# Collaborators: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>

""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
