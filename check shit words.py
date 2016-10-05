def read_text():
    quotes = open("C:\Users\BK201\Desktop\spot angels\python projects\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
