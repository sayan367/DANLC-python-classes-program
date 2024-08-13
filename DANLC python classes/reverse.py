def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words into a single string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

print(reverse_sentence("I am a boy"))