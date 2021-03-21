from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form,IntegerField ,SubmitField,StringField, PasswordField, validators, SelectField, ValidationError, SelectMultipleField , RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo
# from flask_wtf import FlaskForm
# [['CycleWithPeakorNot', 'ReproductiveCategory',
#        'LengthofLutealPhase', 'FirstDayofHigh',
#        'TotalNumberofHighDays', 'TotalHighPostPeak', 'TotalNumberofPeakDays',
#        'TotalDaysofFertility', 'TotalFertilityFormula', 'LengthofMenses',
#        'MensesScoreDayOne', 'MensesScoreDayTwo', 'MensesScoreDayThree',
#        'MensesScoreDayFour', 'MensesScoreDayFive', 'TotalMensesScore',
#        'NumberofDaysofIntercourse', 'IntercourseInFertileWindow',
#        'UnusualBleeding']]

# class PredictForm(Form):

    # CycleWithPeakorNot = RadioField('Cycle With Peak or Not', choices = [('1','Yes'),('0','No')], validators=[DataRequired()])
    # ReproductiveCategory = RadioField('Reproductive Category', choices = [('0','Yes'),('1','No'),('2','Yes'),('9','No')],validators=[DataRequired()])
    # LengthofLutealPhase = IntegerField("Length of Luteal Phase :",validators=[DataRequired()])
    # FirstDayofHigh = IntegerField("First Day of High :",validators=[DataRequired()])
    # TotalNumberofHighDays = IntegerField("Total Number of High Days :",validators=[DataRequired()])
    # TotalHighPostPeak = RadioField('Total High Post Peak', choices = [('1','Yes'),('1','No'),('2','Yes'),('3','No'),('4','Yes'),('5','No'),('6','Yes'),('4','No')], validators=[DataRequired()])
    # TotalNumberofPeakDays = IntegerField("Total Number of Peak Days :",validators=[DataRequired()])
    # TotalDaysofFertility = IntegerField("Total Days of Fertility :",validators=[DataRequired()])
    # TotalFertilityFormula = IntegerField("Total Fertility Formula :",validators=[DataRequired()])
    # LengthofMenses = IntegerField("Length of Menses :",validators=[DataRequired()])
    # MensesScoreDayOne = RadioField('Menses Score Day One', choices = [('0','Yes'),('1','No'),('3','No')], validators=[DataRequired()])
    # MensesScoreDayTwo = RadioField('Menses Score Day Two', choices = [('0','Yes'),('1','No'),('3','No')], validators=[DataRequired()])
    # MensesScoreDayThree = RadioField('Menses Score Day Three', choices = [('0','Yes'),('1','No'),('3','No')], validators=[DataRequired()])
    # MensesScoreDayFour = RadioField('Menses Score Day Four', choices = [('0','Yes'),('1','No'),('3','No')], validators=[DataRequired()])
    # MensesScoreDayFive = RadioField('Menses Score Day Five', choices = [('0','Yes'),('1','No'),('3','No')], validators=[DataRequired()])
    # TotalMensesScore = IntegerField("Total Menses Score :",validators=[DataRequired()])
    # NumberofDaysofIntercourse = IntegerField("Number of Days of Intercourse :",validators=[DataRequired()])
    # IntercourseInFertileWindow = RadioField('Intercourse In Fertile Window', choices = [('1','Yes'),('0','No')], validators=[DataRequired()])
    # UnusualBleeding = RadioField('Unusual Bleeding', choices = [('1','Yes'),('0','No')], validators=[DataRequired()])
    
    


