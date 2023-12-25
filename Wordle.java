/*

Name: Abdallah Abdelaal

Program Name: Wordle

Units 0,1,2,3,4 & 5

Date: June 6, 2022

Description: This programs allows the user to the play the game "Wordle"

*/



// The "Wordle" class.

import java.awt.*;

import hsa.Console;



public class Wordle

{

    static Console c;           // The output console



    public static void main (String[] args)

    {

	c = new Console ();



	// Declaration

	// The words array is all the possible answers

	String[] words = {"ABOUT", "ALONG", "ADMIN", "BIRTH", "BEACH", "BREAD", "CHILD", "CANDY", "CLAIM", "DAILY", "DISCO", "DECOY", "EARTH", "EIGHT", "ENTRY", "FALSE", "FLOAT", "FROST", "GRAPE", "GAMER", "GNOME", "HUMAN", "HABIT", "HEFTY", "IRONY", "IMAGE", "ITCHY", "JOKER", "JUMBO", "JUICE", "LIGHT", "LAPSE", "LIMBO", "MACHO", "MAGIC", "MEDAL", "NAIVE", "NOISY", "NORTH", "OCEAN", "OFTEN", "OMEGA", "PAINT", "PEACH", "PLACE", "QUITE", "QUACK", "QUICK", "RADIO", "RANGE", "REPLY", "SADLY", "SCARF", "SETUP", "TAKEN", "TIMER", "TOUGH", "ULTRA", "UNDER", "USING", "VALID", "VEGAN", "VOICE", "WHINE", "WAIST", "WOKEN", "YACHT", "YEAST", "YOUNG"};

	int pos, guess;

	double games = 0.0, correct = 0.0;

	String word = "";

	char playAgain = 'Y';

	char[] letters = new char [5];

	Color yellow = new Color (235, 201, 52);

	Color green = new Color (110, 186, 60);

	// All the fonts that will be used throughout the program

	Font introTitle = new Font ("Times New Roman", Font.BOLD, 96);

	Font title = new Font ("Times New Roman", Font.BOLD, 50);

	Font statisticsTitle = new Font ("Times New Roman", Font.BOLD, 25);

	Font writing = new Font ("Times New Roman", Font.PLAIN, 16);



	// Start Screen
	// This makes the background black
	c.fillRect (0, 0, 1000, 600);

	c.setColor (Color.white);

	// Draws the Title "WORDLE" in the start screen

	c.setFont (introTitle);

	c.setColor (Color.white);

	c.drawString ("WORDLE", 120, 75);

	c.setFont (writing);

	// This block of code introduces the game to the player

	c.drawString ("Hello and welcome to the amazing game called Wordle!!", 1, 100);

	c.drawString ("The game is simple! All you have to do is guess a word within 6 guesses! Sounds easy right?", 1, 125);

	c.drawString ("Here are the instructions and rules:", 1, 160);

	c.drawString ("1. As stated before, you can only have 6 attempts to guess the word!", 1, 185);

	c.drawString ("2. The answer cannot contain two or more of the same letter, therefore, you are not allowed to enter a", 1, 210);

	c.drawString ("word that has two or more of the same letter (Example. 'Digit').", 1, 225);

	c.drawString ("3. The word will never be a plural word!", 1, 250);

	c.drawString ("4. You are not allowed to delete the letters that you have typed!", 1, 275);

	c.drawString ("5. You must use CAPITAL LETTERS ONLY or else you will not be able to guess a word correctly!", 1, 300);

	c.setColor (green);

	c.drawString ("6. If a correct letter is guessed and it is in the right position, the letter will turn green.", 1, 325);

	c.setColor (yellow);

	c.drawString ("7. If a correct letter is guessed and it is not in the right position, the letter will turn yellow.", 1, 350);

	c.setColor (Color.gray);

	c.drawString ("8. If an incorrect letter is guessed, the letter will turn gray.", 1, 375);

	c.setColor (Color.white);

	c.drawString ("Enter any key when you are ready to play. Have fun!", 1, 410);

	// Clears the start screen so that the game can begin

	c.getChar ();

	c.clear ();



	// Input
	// After the first game, the game will only play again if the player wants to
	while ((playAgain == 'Y') || (playAgain == 'y'))

	    {
		// This makes the background black
		c.setColor (Color.black);

		c.fillRect (0, 63, 1000, 1000);

		games++;
		// Randomizes the word list so that the answer can be different each game
		pos = (int) (Math.random () * 68);





		// Graphics; Draws the title and the boxes that the letters will appear in

		c.setFont (title);

		c.setColor (Color.white);

		c.drawString ("WORDLE", 200, 100);



		for (int x = 175 ; x <= 395 ; x += 55)

		    {

			for (int y = 110 ; y <= 385 ; y += 55)

			    {

				c.drawRect (x, y, 50, 50);

			    }

		    }



		// Game

		for (guess = 1 ; guess <= 6 ; guess++) // This for loop ensures that the player only gets 6 guesses

		    {

			word = "";

			do // This do while loop ensures that the player does not input a word with two of the same letter and that the word has 5 letters

			    {

				for (int i = 0 ; i <= 4 ; i++) // This for loop ensures that the player inputs 5 letters as their word

				    {

					c.setCursor (1, 1);

					c.println ("                                  ");

					c.println ("                                  ");

					c.setCursor (1, 1);

					c.print ("What's your letter #" + (i + 1) + " for your word #" + guess + "? ");

					letters [i] = c.getChar ();

					word += letters [i];

					displayLetter (i, guess, word, letters);



				    }

				// This if statement only allows for the game to continue if the player inputs a word with distinct letters and a word has 5 letters
				if ((word.length () == 5) && (word.charAt (0) != word.charAt (1)) && (word.charAt (0) != word.charAt (2)) && (word.charAt (0) != word.charAt (3)) && (word.charAt (0) != word.charAt (4)) && (word.charAt (1) != word.charAt (2)) && (word.charAt (1) != word.charAt (3)) && (word.charAt (1) != word.charAt (4)) && (word.charAt (2) != word.charAt (3)) && (word.charAt (2) != word.charAt (4)) && (word.charAt (3) != word.charAt (4)))

				    {

					check (word, words, pos, guess, letters);

				    }

				//If the player's guess does not follow the requirements, the player will be able to retry his guess
				else

				    {

					word = "";



					for (int x = 175 ; x <= 395 ; x += 55)

					    {

						int y = ((guess * 55) + 55);

						c.setColor (Color.black);

						c.fillRect (x, y, 50, 50);

					    }



					for (int x = 175 ; x <= 395 ; x += 55)

					    {

						int y = ((guess * 55) + 55);

						c.setColor (Color.white);

						c.drawRect (x, y, 50, 50);

					    }

				    }

			    }

			while ((word.length () != 5) || (word.charAt (0) == word.charAt (1)) || (word.charAt (0) == word.charAt (2)) || (word.charAt (0) == word.charAt (3)) || (word.charAt (0) == word.charAt (4)) || (word.charAt (1) == word.charAt (2)) || (word.charAt (1) == word.charAt (3)) || (word.charAt (1) == word.charAt (4)) || (word.charAt (2) == word.charAt (3)) || (word.charAt (2) == word.charAt (4)) || (word.charAt (3) == word.charAt (4)));

			if (word.equals (words [pos])) // If the user guesses correctly, he/she will be asked if they want to play again

			    {

				correct++;

				do // This do while is used to ensure that the user enters a valid response

				    {

					c.setCursor (3, 1);

					c.print ("Would you like to play again (Y/N)? ");

					playAgain = c.getChar ();

				    }

				while ((playAgain != 'Y') && (playAgain != 'N') && (playAgain != 'y') && (playAgain != 'n'));

				break;

			    }

		    }

		if (guess == 7) // This block of code only executes if the user runs out of their guesses

		    {

			c.println ("The correct answer was " + words [pos]); // The correct answer will be told to the user

			do // This do while is used to ensure that the user enters a valid response

			    {

				c.setCursor (3, 1);

				c.println ("                                  ");

				c.setCursor (3, 1);

				c.print ("Would you like to play again (Y/N)? ");

				playAgain = c.getChar ();

			    }

			while ((playAgain != 'Y') && (playAgain != 'N') && (playAgain != 'y') && (playAgain != 'n'));

		    }



		if ((playAgain == 'Y') || (playAgain == 'y')) // If the user wants to play again, the screen will clear and return to the regular format

		    {

			c.clear ();

		    }

	    }

	if ((playAgain == 'N') || (playAgain == 'n')) // If the user does not want to play again, the user will be given their "game statistics" which includes the amount of games they've played, the amount they've won and their win percentage

	    {
		//This block of code creates the format for the "game statistics"
		c.clear ();

		c.setColor (Color.black);

		c.fillRect (0, 0, 1000, 600);

		c.setColor (Color.white);

		c.drawRoundRect (120, 100, 420, 300, 10, 10);



		c.setFont (statisticsTitle);

		c.drawString ("GAME STATISTICS", 225, 125);

		c.setFont (writing);

		// This block of code writes out the players statistics

		c.drawString ("Games played: " + games, 125, 160);

		c.drawString ("Games won: " + correct, 125, 185);

		c.drawString ("Win percentage: ", 125, 210);

		String winPercentage = "";

		winPercentage += Math.round ((correct / games) * 100.0); // This line of code calculates the player's win percentage

		c.drawString (winPercentage, 230, 210);

		c.drawString ("%", 255, 210);



	    }

	// Place your program here.  'c' is the output console

    } // main method





    public static void displayWord (String word, int guess)

    {
	// This method prints the entire correct word if the word has been guessed

	Font title = new Font ("Times New Roman", Font.BOLD, 50);

	c.setFont (title);



	c.setColor (Color.white);



	char let;

	for (int i = 0 ; i <= 4 ; i++) // This for loop allows the program to go through each individual letter in the word

	    {

		let = word.charAt (i);



		if ((let == 'W') || (let == 'M')) // If the letter is a 'W' or 'M', the letters will be printed out a little bit to the left of the usual position in order for them to fit in the box

		    {

			c.drawString (let + "", ((i * 55) + 177), ((guess * 55) + 100));

		    }

		else

		    {

			c.drawString (let + "", ((i * 55) + 185), ((guess * 55) + 100));

		    }

	    }

    }





    public static void check (String word, String words[], int pos, int guess, char letters[])

    {
	// This method checks each individual letter in the word to highlight the letters
	Color green = new Color (110, 186, 60);

	if (word.equals (words [pos])) // The block of code will only execute if the user guesses the word correctly

	    {

		c.println ("CORRECT!! It took you " + guess + " guesses to guess " + words [pos]);



		for (int x = 175 ; x <= 445 ; x++) // This for loop highlights all 5 boxes green to show the user that they are correct

		    {

			int y = ((guess * 55) + 55);



			c.setColor (green);

			c.drawLine (x, y, x, y + 50);



			if ((x == 225) || (x == 280) || (x == 335) || (x == 390) || (x == 445)) // This if statement is used to ensure that the spaces in between the boxes are not coloured in as well

			    {

				x += 5;

			    }

			displayWord (word, guess);

		    }



	    }

	else // This block of code will execute if the player does not guess the word correctly

	    {

		for (int i = 0 ; i <= 4 ; i++) // This for loop allows the program to go through each individual letter in the word

		    {

			if (word.charAt (i) == words [pos].charAt (i)) // This block of code will only execute if the letter in a specific position of the word guessed is the same as the letter in the same position of the correct word

			    {

				c.setColor (green);



				for (int x = ((i * 55) + 175) ; x <= ((i * 55) + 225) ; x++) // This block of code highlights that letter in green

				    {

					int y = ((guess * 55) + 55);



					c.drawLine (x, y, x, y + 50);

					delay (15);

				    }

				displayLetter (i, guess, word, letters);

			    }

		    }

		Color yellow = new Color (235, 201, 52);

		for (int i = 0 ; i <= 4 ; i++) // This for loop allows the program to go through each individual letter in the guessed word

		    {

			for (int n = 0 ; n <= 4 ; n++) // This for loop allows the program to go through each individual letter in the correct word

			    {

				if ((i == n) && (word.charAt (i) != words [pos].charAt (n))) // This block of code will execute if the positions of the guessed and correct word are not alike

				    {

					c.setColor (Color.gray);

					for (int x = ((i * 55) + 175) ; x <= ((i * 55) + 225) ; x++) // This for loop highlights those letters in gray

					    {

						int y = ((guess * 55) + 55);



						c.drawLine (x, y, x, y + 50);

						delay (15);

					    }

					displayLetter (i, guess, word, letters);

				    }

				if ((i != n) && (word.charAt (i) == words [pos].charAt (n))) // This block of code will execute if there is a letter guessed correctly, but it is in the wrong position

				    {

					c.setColor (yellow);



					for (int x = ((i * 55) + 175) ; x <= ((i * 55) + 225) ; x++) // This for loop highlights those letters in yellow

					    {

						int y = ((guess * 55) + 55);



						c.drawLine (x, y, x, y + 50);

						delay (15);

					    }



					displayLetter (i, guess, word, letters);



					break;

				    }





			    }

		    }

	    }

    }





    public static void displayLetter (int i, int guess, String word, char letters[])

    {
	// This method is very similar to "displayWord" except for the fact that this method only prints a single letter rather than the whole word
	c.setColor (Color.white);

	char letter;

	letter = letters [i];



	if ((letter == 'W') || (letter == 'M'))

	    {

		c.drawString (letter + "", ((i * 55) + 177), ((guess * 55) + 100));

	    }

	else

	    {

		c.drawString (letter + "", ((i * 55) + 185), ((guess * 55) + 100));

	    }



    }





    public static void delay (int millisecs)  // Delay Method

    {

	try

	{

	    Thread.currentThread ().sleep (millisecs);

	}





	catch (InterruptedException e)

	{

	}

    }
} // Wordle class

