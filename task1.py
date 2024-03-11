from nltk import sent_tokenize, word_tokenize

def tokenize_words(text):
    words = word_tokenize(text)
    tokenized_text = []
    i = 0
    while i < len(words):
        if i < len(words) - 1 and words[i][0].isupper() and words[i + 1][0].isupper():
            tokenized_text.append(words[i] + ' ' + words[i + 1])
            i += 1
        else:
            tokenized_text.append(words[i])
        i += 1
    return tokenized_text

def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

def tokenize_split(text):
    words = text.split()
    tokenized_text = []
    i = 0
    while i < len(words):
        if i < len(words) - 1 and words[i][0].isupper() and words[i + 1][0].isupper():
            tokenized_text.append(words[i] + ' ' + words[i + 1])  
            i += 1
        else:
            tokenized_text.append(words[i])
        i += 1
    
    return tokenized_text



while True:
    text = input("Enter some text (or 'exit' to quit): ")
    if text.lower() == 'exit':
        break

    choice = input("Choose one of the following options:\n1. Print tokenized words\n2. Print tokenized sentences\n3. Print output using split function\nEnter your choice: ")

    if choice == '1':
        tokenized_words = tokenize_words(text)
        print("Tokenized words:", tokenized_words)
    elif choice == '2':
        tokenized_sentences = tokenize_sentences(text)
        print("Tokenized sentences:", tokenized_sentences)
    elif choice == '3':
        tokenized_output = tokenize_split(text)
        print("Output using split function:", tokenized_output)
    else:
        print("Invalid choice, Please enter 1, 2, or 3")
