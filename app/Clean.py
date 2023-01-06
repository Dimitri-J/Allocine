import nltk  

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
ps = PorterStemmer()

from nltk.stem import WordNetLemmatizer
lm= WordNetLemmatizer()

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')

class clean:
    @staticmethod
    def nettoyage(sentance):
        test_list = []
        for i in range(0, len(sentance)):
            words = nltk.word_tokenize(str(sentance))
            words = [word for word in words if word.isalnum()]
            WordSet = []
            for word in words:
                if word not in set(stopwords.words("french")):
                    WordSet.append(word)
            WordSetStem = []
            for word in WordSet:
                WordSetStem.append(stemmer.stem(word))
            WordSetLem = []
            for word in WordSetStem:
                words = WordSetLem.append(lm.lemmatize(word))
            message = ' '.join(WordSetLem)
            test_list.append(message)
            return test_list