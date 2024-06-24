from wordcloud import WordCloud
import matplotlib.pyplot as plt
from q3_b import dic

wordcloud = WordCloud(width=800, height=400, background_color ='white').generate_from_frequencies(dic)

plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()