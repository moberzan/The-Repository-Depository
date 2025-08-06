import webbrowser
import os

# Open the HTML file in the default browser
file_path = os.path.abspath("General Kenobi/index.html")
webbrowser.open(f"file://{file_path}")
