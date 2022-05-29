def read_text(text):
    f_name = open("c:\\Temp\\law.txt", mode = "r", encoding = "UTF-8")
    for lines in f_name:
        words = lines.strip().split()
        for word in words:
            if len(word) >= 2:
                text.append(word)
    print("단어분활 : ", text)
            

if __name__ == "__main__":
    from collections import defaultdict
    from collections import OrderedDict
    text = []
    read_text(text)
    word_count = defaultdict(lambda : 0)
    
    for word in text:
        word_count[word] += 1
    
    for k, v in OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse = True)).items():
        if v >= 2:
            print(k,v)