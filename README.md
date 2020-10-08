# Trello-App
This Application creates a card on the Trello Board. Labels and Comments can be added to the Card. 

STEPS:

# Step1: Run the following command to install the dependencies.
    - $pip install -r requirements.txt
    
# Step2: Provide your Access Key and Access token in the Access.properties file under ACCESS header.
    - Ex: [ACCESS]
            KEY = 0471642aefef5fa1fa76530ce1ba4c85
            TOKEN = 9eb76d9a9d02b8dd40c2f3e5df18556c831d4d1fadbe2c45f8310e6c93b5c548
            
    - To generate your API TOKEN, go to URL: https://trello.com/app-key
    
    - Note: The above key and token are taken from official trello developer page.

# Step3: Execute the source code file.
    - $python code.py --help
        - Provides the help page on how to execute the commands.

# Scenario: 
CLI program with Python to add a card to a trello.com board. This program should take user input to add a Trello card with labels and a comment to the specified column of board.
 
 Steps to Perform the above the Scenario: 
 
    1. Create the Board.
        - Use Command: $ python code.py create-board <BOARD_NAME>
        Output will be the Board_ID of the board created. Please copy the board id as you need it to create the list.
    
    2. Create new List or use the default lists.
        - Use Command: $python code.py create-list <BOARD_ID> <LIST_NAME>
                (OR)
       Get the Lists from the Board.
       (Default: 3 Lists will be created namely To Do, Doing, Done).
       - Use Command: $python code.py get-lists-from-board <BOARD_ID>
       Output will be the List_ID of the lists available on the board. Please copy the List_ID as you need it to create the cards on the list.

    3. Create Card.
        - Use Command: $python code.py create-card  <LIST_ID> <CARD_NAME>
        Output will be the CARD_ID of the card created. Please copy the CARD_ID as you need it to create labels for the card.

    4. Create Label for the card.
        - Use command: $python code.py create-label-card <CARD_ID> <LABEL_NAME> <COLOR_NAME>
        - Valid Values for COLOR_NAME: {yellow, purple, blue, red, green, orange, black, sky, pink, lime}
        Output will be ERROR/SUCCESS message.
        
    5. Get the Cards from the specified List.
        - Use Command: $python code.py get-cards-from-list <LIST_ID>
        Output will be CARD_ID and CARD_NAME available on the specified List.

    5. Add Comment to the card.
        - Use command: $python code.py add-comment <CARD_ID>
        Output will be SUCCESS/ERROR message.

    Note: Use --help for usage of commands.
    
    To check the output:
    1. Go to URL: https://trello.com/login
    2. Login to the website.
    3. View the output.
    
   Future Development Work:
   
    1. Delete the Card.
    2. Update the Card.
    3. Delete a label from the Card.
    4. Get the details of the all the boards available in the account.

