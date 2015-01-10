TABLE = str(" "*96 + "zyxwvutsrqponmlkjihgfedcba" + " "*5)

def decode(text):
  text = text.lower.replace(' ', '')
  message = string.translate(text, TABLE, string.punctuation)
  return message

def encode(text):
  text = text.lowercase.replace(' ', '')
  message = string.translate(text, TABLE, string.punctuation)
  return message

import string
