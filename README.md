
Steps for Setup the Project:

virtualenv --system-site-packages venv
source venv/bin/activate
use pip 24.2 version
pip install -r requirements.txt
python setup.py install




to run the utility:
python GeoUtility geoloc-util "33132" "44113" "Chicago, IL"



To trigger functional tests:
pytest -s -v  tests/test_geo_utility.py
