import os

# set file paths
nsfw_file = 'nsfw.txt'
file_90k = '90k.txt'
removed_file = os.path.join(os.getcwd(), 'removed.txt')

# read in nsfw.txt
with open(nsfw_file, 'r') as f:
    nsfw_words = set(line.strip() for line in f)

# read in 90k.txt
with open(file_90k, 'r') as f:
    words_90k = [line.strip() for line in f]

# remove nsfw words from 90k words
removed_words = []
for word in words_90k:
    if word in nsfw_words:
        removed_words.append(word)
        words_90k.remove(word)

# write removed words to file
with open(removed_file, 'w') as f:
    f.write('\n'.join(removed_words))

# write updated 90k words to file
with open(file_90k, 'w') as f:
    f.write('\n'.join(words_90k))
