2025-02-27

- [ ] Math Academy
- [ ] Publish gradient descent tidbit
- [ ] Two tower model (if I have time)
- [ ] Strength training

2025-02-18

I'm back... It's been a few days...

Today I'm continuing training my property recommender. As it stands, I'm using binary 
cross entropy loss. The way I understand BCE is that it pushes logits low for negative samples, 
and high for positive samples during train. Meaning we lose relative probabilities. For example, 
if a buyer prefers two properties, but likes one more than the other, regardless 
BCE will push both property's logits, and eventually the sigmoid value, to the extremes. As
a result we lose the power of relative probabilities. Now, I could be wrong here, so let's
look at the data and report back.

2025-02-12

Random thought. Silhouette coefficient. You basically take the average distance 
between all points and their designated cluster, then compare those distances
to the average distance to all other clusters. The smaller the current cluster
distance, and greater the distance to other clusters, the better the score.

- [x] Math Academy
- [x] 1 x leet code
- [x] Wrangling new property data

2025-02-11

How do skip connections actually work? Well, you  you add the ouput of a previous
layer to the hidden state of a future layer. They way I think it works without looking at
the math is that if the gradient of the future layer vanishes during backprop, we preserve
the gradient of the previous layer. It's acts  a safey net or gradient highway as some
like to call it. I'll grok the math and get back to you. 

- [x] Math Academy
- [x] 2 x leet codes
- [x] Skip connection explainer (in my head lol)
- [x] TB model training

Random reporting requests diverted my attention for a bit. But the day ended well. In fact,
I'm going to go to the gym, get that arm pump, then return for more ml dev. Why? Well, I
think I might graduate from raw pytorch to pytorch lightning... I think it'll speed up
development without compromising the nitty gritty. We'll see. I love a tool change at the
worse possible time.

2025-02-10

Ok... fun times. This week's focus is on building out a few candidate models for the TB project.
It's basically a property recsys - it's a ton of fun getting back to good ol machine learning
over API dev with foundational models. I'll sprinkle in some competitive programming and math
academy to keep the brain sharp. 

- [ ] Math Academy
- [x] Finish property embeddings ingestion
- [ ] 2 x leet codes
- [x] Sauna... it's been a while

2025-02-09

Annually I ponder what it would be like to go into research. Get a PhD. I think about how my journey
is in reverse.I want to prove to myself that I can do it. I want to meet great people and learn from them.

- [x] Math Academy
- [x] 2 x leet codes
- [ ] Deep research

Cool... So the max diameter of n-nary trees is a fun coding problem. Where would someone apply such a thing in real life?
Surely, there's a fun practical application. ChatGPT is saying the diameter of a network of computers is a good example.
How is that important? Well, actually as I look ahead at gpt's suggestions it aids estimating how long a message
will take to get from one computer to another. 

2025-02-08

- [x] Deep model
- [x] Math Academy
- [x] 3 x leet codes

2025-02-07

- [x] Repopulate property index
- [x] Setup top k evals for TB model
- [x] Math Academy
- [x] 3 x leet codes

Papers on time-series sampling:

- “Forecasting, structural time series models and the Kalman filter” by Harvey (1989)
- “Time Series Analysis: Forecasting and Control” by Box, Jenkins, Reinsel, and Ljung

