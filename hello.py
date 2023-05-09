print("hello World")


for x in range(3):
    print ("hello world for loop")
    
    
phrase = "This is what I want to print"
number_of_times = 10

def print_text_x_times(text:str, number_of_times:int):
    for x in range(number_of_times):
        print (text)
        
        
print_text_x_times(phrase, number_of_times)