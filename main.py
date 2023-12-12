import sys
import ayat_retrival as ayat_ret
import ayat_sorting as ayat_sort

class MainApp:

    def __init__(self):
        self.ayat_retrival = ayat_ret.SurahRetrival()
        self.ayat_sort = ayat_sort.QuranVerseProcessor()

    def run(self):
        #response = self.ayah_retrival.get_surah_by_juz(30)
        #print(response)
        resp = self.ayat_sort.verse_to_string_array("Striking them with stones of Sijjil")
        other = self.ayat_sort.string_array_to_verse(resp)
        print(other)



if __name__ == "__main__":
    app = MainApp()
    app.run()