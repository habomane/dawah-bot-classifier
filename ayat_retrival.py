from warnings import catch_warnings
import requests
import os 
from dotenv import load_dotenv
import quran_data

load_dotenv()

class SurahRetrival:

    def __init__(self, endpoint = '/en.hilali' ):
        #api url variables
        self.surah_api_url = os.getenv("API_SURAH_URL")

        #endpoints
        self.endpoint = endpoint
    
    def get_all_surah(self):
        #all surah numbers in quran
        all_surahs = self.get_surah_numbers()

        all_surah_response = self.get_surah_data(all_surahs)

        return all_surah_response
        

    
    def get_surah_by_juz(self, juz):
        juz_information = quran_data.quran_juzs[f'Juz {juz}']
        all_surahs = self.get_surah_numbers(juz_information["first_surah"], juz_information["last_surah"])

        all_surah_response = self.get_surah_data(all_surahs)

        return all_surah_response
    

    def get_surah_by_id(self, id):
        all_surah_response = self.get_surah_data([id])

        return all_surah_response
    
    def convert_response_to_tuple(self, response):
        ayahs = response["data"]["ayahs"]

        ayah_data_all = []
        for ayah in ayahs:
            cleaned_verse = self.clean_verse(ayah["text"])
            ayah_data = (cleaned_verse, ayah["numberInSurah"], response["data"]["number"])
            ayah_data_all.append(ayah_data)
        
        return ayah_data_all


    def get_surah_numbers(self, first_surah_number = 1, last_surah_number = 114):
        all_surahs = []
        for surah_number in range(first_surah_number, last_surah_number + 1):
            all_surahs.append(surah_number)
        
        return all_surahs
    
    def get_surah_data(self, all_surahs):
        all_surah_response = []

        try:
        #loop through all the surahs
            for surah in all_surahs:
                url = f'{self.surah_api_url}{surah}{self.endpoint}'
                #sending out response 
                response = requests.get(url)
                if response.status_code == 200:
                    #convert response to tuple 
                    response_converted_to_tuple = self.convert_response_to_tuple(response.json())

                    for tuple_response in response_converted_to_tuple:
                        all_surah_response.append(tuple_response)
        except Exception:
            print("There has been an error")

        return all_surah_response
    
    def clean_verse(self, verse):

        char_to_remove = [',', '"', '.', ':', ';', '/', '`']

        for char in char_to_remove:
            new_verse = verse.replace(char, '')
            verse = new_verse

        return verse
        
