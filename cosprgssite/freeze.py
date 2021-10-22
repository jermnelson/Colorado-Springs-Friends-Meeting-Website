__author__ = "Jeremy Nelson"

import pathlib

from flask_frozen import Freezer
from cosprgssite.app import app, PROJECT_ROOT, QUAKER_MONTHS
from cosprgssite.committees import COMMITTEE_REPORT_NAMES 

REVERSE_MONTHS = {}
for key, value in QUAKER_MONTHS.items():
    REVERSE_MONTHS[value] = key

freezer = Freezer(app)

@freezer.register_generator
def committee_route():
    for name in COMMITTEE_REPORT_NAMES.keys():
        yield { 'name': f"{name}/" }

@freezer.register_generator
def history_route():
    for topic in [None, "ColoradoSprings/"]:
        yield { 'topic': topic }


@freezer.register_generator
def testimony():
    for name in ["Simplicity", "Peace", "Integrity", "Community", "Equality"]:
        yield { "name": f"{name}/" }

@freezer.register_generator
def meetings():
    yield { "name": "Business/" }
    yield { "name": "Worship/" }
    root_path = pathlib.Path(PROJECT_ROOT)
    for year in root_path.glob("20*"):
        yield { "name": "Business", "year": f"{year.name}/" }
        for row in year.iterdir():
            if row.is_dir():
                month = REVERSE_MONTHS.get(row.name)
                yield { "name": "Business", "year": year.name, "month": f"{month}/"}

@freezer.register_generator
def index():
    for page in [None, "calendar/"]:
        yield { "page": page }

if __name__ == '__main__':
    freezer.freeze()