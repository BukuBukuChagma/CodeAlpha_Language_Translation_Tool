# Language Translation Tool

A modern web application that provides real-time language translation using Google Translate API. Built with Flask backend and vanilla JavaScript frontend, this tool offers a clean, user-friendly interface for translating text between multiple languages.

![Language Translator Screenshot](/frontend/frontend_screenshot.png)

## Features

- **Real-time Language Detection**: Automatically detects the source language
- **Multiple Language Support**: Translate between numerous languages including:
  - English
  - Spanish
  - French
  - German
  - Italian
  - Portuguese
  - Russian
  - Japanese
  - Korean
  - Chinese (Simplified)
  - Arabic
  - Hindi
- **Intuitive Interface**:
  - Clean, modern design
  - Responsive layout for all devices
  - Easy-to-use language selection
- **Additional Features**:
  - Copy translation to clipboard
  - Clear text fields
  - Swap languages

## Technologies Used

### Backend
- **Python 3.x**
- **Flask**: Web framework
- **googletrans**: Google Translate API wrapper
- **flask-cors**: Cross-Origin Resource Sharing support

### Frontend
- **HTML5**
- **CSS3**: Modern styling with Flexbox
- **JavaScript**: Vanilla JS for API interactions
- **Font Awesome**: Icons

### Testing
- **unittest**: Python testing framework

## Project Structure
```
language-translator/
├── frontend/
│   ├── index.html                     # Main HTML file
│   ├── style.css                      # Styling
|   ├── script.js                      # Frotnend logic
│   └── frontend_screenshot.png        # Frontend Interface Screenshot
|   
├── app.py                             # Flask application
├── translate.py                       # Translation service
├── test_app.py                        # Backend tests
├── requirements.txt                   # Python dependencies
├── demo.mp4                           # Demo video of tool in working
└── README.md                          # Documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BukuBukuChagma/CodeAlpha_Language_Translation_Tool.git
   cd CodeAlpha_Language_Translation_Tool
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Unix/MacOS
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:{PORT}
   ```

3. To translate text:
   - Enter text in the left text area
   - Select source and target languages (or use auto-detect)
   - Click "Translate" button
   - Translation appears in the right text area

4. Additional features:
   - Click the swap button (↔️) to switch languages
   - Click the copy button (📋) to copy translation
   - Click the clear button (✖️) to reset both fields

## Testing

Run the backend tests:
```bash
python -m unittest test_app.py -v
```

## API Endpoints

- `GET /`: Serves the main application
- `POST /api/detect`: Detects language of input text
- `POST /api/translate`: Translates text between languages

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Known Limitations

- Relies on Google Translate API
- Character limit based on Google Translate restrictions
- Internet connection required

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
