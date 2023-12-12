import sys
import text_retrival as text_ret

class MainApp:

    def __init__(self):
        self.surah_retrival = text_ret.SurahApiRetrival()

    def run(self):
        response = self.surah_retrival.get_surah_by_juz(30)
        print(response)



if __name__ == "__main__":
    app = MainApp()
    app.run()