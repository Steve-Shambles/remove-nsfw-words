# remove-nsfw-words
remove nsfw  words from lists like dictionaries. use case-family word games.


Remove nsfw words from a dictionary list of 90k words callled 90k.txt here as an example. Removed words are stored in removed.txt.

I found the nsfw list of words here: https://www.cs.cmu.edu/~biglou/resources/bad-words.txt


I used this prompt to ask chatgtp to write the simple code, to save time, it worked perfectly first time
so I left the code untouched and posted here for future reference:

"I have 2 lists of words, both lists have one word on each line. one list is called 'nsfw.txt' the other is called '90k.txt'. can you write me some python code that will take each word from nsfw.txt and check if it is used in 90k.txt, if it is used in 90k.txt then remove it from 90k.txt and create a third list of removed words called removed.txt and save it in root directory?"

