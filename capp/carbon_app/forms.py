from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange

# class BusForm(FlaskForm):
#   kms = FloatField('Kilometers', [InputRequired()])
#   fuel_type = SelectField('Type of Fuel', [InputRequired()], 
#     choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
#   submit = SubmitField('Submit')

class BusForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('CNG', 'CNG'),
        ('Electric/Hydrogen', 'Electric/Hydrogen')])
    submit = SubmitField('Submit')

class CarForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')])
    passengers = IntegerField('Number of passengers (including you)', 
        validators=[InputRequired(), NumberRange(min=1, max=8, message="Between 1 and 8 passengers")],
        default=1)
    submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Flight class', choices=[
        ('Economy', 'Economy'),
        ('Business Class', 'Business Class')])
    submit = SubmitField('Submit')

class TrainForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Electric', 'Electric')])
    submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  
