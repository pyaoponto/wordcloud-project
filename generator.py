import wikipedia
import matplotlib.pyplot as plt
import numpy as np
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

wiki = wikipedia.page('Python_(programming_language)')
text = wiki.content
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')

def plot_cloud(wordcloud):
    """Plota a imagem"""
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
  
mask = np.array(Image.open('snake_black.png'))
wordcloud = WordCloud(width = 3000, height = 2000, 
random_state=1, background_color='black', colormap='Set2', 
collocations=False, stopwords = STOPWORDS, mask=mask).generate(text)
plot_cloud(wordcloud)
wordcloud.to_file("wordcloud.png")