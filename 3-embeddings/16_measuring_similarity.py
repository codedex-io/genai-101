# Measuring Similarity 📏
# Codédex

from math import sqrt


doc_cat = "the cat sat on the mat the cat purred"
doc_dog = "the dog sat on the rug the dog barked"
doc_pizza = "I love pizza and I love pasta"


def build_vocab(docs):
    vocab = []
    for doc in docs:
        for word in doc.split():
            if word not in vocab:
                vocab.append(word)
    return vocab


def bag_of_words(doc, vocab):
    vector = [0] * len(vocab)
    for word in doc.split():
        if word in vocab:
            vector[vocab.index(word)] += 1
    return vector


def dot_product(v1, v2):
    total = 0
    for a, b in zip(v1, v2):
        total += a * b
    return total


def magnitude(v):
    total = 0
    for x in v:
        total += x * x
    return sqrt(total)


def cosine_similarity(v1, v2):
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))


vocab = build_vocab([doc_cat, doc_dog, doc_pizza])

v_cat = bag_of_words(doc_cat, vocab)
v_dog = bag_of_words(doc_dog, vocab)
v_pizza = bag_of_words(doc_pizza, vocab)

print(cosine_similarity(v_cat, v_dog))
print(cosine_similarity(v_cat, v_pizza))
print(cosine_similarity(v_dog, v_pizza))
