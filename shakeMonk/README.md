Goal: Generate the string "methinks it is like a weasel" by randomly generating strings.

Write a function that generates a string that is 27 characters long choosing from 26 letters and a space.

Write another function that scores each generated string by comparing the generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the string is correct we are done.  If the letters are not correct we will generate a new string.  To make it easier to follow the program's progress, this third function will print out the best string generated so far and its score every 1000 tries.

Bonus: See if you can improve the program in the self check by keeping the letters that are correct and only modifying one character in the best string so far.
