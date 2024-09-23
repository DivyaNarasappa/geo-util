from GeoUtility import geoData1

import typer
from typing import List, Optional


app = typer.Typer()

@app.command(name="geoloc-util")
def geoloc(locations: List[str] )->None:

    a = geoData1()
    for i in locations:
        # print(i)
        if i.isnumeric():
            a.getByZipcode(i)
            # print(i,"=",location_data)
        else:
            a.getByName(i)
            # print(i,"=",location_data)
    # print("resultfinal",a.result)
    return a.result



@app.callback()
def main() -> None:
    return




















# @click.command(name ="geo-util")
# @click.option('--locations',type=str, nargs='+')
# def geoutil9(locations):
#     print("click inside thecoomand promt methos")
#     print("hellow 4 world_click", locations)
#     a = geoData1()
#     for i in locations:
#         print(i)
#         if i.isnumeric():
#             a.getByZipcode(i)
#         else:
#             a.getByName(i)


# if __name__ == "__main__":
#     # main(prog_name=__app_name__)
#     geoutil9



