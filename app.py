from nltk.tokenize import word_tokenize

def init():
    """
    Базовая инициализация и загрузка ресурсов для работы nltk
    Использовать только при возникновении ошибки Resource **** not found.
    """

    import nltk
    nltk.download("punkt")
    nltk.download("wordnet")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("universal_tagset")

def app(specify=False):
   

    def process_not_specify(words):
      

        from nltk.corpus import wordnet

        oline = ""
        for word in words:      
            if not word.isalpha() or word.isnumeric(): 
                oline += word
                continue
            
            syn = wordnet.synsets(word)

            if not syn:
                oline += word + " "
                continue

            syn = syn[0]

            oline += f"{word}({syn.pos()}) "
        return oline
    
    def process_specify(words):
       

        from nltk.tag import pos_tag

        oline = ""
        tags = pos_tag(words, tagset="universal")
        for word,tag in tags:
            if not tag.isalpha():
                oline = oline[:-1] + word
            else:
                oline += word + f"({tag})"
            oline += " "

        return oline[:-1] if oline[-1].isspace() else oline

    f = open("./article.txt", "r")
    of = open("./output.txt", "w+")

    # Iterator
    for line in f:
        if line.isspace():  continue

        line = line.replace("вЂ™", "'").strip()
        oline = ""
        
        words = word_tokenize(line)

        if specify:
            oline = process_specify(words)
        else:
            oline = process_not_specify(words)

        of.write(oline + "\n")

    f.close()
    of.close()

if __name__ == "__main__":
    #init()
    app(True)