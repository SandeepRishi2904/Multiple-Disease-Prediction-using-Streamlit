import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('D:/Sandeep Rishi J B/Hackathon/Techathon/Multiple Disease Prediction System/saved models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('D:/Sandeep Rishi J B/Hackathon/Techathon/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('D:/Sandeep Rishi J B/Hackathon/Techathon/Multiple Disease Prediction System/saved models/parkinsons_model.sav','rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart-pulse-fill','person-bounding-box'],
                           default_index = 0)

#Diabetes page

if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BP Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')
        
    #for pred
    diab_diagnosis = ''
    
    #Buttons
    if st.button('Diabetes Test Result'):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_pred[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'
    st.success(diab_diagnosis)

#Heart disease page
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting BP')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    with col3:
        exang = st.text_input('Exercise induce angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels coloured by fluoroscopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
        
    #for pred
    heart_diagnosis = ''
    
    #Buttons
    if st.button('Heart Disease Test Result'):
        heart_pred = heart_disease_model.predict([[Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_pred[0] == 1):
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person does not have Heart Disease'
    st.success(heart_diagnosis)

#Parkinsons page
if(selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi (Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo (Hz)')
    with col4:
        per = st.text_input('MDVP:Jitter(%)')
    with col5:
        abss = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shim = st.text_input('MDVP:Shimmer')
    with col5:
        shimdb = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        apq = st.text_input('MDVP:APQ')
    with col4:
        dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        status = st.text_input('status')
    with col3:
        rpde = st.text_input('RPDE')
    with col4:
        dfa = st.text_input('DFA')
    with col5:
        spread1 = st.text_input('spread1')
    with col1:
        spread2 = st.text_input('spread2')
    with col2:
        d2 = st.text_input('D2')
    with col3:
        ppe = st.text_input('PPE')
        
    #for pred
    parkinsons_diagnosis = ''
    
    #Buttons
    if st.button('Heart Disease Test Result'):
        parkinsons_pred = parkinsons_model.predict([[fo,fhi,flo,per,abss,rap,ppq,ddp,shim,shimdb,apq3,apq5,apq,dda,nhr,hnr,status,rpde,dfa,spread1,spread2,d2,ppe]])
        
        if (parkinsons_pred[0] == 1):
            parkinsons_diagnosis = 'The Person has Parkinson Disease'
        else:
            parkinsons_diagnosis = 'The Person does not have Parkinsons Disease'
    st.success(parkinsons_diagnosis)
    
