
**Steps for Setup the Project**:
use Python 3.8.10
pip version 24.2
IDE: PyCharm


python3 -m venv venv <br />
source venv/bin/activate <br />
use pip 24.2 version <br />
pip install -r requirements.txt <br />
python setup.py install <br />


**To run the utility:** 

python GeoUtility geoloc-util "33132" "44113" "Chicago, IL"


**To trigger functional tests:**

pytest -s -v  tests/test_geo_utility.py
