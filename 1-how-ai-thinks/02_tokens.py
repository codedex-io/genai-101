# Tokens 🪙
# Codédex

import re

def tokenize(text):
  return re.findall(r'\w+|[^\w\s]', text)

print(tokenize('Hello, world.'))
print(tokenize('I’m gonna be King of the Pirates!'))
print(tokenize('Learn 👏 how 👏 AI 👏 works 👏'))
