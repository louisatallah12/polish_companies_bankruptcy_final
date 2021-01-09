from wtforms.validators import DataRequired, InputRequired
from wtforms import Form, FloatField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from flask import Flask, request, flash, render_template, redirect, url_for





class MyForm(FlaskForm):
    year = IntegerField("year", validators= [ DataRequired()])
    Attr63 = FloatField("sales / short-term liabilities", validators=[ DataRequired()])
    Attr46 = FloatField("(current assets - inventory) / short-term liabilities", validators=[ DataRequired()])
    Attr40 = FloatField("(current assets - inventory - receivables) / short-term liabilities", validators=[ DataRequired()])
    Attr33 = FloatField("operating expenses / short-term liabilities", validators=[ DataRequired()])
    Attr25 = FloatField("(equity - share capital) / total assets", validators=[ DataRequired()])
    Attr16 = FloatField("(gross profit + depreciation) / total liabilities", validators=[ InputRequired()])

    submit = SubmitField("Submit")

    def validate_on_submit(self) : 
        if request.method == 'POST' and self.validate() : 
            return True
        return False