#generate and solve questions randomly
#generate x amount of questions
#give score and correct answer/show solution

#q1: b10 => any other base
#q2: any other base => b10
#q3: randomB => otherRandomB

import random, settings #imports random and the file "settings"

#helper function reverse which reverses input given
def reverse(toReverse):#reverses parameter given
    a=''
    for x in toReverse:
        a = x + a
    return a



#this class generates a random question of 3 different possible types
class Question:
    def __init__(self): #initialisation
        #randomly generate b10 nr according to settings
        self.decimalNr=decimalNr=random.randint(settings.rangeMin, settings.rangeMax)
        #choose random base to calculate in (from base pool in settings)
        self.secondBase=random.choice(settings.bases)
        #this will use the function convertBase to give us the other Base Number
        self.secondBaseNr = self.convertBase(self.decimalNr, self.secondBase)


    #this function takes in a decimal number and converts it to the base specified
    def convertBase(self, decimalNr, secondBase):
        #here you decide the characters you have at your disposal specific to the base
        #this will determine the range of characters. eg: base 10 limits it from 0 to 9
        chars=settings.baseChars[0:secondBase]

        #once the check becomes less than 1 it'll have to stop the loop
        check=1
        #final result initialised to empty string
        secondBaseNr=''

        #while loop to calculate the conversion
        while check>=1:
            check=decimalNr/secondBase
            rem=decimalNr%secondBase #rest to be attached to answer
            secondBaseNr+=str(chars[rem])
            decimalNr=int(decimalNr/secondBase)
        #to get the correct answer the current string of digits needs to be reversed
        secondBaseNr=reverse(secondBaseNr) #reverses the order of the characters
        #returns the number converted to the base specified in the function
        return secondBaseNr



    #this function decides what type of question it'll generate
    def chooseQuestion(self):
        questionPool=[Question.type1, Question.type2, Question.type3]
        return random.choice(questionPool)(self)


    #this function compares the input to the correct answer and returns the marks
    def marking(self, inputAnswer, correctAnswer, marks):
        self.maxScore=marks
        if (inputAnswer==correctAnswer): #correct answer
            print("You answered correct. (+{} points)\n".format(marks))
            return marks;

        else: #wrong answer
            print("Wrong anwer (-{} points). Correct answer was: {}. \n".format(settings.deductPoints, correctAnswer))
            return -settings.deductPoints



    def type1(self): #type 1 question (base 10 to base x)
        Q1=str(input("Convert decimal number {} to {} (base {}): ".format(self.decimalNr, settings.baseDictionary[self.secondBase], self.secondBase)))
        return self.marking(Q1.lower(), (str(self.secondBaseNr).lower()), settings.marksPerQuestion[0])


    def type2(self): #type 2 question (base x to base 10)
        Q2=int(input("Convert {} (base {}) number {} to decimal: ".format(settings.baseDictionary[self.secondBase], self.secondBase, self.secondBaseNr)))
        return self.marking(Q2, self.decimalNr, settings.marksPerQuestion[1])


    def type3(self): #type 3 question (base x to base y)
        #this will make sure the 2nd random base selected will be different to the previous one selected
        thirdBase = self.secondBase
        while thirdBase == self.secondBase: #re-work this bit
            thirdBase = random.choice(settings.bases)

        #this will calculate the third base number
        thirdBaseNr = self.convertBase(self.decimalNr, thirdBase)

        #format of question
        Q3=str(input("Convert {} (base {}) number {} to {} (base {}): ".format(settings.baseDictionary[thirdBase], thirdBase, thirdBaseNr, settings.baseDictionary[self.secondBase], self.secondBase)))
        return self.marking(Q3.lower(), (str(self.secondBaseNr)).lower(), settings.marksPerQuestion[2])





#this class generates a test
class Test:
    def __init__(self): #initialisation
        finalScore=0 #score achieved by user
        possibleScore=0 #will become maxScore by the end of the test
        #the number of the test
        print("Bases Test {}".format(i))
        #other settings and details of the test
        print("You'll have {} questions to answer, current bases pool you could be asked to convert from is {}.".format(settings.nrQuestions, settings.bases))
        print("The range of numbers you will be asked to convert is between ({} and {}).".format(settings.rangeMin, settings.rangeMax))
        print("You will get {} points deducted for every wrong answer.".format(settings.deductPoints))
        print("(You can change these settings from within the settings file.)\n")
        
        #ready to start current test
        ready=input("Start test (y/n)? ")

        #if yes it generates a set of questions
        if (ready.lower()=="y"):
            for nr in range(settings.nrQuestions):
                q = Question()
                finalScore += q.chooseQuestion() #adds the marks you got per question
                possibleScore += q.maxScore #keeps adding the marks you can achieve in a question
            #final score for the test print
            print("Your final score for test {} is {} out of {}. \nPercentage: {}% \n".format(i, finalScore, possibleScore, round(max(finalScore/possibleScore*100, 0.0),1)))

        #if not then the test and program will end
        elif (ready.lower()=="n"):
            print("Test end.")
            quit()

        #otherwise, starts and asks the question again
        else:
            print("Wrong answer. Try again.")
            pass



#starting loop to keep taking tests for as long/many as you want
i=1
while True:
    #this keeps reasigning testLoop to a new Test() each loop
    testLoop=Test()
    i+=1



