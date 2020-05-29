"""Core Flask app routes."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    return render_template('index.jinja2',
                           title='Pokestat | Compare your Pokemon',
                           template='home-template',
                           body="This is a homepage served with Flask.")

    
   
@app.route('/rocket/')
def rocket():
    return render_template('rocket.jinja2',
                           template='home-template')