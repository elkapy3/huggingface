#pip install wordcloud matplotlib


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Generate a word cloud from the extracted text
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
