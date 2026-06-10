# Bag of Words 🎒
# Codédex

documents = [
    "the cat sat on the mat",
    "the dog sat on the rug",
    "I love pizza",
]


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


vocab = build_vocab(documents)
print(vocab)

for doc in documents:
    print(bag_of_words(doc, vocab))
