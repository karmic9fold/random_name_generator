import sys, random
from flask import Flask, render_template
from first_names import first as f
from last_names import last as l

app = Flask(__name__)

firstName = random.choice(f)
lastName = random.choice(l)

@app.route('/')
def index():
    # Generate a random name from the list
    firstName = random.choice(f)
    lastName = random.choice(l)
    random_name = firstName + " " + lastName
    return render_template('index.html', random_name=random_name)

if __name__ == '__main__':
    app.run(debug=True)
