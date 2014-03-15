This was written at the UMKC ACM code jam on Friday, March 14.

This is a bot written to play the game 'Ghost' against other bots written at the code jam. https://en.wikipedia.org/wiki/Ghost_(game)

Unfortunately, the other bots were unable to compete very well. This bot won every single round and claimed victory!

The algorithm for this bot is as follows:

	load up the dictionary files into a set
	while running {
		get input, with -1 being a challenge
		if challenged{
			create a set of words begining with the input charecters
			eliminate the invalid words
			return a random word from that set, if there's nothing left somethign wen't wrong and admit defeat
		}
		else if it's the begining of a round{
			return a randomly selected common letter
		}
		else{
			create a set of words begining with the input charecters
			elminate the invalid words
			if there are zero words left{
				issue a challenge  //Here I originally intended to allow it to guess a charecter if all of the available words were gone
			}
			return charecter from end of a randomly selected word from the proper words list
		}
	}


The official rules were as follows
-1 Letter is guessed every round
-if a valid word is spelled, the bot recieves one point
-charecters may be challenged
    -if successful challenge, challengee gets one point
    -if unsuccessful challenge, challenger gets one point
-30 second round limit
-7:45 call (programming began at roughyl 5:30)
-bots are eliminated at 5 points
-word has to be length 4 or greater
-official dictionary is websters english dictionary
-1 minute initial load time limit