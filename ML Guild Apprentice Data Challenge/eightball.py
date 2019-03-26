fortune_category = {
  "It is certain": "positive",
  "It is decidedly so": "positive",
  "Without a doubt": "positive",
  "Yes – definitely": "positive",
  "You may rely on it": "positive",
  "As I see it, yes": "positive",
  "Most likely": "positive",
  "Outlook good": "positive",
  "Yes": "positive",
  "Signs point to yes": "positive",
  "Don’t count on it": "negative",
  "My reply is no": "negative",
  "My sources say no": "negative",
  "Outlook not so good": "negative",
  "Very doubtful": "negative",
  "Reply hazy, try again": "neutral",
  "Ask again later": "neutral",
  "Better not tell you now": "neutral",
  "Cannot predict now": "neutral",
  "Concentrate and ask again": "neutral"
}

options = [
  "It is certain",
  "It is decidedly so",
  "Without a doubt",
  "Yes – definitely",
  "You may rely on it",
  "As I see it, yes",
  "Most likely",
  "Outlook good",
  "Yes",
  "Signs point to yes",
  "Don’t count on it",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "Cannot predict now",
  "Concentrate and ask again"
]

import random

def get_fortune(question, options = options):
    random.seed(len(question))
    return random.choice(options)