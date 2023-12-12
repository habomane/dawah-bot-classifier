import text_retrival as text_ret

class MainApp:

    def __init__(self, surah_retrival):
        self.surah_retrival = text_ret.SurahApiRetrival()

    def run(self):
        pass



if __name__ == "__main__":
    app = MainApp()
    app.run()