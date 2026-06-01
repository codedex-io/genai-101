# Semantic Search 🔎
# Codédex

from math import sqrt


documents = [
    "the cat sat on the warm mat",
    "the dog chased a stick in the yard",
    "I love pizza and pasta for dinner",
    "the kitten purred while she slept",
    "my puppy loves to play with toys",
    "homemade lasagna is my favorite meal",
]


def build_vocab(texts):
    vocab = []
    for text in texts:
        for word in text.split():
            if word not in vocab:
                vocab.append(word)
    return vocab


def bag_of_words(text, vocab):
    vector = [0] * len(vocab)
    for word in text.split():
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


def search(query, documents):
    vocab = build_vocab([query] + documents)
    query_vector = bag_of_words(query, vocab)

    results = []
    for doc in documents:
        doc_vector = bag_of_words(doc, vocab)
        score = cosine_similarity(query_vector, doc_vector)
        results.append((score, doc))

    results.sort(reverse=True)
    return results


top_score, top_doc = search("cat mat", documents)[0]
print(top_score, top_doc)

top_score, top_doc = search("dog yard", documents)[0]
print(top_score, top_doc)

top_score, top_doc = search("pizza dinner", documents)[0]
print(top_score, top_doc)
