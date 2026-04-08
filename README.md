# WebDragonBall - Dragon Ball Character Encyclopedia

A Flask-based web application that displays information about Dragon Ball characters using the Dragon Ball API.

## Overview

WebDragonBall is a simple yet powerful web application that allows users to search for and view detailed information about Dragon Ball characters. The application fetches real-time data from the [Dragon Ball API](https://dragonball-api.com/) and presents it in an intuitive web interface.

## Features

- **Character Search**: Search for any Dragon Ball character by name
- **Character Details**: View comprehensive information including:
  - Ki and Max Ki levels
  - Race and gender
  - Character description
  - Origin planet and transformations
  - Character image
- **Responsive UI**: Clean and user-friendly interface
- **Real-time Data**: Fetches current data from the Dragon Ball API

## Project Structure

```
WebDragonBall/
├── main.py                 # Flask application entry point
├── CharacterData.py        # Pydantic models for character data
├── DataManager.py          # Data fetching and management from API
├── requirements.txt        # Python dependencies
├── static/
│   └── styles.css         # CSS styling
└── templates/
    ├── index.html         # Home page
    ├── character.html     # Character details page
    └── error.html         # Error page
```

## Requirements

- Python 3.8+
- Flask
- Pydantic
- Requests

## Installation

1. **Clone or download the project**
   ```bash
   cd WebDragonBall
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Open in browser**
   - Navigate to `http://localhost:5000` in your web browser

3. **Search for characters by name (In spanish)**
   - Use the search functionality to look up Dragon Ball characters
   - View detailed information about selected characters

## API Reference

The application uses the [Dragon Ball API](https://dragonball-api.com/api/characters) to fetch character data.

### Example Character Query
```
https://dragonball-api.com/api/characters?name=Goku
```

## Architecture

### Main Components

- **Flask Routes**
  - `/` - Home page
  - `/character/<character_name>` - Character details page

- **Data Models (CharacterData.py)**
  - `Character` - Main character model
  - `OriginPlanet` - Character's origin planet information
  - `Transformation` - Character transformation information

- **DataManager (DataManager.py)**
  - Handles API requests
  - Validates data using Pydantic models
  - Manages error handling

## Error Handling

The application handles various error scenarios:
- Character not found (404 error page)
- API connection errors
- Data validation errors

## Development

To run the application in debug mode with automatic reloading:
```bash
python main.py
```

The application will run on `http://0.0.0.0:5000` with debug mode enabled.

## Dependencies

- **Flask**: Web framework for building the application
- **Pydantic**: Data validation and settings management
- **Requests**: HTTP library for API calls

## Future Enhancements

Potential improvements for the project:
- Database caching for improved performance
- Advanced filtering and sorting options
- Character comparison feature
- Favorites/bookmark functionality
- Multi-language support

## License

This project is open source and available under the MIT License.

## Credits

- Data provided by [Dragon Ball API](https://dragonball-api.com/)
- Built with Flask, Pydantic, and Requests

---

**Last Updated**: April 2026
