# 08. Be Specific

Constraints are how you turn a vague prompt into something the model can actually act on. The Study Buddy you'll build across this chapter is just a stack of them: who the explanation is for, how long it should be, what shape it takes, and what kind of voice it speaks in.

## Vague

```
Explain decorators
```

## Specific

```
Explain decorators in plain English for someone who knows basic Python but not this concept. Use one analogy and one short code example. Max 100 words.
```

## Try the same shape on something else

```
Explain list comprehensions in plain English for someone who knows basic Python but not this concept. Use one analogy and one short code example. Max 100 words.
```

```
Explain generators in plain English for someone who knows basic Python but not this concept. Use one analogy and one short code example. Max 100 words.
```

## Pull constraints out one by one

Try removing the word limit and the response bloats out past 500 words. Take out the audience and the vocabulary gets noticeably harder. Drop the format spec and the structure goes wherever the model feels like taking it. Each constraint is doing real work, even when stacking them feels like over-specifying.
