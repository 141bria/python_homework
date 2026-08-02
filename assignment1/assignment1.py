#Write your code here.
#Task1
def hello ():
    return 'Hello!'
hello()
#Task2
def greet(name):
    return "Hello, "+ name + "!"
greet("Bria")
print (greet("Bria"))
#Task3
def calc(num1,num2,operation):
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1-num2
    elif operation == "divide":
        try:
            return num1/num2
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "multipliy":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "modulo":
        return num1 % num2
    elif operation == "int_divide":
        try:
            return num1//num2
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "power":
        return num1**num2
    else:
        return "Invalid operation"
print (calc(70,3,"add"))
print (calc(70,3,"subtract"))
print (calc(70,3,"divide"))
print (calc(70,3,"multipliy"))
print (calc(70,3,"modulo"))
print (calc(70,3,"int_divide"))
print (calc(70,3,"power"))
#Task4
def data_type_conversion(value,type_name):
    if type_name == "str":
        try: str(value)
        except Exception:
            return f"You can't convert {value} into a {type_name}."
        return str(value)
    elif type_name == "int":
        try: int(value)
        except Exception:
            return f"You can't convert {value} into a {type_name}."     
        return int(value)
    elif type_name == "float":
        try: float(value)
        except Exception:
            return f"You can't convert {value} into a {type_name}."
        return float(value)
print(data_type_conversion(3,"str"))
print(data_type_conversion(3.5,"int"))
print(data_type_conversion(387,"float"))

#Task5
def grade(*args):
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
    except TypeError:
        return "Invalid data was provided."
print(grade(83,89,97,71,70,80,69,90,94))
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
    elif choice == "mean":
        average = sum(kwargs.values())/len(kwargs.values())
        return average
print(student_scores("best",John=79,Amy=83,Jasmine=94))
#Task 8
def titleize (string):
    words = string.split()
    little_words = ["a","on","an","the","of","is","in","and"]
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
def hangman(secret,guess):
    unknown_word= ""
    for letter in secret:
        if letter in guess:
            unknown_word = unknown_word + letter
        else: 
            unknown_word = unknown_word + "_" 
    return unknown_word
print(hangman("Pears","mnoaps"))

#Task 10
# checking three things 
# if str starts w/ vowel,consonants, or qu. 
# Depending on what it is will determine what is added to the str
def pig_latin(sentence):
    pig_words =[]
    vowels= "aeiou"
    words = sentence.split()
    for word in words:
        if word[0]in vowels:
            pig_words.append(word+ "ay")
        elif word.startswith("qu"):
            pig_words.append(word[2:]+"quay")
        else:
            i=0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i +=1
            pig_words.append(word[i:]+word[:i]+"ay")
    return " ".join(pig_words)
print(pig_latin("apple"))
print(pig_latin("queen"))
print(pig_latin("squeal"))
print(pig_latin("school"))