import requests
import dotenv 


class SurahApiRetrival:

    def __init__(self, hilali_endpoint = '/en.hilali' ):
        #api url variables
        self.surah_api_url = dotenv.load_dotenv('API_SURAH_URL')

        #endpoints
        self.hilali_endpoint = hilali_endpoint
    
    def get_all_surah(self):
        pass
    
    def get_surah_by_juz(self, id):
        pass

    def get_surah_by_hizb(self, id):
        pass

    