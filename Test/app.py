from flask import Flask, request, flash, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import joblib 
import pandas as pd
from forms import MyForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

Bootstrap(app)

@app.route('/index')
def index():
    return render_template('index.html')

"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

"""

model = joblib.load("model")
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = MyForm(request.form)
    message=''
    liste = []

    if request.method == 'POST'  :
        
        liste.append(form.Attr15.data)
        liste.append(form.Attr21.data)
        liste.append(form.Attr27.data)
        liste.append(form.Attr39.data)
        liste.append(form.Attr55.data)
        liste.append(form.Attr61.data)
        liste.append(form.year.data)
        p = model.predict(pd.DataFrame(liste))[0]
        if p == 1 :
            message = "Sorry it seems that your company go straight to bankruptcy"
        elif p == 0 : 
            message= "Your company will not go to bankruptcy"
        
        flash(message)
        return redirect(url_for('index'))
    else :

        return render_template('pred.html', form=form)

if __name__ == "__main__" : 
    print(app.url_map)
    app.run(host = "127.0.0.1", port=1000,debug=True)