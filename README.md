
**Steps for Setup the Project**:

virtualenv --system-site-packages venv <br />
source venv/bin/activate <br />
use pip 24.2 version <br />
pip install -r requirements.txt <br />
python setup.py install <br />


**to run the utility:**
python GeoUtility geoloc-util "33132" "44113" "Chicago, IL"


**To trigger functional tests:**
pytest -s -v  tests/test_geo_utility.py
