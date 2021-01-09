from wtforms.validators import DataRequired, InputRequired
from wtforms import Form, FloatField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from flask import Flask, request, flash, render_template, redirect, url_for





class MyForm(FlaskForm):
    year = IntegerField("year", validators= [ DataRequired()])
    Attr61 = FloatField("sales / receivables", validators=[ DataRequired()])
    Attr55 = FloatField("working capital", validators=[ DataRequired()])
    Attr39 = FloatField("profit on sales / sales", validators=[ DataRequired()])
    Attr27 = FloatField("profit on operating activities / financial expenses", validators=[ DataRequired()])
    Attr21 = FloatField("sales (n) / sales (n-1)", validators=[ DataRequired()])
    Attr15 = FloatField("(total liabilities * 365) / (gross profit + depreciation)", validators=[ InputRequired()])

    submit = SubmitField("Submit")

    def validate_on_submit(self) : 
        if request.method == 'POST' and self.validate() : 
            return True
        return False