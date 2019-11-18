from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True


rotate_form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="rotate_form" method="post">
        <label for="rot"><em>Rotate by:</em></label>
        <input type="text" id="rot" name="rot"value='0'/>
        <br>
        <textarea id='text' name="text">{0}</textarea>
        <br><input type="submit" value="Submit Query"/>



      </form>
    </body>
</html>
"""

@app.route("/rotate_form",methods=['POST'])
def encrypts():

    text_str = request.form['text']
    rotate = request.form['rot']
    new_text= encrypt(text_str,rotate)
    return rotate_form.format(new_text)
@app.route('/')
def index():
    return rotate_form.format('')
app.run()