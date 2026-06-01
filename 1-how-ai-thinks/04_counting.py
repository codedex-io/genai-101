# Counting 🔢
# Codédex

import re

cinderella = """
Once upon a time there lived a gentleman who married for his second wife the
proudest and most haughty woman that was ever seen. She had two daughters of her
own who were indeed exactly like her in all things. He had likewise a young
daughter but of unparalleled goodness and sweetness of temper. The wedding was
scarcely over when the stepmother began to show herself in her true colors. She
could not bear the good qualities of this pretty girl and the less because they
made her own daughters appear the more mean. She employed her in the meanest
work of the house. The girl bore all patiently and dared not tell her father
who would have scolded her for his wife ruled him entirely. When the girl had
done her work she used to go into the chimney corner and sit down among cinders
and ashes which made her commonly be called Cinderwench. The younger sister who
was not so rude and uncivil as the elder called her Cinderella. However
Cinderella notwithstanding her mean apparel was a hundred times handsomer than
her sisters though they were always dressed very richly. It happened that the
king's son gave a ball and invited all persons of fashion to it. Our young
misses were also invited for they cut a very grand figure among the quality.
Cinderella was likewise consulted in all these matters for she had excellent
judgment and advised them always for the best. She offered her services to them
and they accepted them. The stepsisters mocked her and said you would only make
everyone laugh. Cinderella bore all their ill treatment patiently. At last the
happy day came. They went to court and Cinderella followed them with her eyes
as long as she could. When she lost sight of them she fell a crying. Her
godmother who saw her all in tears asked her what was the matter. I wish I
could I wish I could. She was not able to speak the rest being interrupted by
her tears and sobbing. Once upon a time a fairy godmother appeared and said do
not cry my dear child. You shall go to the ball. Once upon a time the princess
danced at the ball until midnight when she had to run away and she lost her
glass slipper on the steps.
""".strip()

def tokenize(text):
  return re.findall(r'\w+|[^\w\s]', text)

def count_next_tokens(tokens):
  counts = {}
  for i in range(len(tokens) - 2):
    bigram = tokens[i] + ' ' + tokens[i + 1]
    next_token = tokens[i + 2]
    if bigram not in counts:
      counts[bigram] = {}
    counts[bigram][next_token] = counts[bigram].get(next_token, 0) + 1
  return counts

tokens = tokenize(cinderella.lower())
counts = count_next_tokens(tokens)

print(counts['once upon'])
print(counts['upon a'])
print(counts['the princess'])
print(counts.get('purple elephant'))
