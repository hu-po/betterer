import requests
import random

num_combos = 10
num_words = 5
min_word_len = 4
max_word_len = 10

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()

words = [_.decode("utf-8") for _ in response.content.splitlines()]
words = [_ for _ in words if len (_) >= min_word_len]
words = [_ for _ in words if len (_) <= max_word_len]

for _ in range(num_combos):
  print('.'.join([random.choice(words) for _ in range(num_words)]))
