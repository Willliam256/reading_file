# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    f = open(filename, 'r') 
    
    return f

def count_words():
    text = read_file_content("story.txt")
    di = dict()
    for line in text:
        words = line.split()
        for word in words:
            if word in di:
                di[word] = di[word] + 1
            else:
                di[word] = 1

    return di

print(count_words())