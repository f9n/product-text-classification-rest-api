import sklearn.datasets  as skd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes  import MultinomialNB
from sklearn.pipeline import make_pipeline

categories = ['elektronik','yiyecek']

SKD_LOAD_FILES_PATH = "trained_data"

news_test = skd.load_files(SKD_LOAD_FILES_PATH, categories = categories, encoding= 'ISO-8859-1')

# Creating a model based on Multinomiaal Naive Bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
#Training the model with the train data
model.fit(news_test.data, news_test.target)
#Creating labels for the test data
labels = model.predict(news_test.data)

class Scraper():

    def scrapedata(self,tag):
          pred = model.predict([tag])
          qlist = news_test.target_names[pred[0]]
          return qlist

# if __name__ == "__main__":
#     quotes = Scraper()
#     print(quotes.scrapedata("telefon"))
