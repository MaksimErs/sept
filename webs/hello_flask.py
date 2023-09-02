from flask import Flask
import book4
app = Flask(__name__)
"""@app.route('/')
def hello() -> str:
    return 'Hello word Flask'
app.run()"""

@app.route('/ook')
def do_book():
    return str(book4.search4vowels('e', 'eer'))
app.run()

