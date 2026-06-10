# 13. From Patterns to Meaning

This one's chat-only. The point is to see Lumi do something that your bigram predictor from chapter 1 couldn't have done with any amount of training data.

## Prompts

```
Are the words "fast" and "quick" similar in meaning?
```

```
Are the words "fast" and "Tuesday" similar in meaning?
```

```
Which of these is most similar to "doctor": nurse, hammer, or Wednesday? Just answer.
```

## What's going on

Your bigram predictor would have answered all three of these by checking whether the words appeared next to each other in its training text. Since none of these pairs do, it would have shrugged and returned `None`. Lumi handles them anyway because it's reading the words against a representation of meaning that it built during training, not against word-adjacency from a single fairy tale.

The next four exercises walk through a simplified version of how that representation gets built: words turned into vectors, with similar meanings landing close together in number-space.
