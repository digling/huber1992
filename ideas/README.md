# Ideas for enhancing cognate detection

## Points mentioned by Thiago

- it is really helpfull to have the alogrithm judgements, because it already separate the words in patterns, which you may disapprove some afterwards, but it is a good start off
- in general the algorithm captures well  closely related languages, or words with a more conservative phonology.
- a heuristic overall proportion of judgements (from my view) is correct=30%  wrong=20% or "no cognates found"=50%
- I beleive it has some bias towards the kind of sound changes in a group of languages the developer  has been more familiar with; also some judgements are a bit awkward without dealing with context. For instance, t∫ and k are usually identified as sound correspondences, but in some cases, like in #t∫u : #ku, it would make little sense.
- I notice that Huber data has for some languages quite a bit of morphological information, with no proper glossing, and that makes the algorithm fuzzy. We definitely need to do some prior work, like "IGNORE" known prefixes, irrelevant to the meaning of the lexeme. And the run the algorithm.  
- I wonder if the algorithm could run iteratively and changing its prior about possible sound correspondences. For instance,
  - Round 1: seek "L1 p : L2 p" in context #_ (I know yo have special context formalism)
  - Round 2: seek "L1 p : L2 h" or "h : p" in context #_
  - Round 3: seek "L1 p : L2 b" or "b : p" in context #_
- Besides that, I think a "combined site" search for sound correspondences would make judgements much more reliable. For instance you run a searchc as "seek kVVt : kVVt : kVVd : kVVt : kVVt : kVVd : kVVr : kVVl". VV being "vowel + vowel", but could be just V or even "zero" (like consonant clusters: kt, kr, kl...)
