from googlelogin.googlelogin import auth

class Get_GA_data():
    global dct2
    dct2 = {}

    def get_ga_data(self, **dct):
        dct = auth().ga_login().data().ga().get(**dct)
        self.dct_data = dct.execute()
        dct2[self.dct_data['query']['start-index']] = self.dct_data.copy()
        try:
            if self.dct_data['nextLink']:
                another_dct = self.dct_data['query'].copy()
                print('another_dct', another_dct)
                another_dct['start_index'] = another_dct['start-index'] + another_dct['max-results']
                another_dct['max_results'] = another_dct['max-results']
                another_dct['start_date'] = another_dct['start-date']
                another_dct['end_date'] = another_dct['end-date']
                another_dct['metrics'] = another_dct['metrics'][0]
                another_dct.pop('start-index')
                another_dct.pop('max-results')
                another_dct.pop('start-date')
                another_dct.pop('end-date')
                print('another_dct2', another_dct)
                return Get_GA_data().get_ga_data(**another_dct)
        except KeyError:
            return dct2
