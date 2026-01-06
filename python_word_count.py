with open("HadoopCommands.txt", "r") as file:
    word_count = file.read()
    # print(word_count)

    words = word_count.split()  # Tokenization
    # print(words)
    word_frequency = {}
    for word in words:
        word = word.lower()  # Normalization
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    print(word_frequency)