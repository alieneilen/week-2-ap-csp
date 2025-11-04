#abstraction is when I hide the complex details for something alot more simple. 

# a function allows us to wrap data or information into a special box or enclosure for reuse 
#define a function
# def personalInformation():
#     question1 = input ("how old are you?")
#     question2 = input ("Where do you live?")
#     question3 = input ("what school do you go to")
#     print (question1 + question2 + question3 )
#if u dont spcae them over then its outside of your function


# personalInformation()
# personalInformation()

#------------------
#make a function that guesses how old you are
def whatAge():
    q1 = int (input("when were you born?"))
    q2 = int (input("what year is it now"))
    answer= q2-q1
    result = print (f"you are {answer} years old")
whatAge()
whatAge()
