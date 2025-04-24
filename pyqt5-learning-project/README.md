# PyQt5 Learning Project

This project is designed to help you learn PyQt5 from scratch by building a simple application. Below are the details of the project structure and how to get started.

## Project Structure

```
pyqt5-learning-project
├── src
│   ├── main.py               # Entry point of the application
│   ├── ui
│   │   └── main_window.ui    # Qt Designer file for the main window layout
│   ├── components
│   │   └── __init__.py       # Contains reusable UI components or logic
│   └── resources
│       └── __init__.py       # Manages resources like images and icons
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd pyqt5-learning-project
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the main script to start the application:
   ```
   python src/main.py
   ```

## Usage

- The application will load the main window defined in `main_window.ui`.
- You can modify the UI using Qt Designer and convert it to a Python file using the `pyuic5` tool if needed.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

## License

This project is open-source and available under the MIT License.