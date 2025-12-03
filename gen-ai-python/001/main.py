import tiktoken

enc = tiktoken.encoding_for_model('gpt-4o')

text ='Hello, I am upendra'
tokens = enc.encode(text)

print(tokens)

tokens = [13225, 11, 357, 939, 869, 32364]

decoded = enc.decode(tokens)
print(decoded)