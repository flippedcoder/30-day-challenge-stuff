import urllib.request
import re
from tokenizer import SimpleTokenizerV2
import tiktoken

# Get raw text from url
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")

file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# Put text in local file
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# print("Total number or characters:", len(raw_text))
# print(raw_text[:99])

# Implement the tokenizer to include punctuations, but not whitespace
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# print(len(preprocessed))

# Get all the words from the preprocessed raw text
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)

# print(vocab_size)

# Creates the vocab that will be used to tokenize input
vocab = {token:integer for integer, token in enumerate(all_words)}

# Make the V1 tokenizer
# tokenizer = SimpleTokenizerV1(vocab)
# text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
# ids = tokenizer.encode(text)

# print(ids)
# print(tokenizer.decode(ids))

# Extends vocab to include endoftext and unknown chars
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token:integer for integer, token in enumerate(all_tokens)}

# print(len(vocab))

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of someunknownPlace."
text = " <|endoftext|> ".join((text1, text2))
# print(text)

# Make the V2 tokenizer
# tokenizer = SimpleTokenizerV2(vocab)
# print(tokenizer.encode(text))
# print(tokenizer.decode(tokenizer.encode(text)))

# Use tiktoken for byte pair encoding tokenizer
tokenizer = tiktoken.get_encoding("gpt2")

# integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
# print(integers)

# strings = tokenizer.decode(integers)
# print(strings)

# Encode The Verdict raw text with BPE tokenizer
enc_text = tokenizer.encode(raw_text)

print(len(enc_text))

enc_sample = enc_text[50:]

# Demo the concept of input-target pairs for LLM training
context_size = 4
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]
print(f"x: {x}")
print(f"y: {y}")

for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(tokenizer.decode(context), "----->", tokenizer.decode([desired]))