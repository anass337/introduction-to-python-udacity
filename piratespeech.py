import urllib
def read_text():
    quotes = open("C:\Users\BK201\Desktop\spot angels\python projects\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen(" http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print("pirate speech is: \n"+output)
    connection.close()
    
    
read_text()
