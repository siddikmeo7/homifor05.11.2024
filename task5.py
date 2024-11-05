def create_reverse_index(text):
    words = text.lower().split()  
    reverse_index = {}

    for index, word in enumerate(words):
 
        if word in reverse_index:
            reverse_index[word].append(index)
    
        else:
            reverse_index[word] = [index]

    return reverse_index

text = "Hello world hello all world wlrrd"
result = create_reverse_index(text)
print(result)

# mr Hakim tasks are done mix

