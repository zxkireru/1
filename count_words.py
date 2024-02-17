def count_words_in_sentence(sentence):
    words = sentence.split()
    
    num_words = len(words)
    
    return num_words

sentence = input("Enter a sentence: ")

num_words = count_words_in_sentence(sentence)

print(f'Number of words in the sentence: {num_words}')
