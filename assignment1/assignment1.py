#Write your code here.
#Task1
def say_hello ():
    print("Hello, Sunshine!")
say_hello()
#Task2
def greet(name):
    return "Hello, "+ name + "!"
greet("Bria")
print (greet("Bria"))
#Task3
def calc(num1,num2,operation):
    if operation == "add":
        return num1+num2
    elif operation == "sub":
        return num1-num2
    elif operation == "div":
        if num2==0:
            return "Can't divide by 0!"
        return num1/num2
    elif operation == "mult":
        return num1 * num2
    elif operation == "modulo":
        return num1 % num2
    else:
        return "Invalid operation"
print (calc(70,3,"add"))
print (calc(70,3,"sub"))
print (calc(70,3,"div"))
print (calc(70,3,"mult"))
print (calc(70,3,"modulo"))
#Task4
def data_type_conversion(vaule,type):
    if type == "str":
        try: float(str)
        except Exception:
            print("You can't change a number to a word!")
        return str(vaule)
    elif type == "int":
        return int(vaule)
    elif type == "float":
        try: str(float)
        except Exception:
            print("You can't change a word to a number")
        return float(vaule)
print(data_type_conversion(3,"str"))
print(data_type_conversion(3.5,"int"))
print(data_type_conversion(387,"float"))

#Task5
def grade_scale(*args):
    try: 
        average = sum(args)/len(args)
        if average >=90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided"
print(grade_scale(83,89,97,71,70,80,69,90,94))
#Task 6
#start w/an empty string
#loop 7 times
#each loop, add original str to new str
# after loop is done, return new str

def repeat (word, count):
    new_word=""
    for i in range(count):
        new_word= new_word + word
    return new_word
print (repeat("Spongebob SquarePants",7))

#Task 7
def student_scores(choice,**kwargs):
    if choice == "best":
        high_score = 0
        best_student = ""
        for key, value in kwargs.items():
            if value > high_score:
                high_score = value
                best_student = key
            return best_student
print(student_scores("best",John=79,Amy=83,Jasmine=94))
#Task 8
def titleize (string):
    words = string.split()
    little_words = ["a","on","an","the","of","is","in"]
    for i, word in enumerate(words):
        if i == 0:
            words[i]= word.capitalize()
        elif word not in little_words:
            words[i] = word.capitalize()
    return " ".join (words)
print(titleize("boogie on down!"))

#Task 9
# two params, both str. Secret & Guess. 
# secret = unknown word
# guess = various letters that will be in this str
#if letter in str goes in str if not return _
def hangman_game(secret,guess):
    unknown_word= " "
    for letter in secret:
        if letter in guess:
            unknown_word = unknown_word + letter
        else: 
            unknown_word = unknown_word + "_" 
    return unknown_word
print(hangman_game("Pears","mnoaps"))

#Task 10
# checking three things 
# if str starts w/ vowel,consonants, or qu. 
# Depending on what it is will determine what is added to the str
def pig_latin(sentence):
    pig_word= " "
    vowels= "aieou"
    if sentence[0]in vowels:
        pig_word = pig_word+ "ay"
    elif sentence[0] not in vowels:
        pig_word = pig_word + "ay" 
    else:
        pig_word = sentence[2:] + "qu" + "ay"
print(pig_latin("One day, things will change"))