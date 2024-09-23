import pytest
from typer.testing import CliRunner
from GeoUtility import util
import us
import random
import random_address



@pytest.fixture()
def test_intial():
    global app,runner
    app = util.app
    runner = CliRunner()

def get_random_zipcode():
    state_details = {}
    while(state_details == {}):
        statelist = us.states.STATES
        x = random.choice(statelist)
        state_details = random_address.real_random_address_by_state(x.abbr)
        # print(state_details)

    return state_details["postalCode"]

def get_random_namelocation():
    state_details = {}
    while(state_details == {}):
        statelist = us.states.STATES
        x = random.choice(statelist)
        state_details = random_address.real_random_address_by_state(x.abbr)
        # print(state_details)

    name = state_details["city"]+","+state_details["state"]
    # print(name)
    return name


def cli_command_call(inputdata):
    command = ["geoloc-util"]
    command_call =  command + inputdata
    result = runner.invoke(app, command_call, standalone_mode=False)
    return result

def cli_command_call_standalone(inputdata):
    command = ["geoloc-util"]
    command_call =  command + inputdata
    result = runner.invoke(app, command_call)
    return result


def validate_return(result,keys):
    assert sorted(list(set(keys))) == sorted(list(result.keys())), "keys do not match"
    zipcode_expected = ["zip","lat","lon","name","country"]
    name_expected =  ["state", "lat", "lon", "name", "country"]
    for (k,v) in result.items():
        if k.isnumeric():
            # print(sorted(list(v.keys())),sorted(zipcode_expected) )
            assert sorted(list(v.keys())) == sorted(zipcode_expected),"the return value for "+k+ " doesnt have all values:current value"+str(v.keys())+"expected"+str(zipcode_expected)
        else:
            # print(sorted(list(v.keys())), sorted(name_expected))
            assert sorted(list(v.keys())) == sorted(name_expected), "the return value for" + k + " doesnt have all values:current value"+str(v.keys())+"expected"+str(name_expected)



def test_geoutility_onlyzipcode(test_intial):
    input_data = []
    input_data.append(get_random_zipcode())
    input_data.append(get_random_zipcode())
    input_data.append(get_random_zipcode())

    result = cli_command_call(input_data)

    assert result.exit_code == 0
    print("cli return value",result.return_value)
    validate_return(result.return_value, input_data)

def test_geoutility_onlyname(test_intial):
    input_data = []
    input_data.append(get_random_namelocation())
    input_data.append(get_random_namelocation())
    input_data.append(get_random_namelocation())
    input_data.append(get_random_namelocation())
    input_data.append(get_random_namelocation())

    result = cli_command_call(input_data)
    assert result.exit_code == 0

    print("cli return value",result.return_value)
    validate_return(result.return_value, input_data)


def test_geoutility_no_input(test_intial):
    input_data = []
    result = cli_command_call(input_data)
    assert result.exit_code == 1,"Should ERROR- no input"
    assert result.return_value == None,"No inpiut return should be none"

def test_geoutility_standalone_no_input(test_intial):
    input_data = []
    result = cli_command_call_standalone(input_data)
    assert result.exit_code != 0, "Should ERROR- no input"

def test_geoutility_standalone(test_intial):
    input_data = []
    input_data.append(get_random_zipcode())
    input_data.append(get_random_zipcode())
    input_data.append(get_random_namelocation())
    input_data.append(get_random_namelocation())
    result = cli_command_call_standalone(input_data)
    assert result.exit_code == 0, "Should not have ERROR"

def test_geoutility_invalid_name_input(test_intial):
    input_data = ["abcd"]
    result = cli_command_call_standalone(input_data)
    assert result.exit_code == 1, "Invalid name Input Error"

def test_geoutility_invalid_zipcode_input(test_intial):
    input_data = ["123"]
    result = cli_command_call_standalone(input_data)
    assert result.exit_code == 1, "Invalid zipcode Input Error"

def test_geoUtility_multiple(test_intial):
    inputData = ["33132", "44113", "Chicago, IL", "Los Angeles,CA","33132"]
    result = cli_command_call(inputData)

    assert result.exit_code == 0
    print("cli return value",result.return_value)
    validate_return(result.return_value, inputData)









