 
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/game1')
def game1():
    """Renders the first game."""
    return render_template('game1.html')

@app.route('/game2')
def game2():
    """Renders the second game."""
    return render_template('game2.html')

@app.route('/game3')
def game3():
    """Renders the third game."""
    return render_template('game3.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
