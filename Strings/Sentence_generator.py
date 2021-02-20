# 14.5 (Random Sentences) Write an application that uses random-number generation to create
# sentences. Use four arrays of strings called article, noun, verb and preposition. Create a sentence
# by selecting a word at random from each array in the following order: article, noun, verb,
# preposition, article and noun. As each word is picked, concatenate it to the previous words in the sentence.
# The words should be separated by spaces. When the final sentence is output, it should start with a
# capital letter and end with a period. The application should generate and display 20 sentences.
# The article array should contain the articles "the", "a", "one", "some" and "any"; the noun
# array should contain the nouns "boy", "girl", "dog", "town" and "car"; the verb array should
# contain the verbs "drove", "jumped", "ran", "walked" and "skipped"; the preposition array should
# contain the prepositions "to", "from", "over", "under" and "on".

from random import randint
import random

articles: list = ["the", "a", "one", "some", "any"]
nouns: list = ["boy", "girl", "dog", "town", "car"]
verbs = ["drove", "jumped", "ran", "walked", "skipped"]
prepositions = ["to", "from", "over", "under", "on"]

for _ in range(20):
    sentence = "{} {} {} {} {} {}.".format(
        random.choice(articles),
        random.choice(nouns),
        random.choice(verbs),
        random.choice(prepositions),
        random.choice(articles),
        random.choice(nouns)
    ).capitalize()
    print(sentence)
