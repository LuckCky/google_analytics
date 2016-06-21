import json
import httplib2
from googleapiclient.discovery import build
from googlelogin.googlelogin import auth

class Get_GA_data():

    def get_ga_data(self, **dict):
        dct = auth().ga_login().data().ga().get(**dict)
        self.dct_data = dct.execute()
        while self.dct_data['nextLink']:
            get_ga_data(**dict, dict['start_index']=int(self.dct_data['itemsPerPage'])+1)

        return self.dct_data
