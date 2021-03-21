import pandas as pandas
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def data_loader(filepath):

    data = pd.read_csv(filepath,na_values=[' '])

    data=data.drop(['ClientID','CycleNumber','Group','MeanCycleLength','MeanMensesLength','MensesScoreDaySix', 'MensesScoreDaySeven', 'MensesScoreDayEight',
            'MensesScoreDayNine', 'MensesScoreDayTen', 'MensesScoreDay11',
            'MensesScoreDay12', 'MensesScoreDay13', 'MensesScoreDay14',
            'MensesScoreDay15', 'MeanBleedingIntensity', 'PhasesBleeding', 'IntercourseDuringUnusBleed',
            'Age', 'AgeM', 'Maristatus', 'MaristatusM', 'Yearsmarried', 'Wedding',
            'Religion', 'ReligionM', 'Ethnicity', 'EthnicityM', 'Schoolyears',
            'SchoolyearsM', 'OccupationM', 'IncomeM', 'Height', 'Weight',
            'Reprocate', 'Numberpreg', 'Livingkids', 'Miscarriages', 'Abortions',
            'Medvits', 'Medvitexplain', 'Gynosurgeries', 'LivingkidsM', 'Boys',
            'Girls', 'MedvitsM', 'MedvitexplainM', 'Urosurgeries', 'Breastfeeding',
            'Method', 'Prevmethod', 'Methoddate', 'Whychart', 'Nextpreg',
            'NextpregM', 'Spousesame', 'SpousesameM', 'Timeattemptpreg', 'BMI'], axis=1)


    return data

def dataloader_cycleLength(data):
    x = data[['CycleWithPeakorNot', 'ReproductiveCategory',
       'LengthofLutealPhase', 'FirstDayofHigh',
       'TotalNumberofHighDays', 'TotalHighPostPeak', 'TotalNumberofPeakDays',
       'TotalDaysofFertility', 'TotalFertilityFormula', 'LengthofMenses',
       'MensesScoreDayOne', 'MensesScoreDayTwo', 'MensesScoreDayThree',
       'MensesScoreDayFour', 'MensesScoreDayFive', 'TotalMensesScore',
       'NumberofDaysofIntercourse', 'IntercourseInFertileWindow',
       'UnusualBleeding']]
    y=data['LengthofCycle']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

    return x_train, x_test, y_train, y_test

def dataloader_ovulationday(data):
    x = data[['CycleWithPeakorNot', 'ReproductiveCategory',
        'LengthofLutealPhase', 'FirstDayofHigh',
        'TotalNumberofHighDays', 'TotalHighPostPeak', 'TotalNumberofPeakDays',
        'TotalDaysofFertility', 'TotalFertilityFormula', 'LengthofMenses',
        'MensesScoreDayOne', 'MensesScoreDayTwo', 'MensesScoreDayThree',
        'MensesScoreDayFour', 'MensesScoreDayFive', 'TotalMensesScore',
        'NumberofDaysofIntercourse', 'IntercourseInFertileWindow',
        'UnusualBleeding', 'LengthofCycle']]
    y=data['EstimatedDayofOvulation']
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

    return x_train, x_test, y_train, y_test

def model_dump(model, filename):
    pkl_filename = "filename"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)
    
    return True

def train_cycleLength(filepath):
    data = data_loader(filepath)
    x_train,x_test,y_train,y_test = dataloader_cycleLength(data)

    regressor = RandomForestRegressor()
    regressor.fit(x_train, y_train)
    print(regressor.score(x_test, y_test))
    model_dump(regressor, "random_forest_length_of_cycle.pkl")

    return True

def train_ovulationday(filepath):
    data = data_loader(filepath)
    x_train,x_test,y_train,y_test = dataloader_ovulationday(data)

    regressor = make_pipeline(StandardScaler(),SGDRegressor(max_iter=1000, tol=1e-3))
    regressor.fit(x_train, y_train)
    print(regressor.score(x_test, y_test))
    model_dump(regressor, "sgdRegressor_ovulationDay.pkl")

    return True


if __name__=="__main__":
    train_cycleLength("FedCycleData071012 (2).xls")
    train_ovulationday("FedCycleData071012 (2).xls")

