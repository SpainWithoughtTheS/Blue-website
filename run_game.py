from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Generate a random correct answer between 1 and 100
correct_answer = random.randint(1, 100)

@app.route('/check_guess', methods=['GET'])
def check_guess():
    try:
        # Get the 'guess' parameter from the query
        user_guess = int(request.args.get('guess', 0))

        # Check if the guess is correct
        if user_guess == correct_answer:
            alert = 'Congratulations! You guessed the correct number.'
        elif user_guess < correct_answer:
            alert = 'Try a higher number.'
        else:
            alert = 'Try a lower number.'

        return feedback
    except ValueError:
        return 'Invalid guess. Please enter a number.'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
