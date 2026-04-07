from flask import Flask, render_template
from DataManager import DataManager

# Initialize Flask app and DataManager
app = Flask(__name__, template_folder='templates', static_folder='static')
data_manager = DataManager()

#Start Define routes
@app.route('/')
def home():
    """Display the home page with a welcome message"""
    return render_template('index.html')


@app.route('/character/<character_name>')
def get_character(character_name):
    """Display character information"""
    character_data = data_manager.Get_Character_Info(character_name)
    
    # Check if there's an error
    if isinstance(character_data, dict) and "error" in character_data:
        return render_template('error.html', error_message=character_data['error']), 404
    
    # Display character info
    return render_template('character.html', character=character_data)
#End Define routes

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
