
#flask app libraries 
import pickle
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request

from sklearn.preprocessing import OneHotEncoder, StandardScaler


model = model = pickle.load(open("random_forest.pkl", "rb"))
app = Flask(__name__)
app.debug = True




@app.route("/") #the home page
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        #Get Out_Day, Out_Month features 
        date_dep = request.form["Dep_Time"]
        Out_Day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Out_Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        
        #Get Dep_Hour, Dep_Min featuress
        Dep_Hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_Min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        
        
        # Get Arr_Hour, Arr_Min features 
        date_arr = request.form["Arrival_Time"]
        Arr_Hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arr_Min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        
        #Get Duration_Hours, Duration_Mins features 
        Duration_Hours =  abs(Arr_Hour - Dep_Hour)
        Duration_Mins = abs(Arr_Min - Dep_Min)
        
        #Get Total_Stops feature
        Total_Stops = int(request.form["Total_Stops"])
        
        
        #Get Out_Airline features
        Out_Airline = request.form['Out_Airline']
        
        if(Out_Airline == "AirAsia India"):
            AirAsia_India = 1
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
        
        elif(Out_Airline == "Emirates"):
            AirAsia_India = 0
            Emirates = 1
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
        
        elif(Out_Airline == "GoFirst"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 1
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
            
                    
        elif(Out_Airline == "IndiGo"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 1
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
            
        elif(Out_Airline == "KLM"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 1
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
            
        elif(Out_Airline == "Lufthansa"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 1
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
            
        elif(Out_Airline == "Multiple Airlines"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 1
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
            
        elif(Out_Airline == "Qatar Airways"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 1
            SpiceJet = 0
            Vistara = 0
            
        elif(Out_Airline == "SpiceJet"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 1
            Vistara = 0
            
        elif(Out_Airline == "Vistara"):
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 1
        
        else: # means Air India
    
            AirAsia_India = 0
            Emirates = 0
            GoFirst = 0
            IndiGo = 0
            KLM = 0
            Lufthansa = 0
            Multiple_Airlines = 0
            Qatar_Airways = 0
            SpiceJet = 0
            Vistara = 0
        
        
        #Get Out_cities feature
        Source = request.form["Out_Cities"]    ##"Out_Cities"
        if (Source == 'Bengaluru'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 1
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Mumbai'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 1
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Kolkata'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 1
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Delhi'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 1
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Jaipur'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 1
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Bhubaneswar'):
            Out_Cities_BBI = 1
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Bhopal'):
            Out_Cities_BBI = 0
            Out_Cities_BHO = 1
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Goa'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 1
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Hyderabad'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 1
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Chandigarh'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 1
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Dr. Ambedkar Nagar'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 1
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        elif (Source == 'Pune'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 1
            Out_Cities_VGA = 0
            
            
        elif (Source == 'Vijayawada'):
            
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 1
            
        else:
            Out_Cities_BBI = 0
            Out_Cities_BHO = 0
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCU = 0
            Out_Cities_DEL = 0
            Out_Cities_GOI = 0
            Out_Cities_HYD = 0
            Out_Cities_IXC = 0
            Out_Cities_JAI = 0
            Out_Cities_NAG = 0
            Out_Cities_PNQ = 0
            Out_Cities_VGA = 0
            
        
        
        #Get Return Cities features
        destination = request.form["Return_Cities"]   
        if (destination == 'Bengaluru'):
            

            Return_Cities_BLR = 1
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
        
        elif (destination == 'Mumbai'):

            Return_Cities_BLR = 0
            Return_Cities_BOM = 1
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0

        elif (destination == 'Kolkata'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 1
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
            
        elif (destination == 'Delhi'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 1
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
              
              
        elif (destination == 'Goa'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 1
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
              
        elif (destination == 'Hyderabad'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 1
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
              
        elif (destination == 'Indore'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 1
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0
              
              
        elif (destination == 'Jaipur'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 1
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0    
              
                      
              
        elif (destination == 'Lucknow'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 1
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0     
              
        elif (destination == 'Chennai'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 1
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0     
              
              
        elif (destination == 'Dr. Ambedkar Nagar'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 1
            Return_Cities_PNQ = 0   
              
              
              
        elif (destination == 'Pune'):
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 1
              
        else: #Bhubaneswar
            Return_Cities_BLR = 0
            Return_Cities_BOM = 0
            Return_Cities_CCU = 0
            Return_Cities_DEL = 0
            Return_Cities_GOI = 0
            Return_Cities_HYD = 0
            Return_Cities_IDR = 0
            Return_Cities_JAI = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_NAG = 0
            Return_Cities_PNQ = 0   
              
              
              
              
              
        #Prediction Part
        prediction = model.predict([[ Out_Day, Out_Month, Duration_Hours,
                                     Duration_Mins, Dep_Hour, Dep_Min, 
                                     Arr_Hour, Arr_Min, Total_Stops, AirAsia_India, 
                                     Emirates, GoFirst, IndiGo, KLM, 
                                     Lufthansa, Multiple_Airlines, 
                                     Qatar_Airways, 
                                     SpiceJet, Vistara, 
                                     Out_Cities_BBI, Out_Cities_BHO, 
                                     Out_Cities_BLR, Out_Cities_BOM, 
                                     Out_Cities_CCU, Out_Cities_DEL, 
                                     Out_Cities_GOI, Out_Cities_HYD, 
                                     Out_Cities_IXC, Out_Cities_JAI, 
                                     Out_Cities_NAG, Out_Cities_PNQ, 
                                     Out_Cities_VGA, Return_Cities_BLR, 
                                     Return_Cities_BOM, Return_Cities_CCU, 
                                     Return_Cities_DEL, Return_Cities_GOI, 
                                     Return_Cities_HYD, Return_Cities_IDR, 
                                     Return_Cities_JAI, Return_Cities_LKO, 
                                     Return_Cities_MAA, Return_Cities_NAG, 
                                     Return_Cities_PNQ ]])
              
        
        price = round(prediction[0][0],2)
        Month = int(prediction[0][1])
        Day = int(prediction[0][2])
        Hours = int(prediction[0][3])
        Mins = int(prediction[0][4])
    return render_template("index.html", 
                           origin="Place:- From {} to {}".format(Source,destination),
                           Out_Airline = "Prefered Airline:- {}".format(Out_Airline),
                           optimal_time = "We advise you to book ticket after {} Month {} days and {}hours with Price of Rs:-{}".format(Month,Day,Hours,price)
                           )   
              
     
              
if __name__ == "__main__":
    # app.debug = True
    app.run() 
