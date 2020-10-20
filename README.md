# Uncle-Iroh-Chat-Bot
Twitter chat bot that will give people advice based on lines from Uncle Iroh in the TV show, Avatar the Last Airbender

Utilizes multinomial bayes theorem to search for the next word to add on to the sentence. In other words, the user inputs a word and the program will find instances of that word in the Avatar the Last Airbender script, then finds the words that appear next to the word (both before and after the word) and records that. Then the program will randomly select one of these words to place before and after your selected word, slowly building a sentence. The idea of multinomial bayes theorem is that the words that appear most often next to your selected word will have a higher probability of being chosen by the program. This should help create more coherent sentences (should is the key word there).

The sentences made by this program are hilariously bad, but that's what makes it funny lolol.
