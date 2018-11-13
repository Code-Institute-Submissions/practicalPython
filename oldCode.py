import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

user_answers = []
riddles_dict = []
riddles = []
answers = []

# Accessing the riddles to pick questions and answers

with open('data/riddles.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)
        
        
# function to bring the riddles and answers into a list to compare the guess answer
# and give score, storing the answer if is wrong to print back

def ask_riddle():
    number_of_riddles = len(riddles)
    riddles_and_answers = zip(riddles, answers)
    riddles_list = list(riddles_and_answers)
    
    
    score = 0
    
    for riddle, answer in riddles_list:
        guess_answer = input(riddle+"\n" + '>>')
        if guess_answer == answer:
            score += 1
            print('Right!')
        else:
            user_answers.append(guess_answer)
            print('Wrong! ' + 'the answer is >> ' + answer)
        print(' you got {0} correct out of {1}'.format(score, number_of_riddles))
        

@app.route('/', methods=["GET", "POST"])
def index():
    # main page 
    #handle post request
    if request.method == "POST":
        return render_template("index.html")
    
    
# need to store the names here 
player_list = []
def create_player_list(username):
    player_list.append(username)
    print(player_list)

@app.route('/game')
def user():
    username_list = []
    if request.method == "POST":
        create_player_list(request.form['username'])
    return render_template("game.html", username_list=username_list)
    


#create_player_list('kim')
#print(player_list)
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)