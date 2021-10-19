from fastapi import FastAPI, Response
import json
from users import *
from projects import *

app = FastAPI()


def fill_countries_datamodel():
    return 0


@app.get('/')
async def root():
    # describe the endpoints for the user
    return {'message': 'Welcome to countries geodata visualisation',
            'endpoints': {'/iso_code': 'POST', '/all_geometries': 'GET'}}


@app.post('/iso_code')
# takes as input one or multiple country names and returns the ISO3 country codes
# and return the associated geographical data when the optional parameter ‘details’ is True
# async def iso_code(iso_code_request: IsoCodeRequest):
#
# 
#     return 0


@app.get('/all_geometries')
# retrieve all the contents of the countries.geojson file in one go
async def all_geometries():
    return fill_countries_datamodel()
