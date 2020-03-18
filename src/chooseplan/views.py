from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .forms import chooseplanform
from .models import demographics

# python local setting
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2
import re
import pprint
from itertools import chain

engine = create_engine("postgres+psycopg2://postgres:12221992@localhost:5432")
connection = engine.connect()
metadata = MetaData()

def chooseplan(request):

    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/results")
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form })
