# Dion Udokop
# November 4, 2024
# Minimum implementation for llama chatbot

####################################
#   TODO: import the actual Llama  #
####################################

'''
llama(): Initializes and simulates a conversational loop with the mock Llama API.

This function initializes the Llama model, sets up an initial system message, 
and starts a loop to interact with the user. It takes user input, generates 
responses from the test API, and streams these responses one token at a time. 
The loop ends when the user types "quit".
'''
def llama():
    ##########################################################
    #   TODO: copy and paste your code from lab 7            #
    ##########################################################
    
    
    #############################################################
    #   TODO: edit the initialization code for the llama API    #
    #############################################################
    
    
    #####################################################################
    #   TODO: edit your conversational loop pass the user’s input to    #
    #   the actual Llama model and display the generated response.      #                   #
    #####################################################################


    print("\n")



''' 
llamaEval() asks you to test and evaluate your chatbot. This is to be filled out after you have completed the lab. 
Once your chatbot is working according to the lab 8 description, you will use it to complete this function.

    Instructions: To ensure a deep understanding of your conversational agent's capabilities and limitations, you will 
    validate the Llama model's output for Python coding problems. This exercise will not only familiarize you with the 
    model's performance in generating code but also encourage you critically think about the results produced.
    The following questions will consist of several Python coding problems, ranging from simple to complex. 
    
    Each problem will require you to prompt your Llama model with a coding problem. You will be required to:
    a) Review the coding problem and the Llama model's solution provided by your code.
    b) Run the code to verify its functionality and Evaluation.
    c) Document your findings and reflections for each problem.
    d) Correct the code so that it better reflects the specifications of the coding problem presented.
    
    The instructions for the Code Evaluation and Correct Code strings are generally the same, just repeated for convenience.
    
    Note: You may consider updating your system message to ensure that your model is producing the best possible responses for 
    generating python code. If you do update your system message, there will be space in the experienceDiary for you to 
    indicate what your new system message is.

Complete this by inserting your answers after the colon. The llama output and corrected code are enclosed in triple quotes
to ensure that the code block just prints to the screen (and doesn't error out for not being executable in here)
'''       
def llamaEval():  
    # Q1 Llama: Prompt your conversational agent with these instructions:
    # "Write a function in Python called 'is_prime' that takes a single parameter, 'num', and returns True if 'num' is prime and False if 'num' is not prime."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q1Llama = """Q1_Llama Output: 
    
    """
    
    # Q1 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q1CE = "Q1_Code Evaluation: "
    
    # Q1 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q1CC = """Q1_Corrected Code:  
    
    """
    
    
    # Q2 Llama: Prompt your conversational agent with these instructions:
    # "Write a Python program to iterate through numbers from 1 to 100. For each number, if it is divisible by 3, print 'Fizz';"" 
    # "if it is divisible by 5, print 'Buzz'. If the number is divisible by both 3 and 5, print 'FizzBuzz'. Otherwise, print the number itself."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q2Llama = """Q2_Llama Output: 
    
    """
    
    # Q2 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q2CE = "Q2_Code Evaluation: "
    
    # Q2 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q2CC = """Q2_Corrected Code:  
    
    """
    
    # Q3 Llama: Prompt your conversational agent with these instructions:
    # "Write a function using the Python 'turtle' library called 'draw_square', which takes a single parameter called 'side_length' and"
    # "can draw a single square of any side length."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q3Llama = """Q3_Llama Output: 
    
    """
    
    # Q3 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q3CE = "Q3_Code Evaluation: "
    
    # Q3 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q3CC = """Q3_Corrected Code:  
    
    """
    
    
    # Q4 Llama: Prompt your conversational agent with these instructions:
    # "Define a function in Python called 'make_triangle' that takes a single argument, 'height', and returns a string representing a"
    # "triangle. For example, 'make_triangle(3)' will return '*\n**\n***\n**\n*\n'."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q4Llama = """Q4_Llama Output: 
    
    """
    
    # Q4 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q4CE = "Q4_Code Evaluation: "
    
    # Q4 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q4CC = """Q4_Corrected Code:  
    
    """
    
    
    # Q5 Llama: Prompt your conversational agent with these instructions:
    # "Define a function in Python that calculates the number of legs in a car. The rules are as follows:"
    # "(1) Every adult has a dog, (2) Every child has a spider."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q5Llama = """Q5_Llama Output: 
    
    """
    
    # Q5 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q5CE = "Q5_Code Evaluation: "
    
    # Q5 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q5CC = """Q5_Corrected Code:  
    
    """
    
    
    # Q6 Llama: Prompt your conversational agent with these instructions:
    # "Write a program that calculates the total cost of a group's meal, including tax and tip, using a while loop. The program should"
    # "prompt the user to enter the cost of each item until the user enters 'done'. After that, the program should ask the user for the" 
    # "tax rate and tip percentage, then calculate and print the total cost of the meal."
    # Then Select and copy the relevant part of the agent's response, typically the code snippet or explanation. 
    # Paste this into the string, making sure it includes all necessary components of the solution or explanation.
    Q6Llama = """Q6_Llama Output: 
    
    """
    
    # Q6 Code Evaluation: Test the solution that your conversational agent generated to ensure it works as expected. 
    # Execute the code using a variety of test cases, including typical cases, edge cases, and invalid input scenarios (if applicable). 
    # Finally, check if the output matches the expected results for each test case. 
    # Please report if your model was able to successfully implement the prompt. Where did your model fail in generating the code? 
    # What worked and what did not? 
    Q6CE = "Q6_Code Evaluation: "
    
    # Q6 Corrected Code: Having analyzed the code generated by the conversational agent, your next task is to modify this code so that 
    # it aligns more closely with the requirements of the initial prompt. Once all modifications are complete, test the code thoroughly 
    # to ensure it fully meets the requirements of the initial prompt. Confirm that the code is not only functional but also adheres to 
    # good coding practices and readability.
    Q6CC = """Q6_Corrected Code:  
    
    """
    
    print("\n")
    print ("Llama Chatbot Code Evaluation \n")
    print (Q1Llama, "\n", Q1CE, "\n", Q1CC, "\n\n",
           Q2Llama, "\n", Q2CE, "\n", Q2CC, "\n\n",
           Q3Llama, "\n", Q3CE, "\n", Q3CC, "\n\n",
           Q4Llama, "\n", Q4CE, "\n", Q4CC, "\n\n",
           Q5Llama, "\n", Q5CE, "\n", Q5CC, "\n\n",
           Q6Llama, "\n", Q6CE, "\n", Q6CC, "\n\n")


''' 
experienceDiary() allows you to reflect on and document your programming process.
This needs to be filled out after you have completed this lab. Once your chatbot is 
working according to the lab 8 description, you will use it to complete this function.

Complete this by inserting your answers after colon.
'''        
def experienceDiary():
    llamaEval()
    print("Reflection \n")
    
    #Q1 Did you update your system message for generating python code? If so, what is your new system message? 
    # What were the reasons for this change?.
    Q1 = "Q1: "
    
    #Q2 How accurately did the LLM interpret the initial prompt? Were there any misunderstandings or oversights? 
    # In what ways did the LLM's output differ from what you expected or needed?
    Q2 = "Q2: "
    
    #Q3 How did you identify which parts of the LLM's output were incorrect or needed improvement? 
    # What strategies did you use to analyze and understand the code generated by the LLM?
    Q3 = "Q3: "
    
    #Q4 How did you approach correcting the errors or inadequacies in the LLM's code? What challenges did you face 
    # while modifying the code, and how did you overcome them?
    Q4 = "Q4: "
    
    #Q5 To what extent do you think it is safe or reliable to depend on LLMs for coding tasks? How has this task 
    # changed your perspective on using automated tools like LLMs in programming?
    Q5 = "Q5: "
    
    #Q6 In what situations do you think LLMs can be most useful in programming? Are there scenarios where you 
    # would avoid using LLMs? What are they, and why?
    Q6 = "Q6: "
    
    #Q7 What are the ethical implications of using LLM-generated code, especially in critical or sensitive applications? 
    # How do you think one should balance the efficiency provided by LLMs with the need for accuracy and reliability?
    Q7 = "Q7: "
    
    print (Q1, "\n\n",Q2, "\n\n",Q3, "\n\n",Q4, "\n\n",Q5, "\n\n",Q6, "\n\n",Q7, "\n\n")


'''
main() runs the Llama chatbot and experience diary.
It calls the llama() to start the conversational loop and 
the experienceDiary() to print reflection responses.
'''
def main():
    llama()
    experienceDiary()


if __name__ == "__main__":
    main()
    
#END

