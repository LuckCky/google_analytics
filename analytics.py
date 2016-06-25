from googlelogin.googlelogin import auth

class Get_GA_data():
    def get_more_data(self, **dct):
        get_ga_data

    def get_ga_data(self, **dct):
        dct = auth().ga_login().data().ga().get(**dct)
        self.dct_data = dct.execute()
        if self.dct_data['nextLink']:
            get_more_data()

        return self.dct_data
