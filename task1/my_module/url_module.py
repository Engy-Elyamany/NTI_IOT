#from webbrowser import * 
import webbrowser

sites = {
    1 : ("GitHub","https://github.com/"),
    2 : ("Google","https://www.google.com/"),
    3 : ("stackoverflow","https://stackoverflow.com/"),
    4 : ("geeksforgeeks","https://www.geeksforgeeks.org/")
}

def open_url(url):
    webbrowser.open(url)

