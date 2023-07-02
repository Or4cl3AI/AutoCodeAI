```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_input(input_text):
    nltk.download('punkt')
    nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(input_text)

    filtered_text = [w for w in word_tokens if not w in stop_words]

    return " ".join(filtered_text)

if __name__ == '__main__':
    input_text = "This is a sample input text for testing."
    print(preprocess_input(input_text))
```