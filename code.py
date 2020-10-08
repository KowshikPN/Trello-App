'''
Name: Kowshik Prasad Navilur
Synopsis: This program creates a card on the Trello Board. Labels and Comments can be added to the Card.
This program has 7 commands in order to perform the task namely 
a) create-board b) create-list c)get-lists-from-board d) create-card
e) get-cards-from-list f) create-label-card g)add-comment.

'''

import requests
import click
import configparser

def get_tokens():
    try:
        config = configparser.ConfigParser()
        config.read('Access.properties')
        key = config.get("ACCESS", "KEY").replace("'","")
        token = config.get("ACCESS", "TOKEN").replace("'","")
        return [key, token]
    except:
        click.echo("Failed to read Config Properties..")        


@click.group()
def main():
    """
    Simple cli program to create cards on the Trello board.\n
    Labels and Comments can be added to the card created.\n

    Steps:\n
    i) Store the KEY and TOKEN in the Access.properties file.\n
    1. Create the Board.\n
        - Use Command: create-board\n
    2. Create new List.\n
        - Use Command: create-list\n
                (OR)\n
       Get the Lists from the Board.\n
       (Default: 3 Lists will be created namely To Do, Doing, Done).\n
       - Use Command: get-lists-from-board\n
    3. Create Card.\n
        - Use Command: create-card\n
    4. Create Label for the card.\n
        - Use command: create-label-card\n
    5. Add Comment to the card.\n
        - Use command: add-comment\n

    Note: Use --help for usage of commands.\n
    """
    pass

@click.command()
@click.argument('board_name')
def create_board(board_name):
    """ To create a board in Trello with BOARD_NAME
    
    BOARD_NAME : Name of the board to be created.
    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/boards/"
        querystring = {"name": board_name, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        if(response.status_code == 200):
            board_id = response.json()['id']
            click.echo("Board Created Successfully !!")
            click.echo("Board ID")
            click.echo(board_id)
        else:
            click.echo("Failed to create the board..")
    except:
        click.echo("Failed to get the API Keys and Tokens or Failed to create the board..")

main.add_command(create_board)


@click.command()
@click.argument('board_id')
def get_lists_from_board(board_id):
    """
    Enter the BOARD_ID to get the lists available

        BOARD_ID is required to get the available Lists.
        To create a new board enter the create_new_board command.

    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/boards/"+board_id+"/lists"
        querystring = {"key": key, "token": token, "id": board_id}
        response = requests.request("GET", url, params=querystring)
        result = response.json()
        lists_in_board = {}
        for lists in result:
            for k,v in lists.items():
                if k == 'id':
                    id = v
                if k == 'name':
                    lists_in_board[id] = v
        for k,v in lists_in_board.items():
            click.echo("LIST ID :")
            click.echo(k)
            click.echo("LIST NAME :")
            click.echo(v)
    except:
        click.echo("Failed to get the API Keys and Tokens or Failed to get lists from board..")        

main.add_command(get_lists_from_board)

@click.command()
@click.argument('board_id')
@click.argument('list_name')
def create_list(board_id, list_name):
    """ To create a list in the board\n
        Takes 2 arguments: a) Board ID b) List Name to be created on the board.\n
     """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/boards/"+board_id+"/lists"
        querystring = {"name": list_name, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        list_id = response.json()["id"]
        if(response.status_code == 200):
            click.echo("List created successfully on the board")
            click.echo("LIST ID :")
            click.echo(list_id)
        else:
            click.echo("List Not Created on the board")
    except:
        click.echo("Failed to get the API Keys and Tokens or List Not Created on the board..")

main.add_command(create_list)

@click.command()
@click.argument('list_id')
@click.argument('card_name')
def create_card(list_id, card_name):
    """
    To Create a Card on the Specified List.\n
    Requires 2 arguments:\n
    a) List_ID: Can be Obtained from get-lists-from-board command.\n
    b) CARD_NAME\n

    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/cards"
        querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        card_id = response.json()["id"]
        if(response.status_code == 200):
            click.echo("Card Created successfully !!")
            click.echo("CARD_ID: ")
            click.echo(card_id)
        else:
            click.echo("Failed to create the card..")
    except:
        click.echo("Failed to get the API Keys and Tokens or Failed to create the card..")

main.add_command(create_card)


@click.command()
@click.argument('list_id')
def get_cards_from_list(list_id):
    """
    To Get the Cards details from the List Provided.\n
    Required 1 parameter: LIST_ID : ID of the List.

    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/lists/"+list_id+"/cards"
        querystring = {"key": key, "token": token, "id": list_id}
        response = requests.request("GET", url, params=querystring)
        if(response.status_code == 200):
            card_data = response.json()
            click.echo("-----CARD DATA-----")
            for details in card_data:
                for k,v in details.items():
                    if(k == "id"):
                        click.echo("CARD ID :")
                        click.echo(v)
                    if(k == "name"):
                        click.echo("CARD NAME")
                        click.echo(v)
        else:
            click.echo("Failed to get the Cards..")
    except:
        click.echo("Failed to get Cards from List provided or Failed to get the Cards..")

main.add_command(get_cards_from_list)

@click.command()
@click.argument('card_id')
@click.argument('label_name')
@click.argument('color_name',type=str)
def create_label_card(card_id, label_name, color_name):
    """
    To Create a Label to the Card.\n
    Required 3 arguments:\n
    a) CARD_ID: ID of the card.\n
    b) LABEL_NAME: name for the label.\n
    c) COLOR_NAME: Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime\n
    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        color_sets = {"yellow", "purple", "blue", "red", "green", "orange", "black", "sky", "pink","lime"}

        if(color_name not in color_sets):
            color_name = None

        url =  "https://api.trello.com/1/cards/"+card_id+"/labels"
        querystring = {"key": key, "token": token, "color": color_name,"id": card_id, "name": label_name}
        response = requests.request("POST", url, params=querystring)
        if(response.status_code == 200 and color_name == None):
            click.echo("Label Created successfully for the card !!")
            click.echo("Label with no color created..")
        elif(response.status_code == 200 and color_name != None):
            click.echo("Label Created successfully for the card !!")
        else:
            click.echo("Failed to create label for the card..")
    except:
        click.echo("Failed to get the API Keys and Tokens or Failed to create label for the card..")

main.add_command(create_label_card)


@click.command()
@click.argument('comment')
@click.argument('card_id')
def add_comment(comment, card_id):
    """
    To add comment to the Card.\n
    Takes 2 arguments:\n
    a) COMMENT: comment text that needs to be added to the card.\n
    b) CARD_ID: ID of  the card for which comment needs to be added.\n

    """
    out = get_tokens()
    try:
        key = out[0]
        token = out[1]
        url = "https://api.trello.com/1/cards/"+card_id+"/actions/comments"
        querystring = {"key": key, "token": token, "text": comment,"id": card_id}
        response = requests.request("POST", url, params=querystring)
        if(response.status_code == 200):
            click.echo("Comment added to the card successfully !!")
        else:
            click.echo("Failed to add the comment..")

    except:
        click.echo("Failed to get the API Keys and Tokens or Failed to add the comment..")

    

main.add_command(add_comment)

if __name__ == "__main__":
    main()
