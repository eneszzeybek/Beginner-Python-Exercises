# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:53:23 2021

@author: Enes Zeybek
"""

class Question:
    def __init__(self, text, choice, answer):
        self.text = text
        self.choice = choice
        self.answer = answer
        
    def checkAnswer(self, answer):
        return self.answer == answer 
    
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print("Question", self.questionIndex + 1, ":", question.text)
        for i in question.choice:
            print("-", i)
        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            print("CORRECT!")
            self.score += 1
            self.questionIndex += 1
        else:
            print("WRONG!")
            print("Correct answer is:", question.answer)
            self.questionIndex += 1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            self.displayProgress()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):    
        print("Score:", self.score) 
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz is over!")
        else:
            print("Question", questionNumber, "of", totalQuestion)

q1 = Question("What player scored the most points in one game?", ["Wilt Chamberlain", "Michael Jordan", "Stephen Curry", "Kobe Bryant"], "Wilt Chamberlain")
q2 = Question("What player has the most career points?", ["Kareem Abdul-Jabbar", "LeBron James", "Kobe Bryant", "Michael Jordan"], "Kareem Abdul-Jabbar")
q3 = Question("Who won the most NBA Finals MVP's", ["Bill Russell", "Kobe Bryant", "Michael Jordan", "Wilt Chamberlain"], "Michael Jordan")
questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.loadQuestion()