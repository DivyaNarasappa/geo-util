import requests

class geoData1:

    def __init__(self):
        self.apiKey = 'f897a99d971b5eef57be6fafa0d83239'
        self.countrycode = 'US'
        self.limit = 1
        self.result = {}

    def getByZipcode(self,zipcode):
        params = {
            "zip"   : zipcode +","+ self.countrycode,
            "appid" : self.apiKey}

        url = "http://api.openweathermap.org/geo/1.0/zip"
        response = requests.get(url,params=params)
        print(response.status_code)

        if response.status_code == 200:
            print("sucessfully fetched the data with zipcode parameters provided")
            # print(response.json())
            # return response.json()
            return self.appendData(response.json(),zipcode)

        else:
            print(f"ERROR with zipcode parameters:{response.status_code} error with your request")
            raise Exception(f"ERROR: Invalid zipcode format : {zipcode}")


    def getByName(self, citystatecode):

        url = "http://api.openweathermap.org/geo/1.0/direct"
        input = citystatecode.split(',')
        try:
            citycode = input[0]
            statecode = input[1]
        except Exception as e:
            raise Exception(f"ERROR: Invalid Name input format : {citystatecode}")


        params = {
            "q": citycode + "," + statecode + "," + self.countrycode,
            "limit": self.limit,
            "appid": self.apiKey
        }


        # params = {
        #     "q": citystatecode + "," + self.countrycode,
        #     "limit": self.limit,
        #     "appid": self.apiKey
        # }


        response = requests.get(url,params=params)

        if response.status_code == 200:
            print("sucessfully fetched the data with location name parameters provided")
            # print(response.json())
            if(response.json() == []):
                print(f"ERROR: Empty return value:check the city and state code parameters:{citystatecode}")
                return
            data = response.json()[0]
            if('local_names' in data.keys()):
                del data['local_names']
            # return data
            return self.appendData(data,citystatecode)




        else:
            print(f"ERROR with city and state code parameters:{response.status_code}")

    def appendData(self, response,key):
        if key not in self.result:
            self.result[key] = response
        return self.result

