BasesTestPy
------------------------------------------------------------
My aim for this project was to make a bases test generator
that can use the parameters set by the user in the settings
file. The test has 3 different types of questions which it 
can generate and verify. The three types of questions are 
as follows:

1) base 10 -> random base 
2) random base -> base 10
3) random base -> random base 

The user is able to change the following parameters as
they wish: (from within the settings file)

* highest and lowest numbers they can be asked to convert to and from; 
* points you can achieve or lose per question; 
* the bases you can be asked to convert from; 
* the characters/symbols used in the conversion 
* the number of questions you get asked.

! If you wish for a more constrained set of bases to be 
tested on such as the fun conversions between bases 2,8 
and 16 you can change the bases array inside settings.py 
so it only contains the ones you wish to be tested on.

The tests will keep looping and giving the user their score 
for every test they complete. The download includes a zip 
consisting of two python files: settings.py and baseTest.py. 


Sample execution:
------------------------------------------------------------
```
Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
...
Bases Test 1
You'll have 8 questions to answer, current bases pool you could be asked to convert from is [2, 3, 4, 5, 6, 7, 8, 9, 16].
The range of numbers you will be asked to convert is between (32 and 512).
You will get 1 points deducted for every wrong answer.
(You can change these settings from within the settings file.)

Start test (y/n)? y
1. Convert Octal (base 8) number 740 to decimal: 480
You answered correct. (+2 points)

2. Convert Nonary (base 9) number 151 to Septenary (base 7): 127
Wrong anwer (-1 points). Correct answer was: 241.

3. Convert decimal number 209 to Hexadecimal (base 16): d1
You answered correct. (+2 points)

4. Convert Nonary (base 9) number 35 to Senary (base 6): 52
You answered correct. (+4 points)

5. Convert decimal number 350 to Quaternary (base 4): 11132
You answered correct. (+2 points)

6. Convert decimal number 42 to Binary (base 2): 101010
You answered correct. (+2 points)

7. Convert decimal number 153 to Hexadecimal (base 16): 99
You answered correct. (+2 points)

8. Convert Quinary (base 5) number 242 to Nonary (base 9): 80
You answered correct. (+4 points)

Your final score for test 1 is 17 out of 22.
Percentage: 77.3%

Bases Test 2
You'll have 8 questions to answer, current bases pool you could be asked to convert from is [2, 3, 4, 5, 6, 7, 8, 9, 16].
The range of numbers you will be asked to convert is between (32 and 512).
You will get 1 points deducted for every wrong answer.
(You can change these settings from within the settings file.)

Start test (y/n)? n
Test end.
```





