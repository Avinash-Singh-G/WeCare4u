# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegressionCV
page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=http%3A%2F%2Fwallpaperswide.com%2Fbeige_simple_background-wallpapers.html&psig=AOvVaw1OG-KtBHNd577BnmQECf_2&ust=1616371855992000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDfl82MwO8CFQAAAAAdAAAAABAE");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

pickle_in = open("P3.pkl","rb")
classifier=pickle.load(pickle_in)
pickle1_in = open("P4.pkl","rb")
classifier1=pickle.load(pickle1_in)

def predict_menstruation_cycle(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding):
    prediction=classifier.predict([[ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding]])
    print(prediction)
    return prediction
def predict_menstruation_cycle1(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,LengthofCycle):
    prediction1=classifier1.predict([[ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,LengthofCycle]])
    print(prediction1)
    return prediction1
def main():
    st.title("WeCare ML Web App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Menstruation Cycle Predictor </h2>
    </div>
    """
    Email = st.text_input("Email")
    date = st.text_input("Date(dd-mm-yyyy)")
    ReproductiveCategory = st.text_input("Reproductive Category")
    if st.button("Know More"):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Regular (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Long ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = Short ( < 25 days)</h3>
                        <h3 style="color:black;text-align:left;">3 = Post hormonal</h3>
                        <h3 style="color:black;text-align:left;">4 = Pill or injection</h3> 
                        <h3 style="color:black;text-align:left;">5 = Postpartum (Breastfeeding)</h3>
                        <h3 style="color:black;text-align:left;">6 = Postpartum ( Not breastfeeding)</h3>
                        <h3 style="color:black;text-align:left;">7 = Post miscarriage</h3>
                        <h3 style="color:black;text-align:left;">8 = Pre-menopausal</h3>
                        <h3 style="color:black;text-align:left;">9 = Other</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
        
    LengthofLutealPhase = st.text_input("Length of Luteal Phase")
    LengthofMenses = st.text_input("Length of Menses")
    MensesScoreDayOne = st.text_input("Menses Score Day One")
    if st.button("Know More "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Low (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Medium ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = High ( < 25 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    MensesScoreDayTwo = st.text_input("Menses Score Day Two")
    if st.button("Know More  "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Low (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Medium ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = High ( < 25 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    MensesScoreDayThree = st.text_input("Menses Score Day Three")
    if st.button("Know More   "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Low (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Medium ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = High ( < 25 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    MensesScoreDayFour = st.text_input("Menses Score Day Four")
    if st.button("Know More    "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Low (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Medium ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = High ( < 25 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    MensesScoreDayFive = st.text_input("Menses Score Day Five")
    if st.button("Know More     "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  Low (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Medium ( > 35 days)</h3>
                        <h3 style="color:black;text-align:left;">2 = High ( < 25 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    NumberofDaysofIntercourse = st.text_input("Number of Days of Intercourse")
    IntercourseInFertileWindow = st.text_input("Intercourse In Fertile Window")
    if st.button("Know More      "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  No (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Yes ( > 35 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    UnusualBleeding = st.text_input("Unusual Bleeding")
    if st.button("Know More       "):
        html_temp = """
                        
                        <div>
                        <h3 style="color:black;text-align:left;">0 =  No (25-35 days)</h3>
                        <h3 style="color:black;text-align:left;">1 = Yes ( > 35 days)</h3>
                        </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    result=""
    result1=""
    if st.button("Predict"):
        result=predict_menstruation_cycle(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding)
        result1=predict_menstruation_cycle1(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,result)
    
        st.success('The length of the cycle is {}'.format(int(result)))
        st.success('The estimated day of ovolution is {}'.format(int(result1)))
        import ics as icsneo
        import calendar
        from ics import Calendar, Event
        def date_stripper(date):
            day = date[0:2]
            month = date[3:5]
            year = date[6:10]
            return int(day),int(month),int(year)
            y1 = year
            m1 = month
            m2=int(int(m1)+1)%12
            print(calendar.month(y1, m1))
            print(calendar.month(y1, m2))
        

        def output(day, month, year, ml_output):
            day31 = [1, 3, 5, 7, 8, 10, 12]
            day30 = [4, 6, 9, 10]

            def day31f(day, month, year, ml_output):
                day += ml_output
                if day > 31:
                    day -= 31
                    month += 1
                if month > 12:
                    month = 1
                    year += 1
                return day, month, year

            def day30f(day, month, year, ml_output):
                day += ml_output
                if day > 30:
                    day -= 30
                    month += 1
                if month > 12:
                    month = 1
                    year += 1
                return day, month, year

            def feb(day, month, year, ml_output):
                day += ml_output
                if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
                    if day > 29:
                        day -= 29
                        month += 1
                    if month > 12:
                        month = 1
                        year += 1
                else:
                    if day > 28:
                        day -= 28
                        month += 1
                    if month > 12:
                        month = 1
                        year += 1
                return day, month, year

            if month in day31:
                day, month, year = day31f(day, month, year, ml_output)
            elif month in day30:
                day, month, year = day30f(day, month, year, ml_output)
            else:
                day, month, year = feb(day, month, year, ml_output)

            return day, month, year
        day,month,year = date_stripper(date)


        final_d,final_m,final_y = output(day,month,year,int(result))
        final_d,final_m = str(final_d) , str(final_m)
        if len(final_d)==1:
            final_d = "0" + final_d
        if len(final_m)==1:
            final_m = "0" + final_m
        final = str(final_y) + "-" +str(final_m) + "-" +str(final_d) + " 00:00:00"
        print(final)
        c = Calendar()
        e = Event()
        e.name = "Predicted First Day of period"
        e.begin = final
        c.events.add(e)
        c.events
        with open('my.ics', 'w') as my_file:
            my_file.writelines(c)
        import smtplib
        from email.message import EmailMessage

        EMAIL_ADDRESS ="weecaree4youu@gmail.com"
        EMAIL_PASSWORD ="glvqfnhrbcjdjsqc"

        msg = EmailMessage()
        msg['Subject'] = 'Check out Bronx as a puppy!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = Email

        msg.set_content('This is a plain text email')

        files = ['my.ics']

        for file in files:
            with open(file,'rb') as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        
        

        
 
import webbrowser

url = 'https://tripetto.app/run/85ZPL31A7Z'

if st.button('Review Form : Help us Improve'):
    webbrowser.open_new_tab(url)
        
if __name__=='__main__':
    main()
    
    
