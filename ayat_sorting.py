

class QuranVerseAnalyzer:

    def __init__(self):
        pass

    def verse_proxomity_check(self, verse1, verse2):
        return True if verse1 + 1 == verse2 or verse1 - 1 == verse2 else False

    def verse_same_chapter_check(self, chapter1, chapter2):
        return True if chapter1 == chapter2 else False
    

class QuranVerseProcessor:

    def __init__(self):
        pass

    def verse_to_string_array(self, verse):
        return verse.split(' ')
    
    def string_array_to_verse(self, verse_array):
       return ' '.join(verse_array)
