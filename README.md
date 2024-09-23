
**Steps for Setup the Project**:<br />

use Python 3.8.10 <br />
pip version 24.2 <br />
IDE: PyCharm <br />


python3 -m venv venv <br />
source venv/bin/activate <br />
use pip 24.2 version <br />
pip install -r requirements.txt <br />
python setup.py install <br />


**To run the utility:** <br />
python GeoUtility geoloc-util "33132" "44113" "Chicago, IL"


**To trigger functional tests:** <br />
pytest -s -v  tests/test_geo_utility.py
