import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    Result =  model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    return Result
def main():
    st.title("Diabetes Prediction")
    html_temp = """
    <div style="background-color:#02520e ;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies", "Type Here")
    Glucose  = st.text_input("Glucose","Type here")
    BloodPressure  = st.text_input("BloodPressur", "Type here")
    SkinThickness =   st.text_input("SkinThickness", "Type here")
    Insulin  = st.text_input("Insulin", "Type here")
    BMI  = st.text_input("BMI", "Type here")
    DiabetesPedigreeFunction  = st.text_input("DiabetesPedigreeFunction", "Type here")
    Age  = st.text_input("Age", "Type here")

    safe_html="""  
      <div style="background-color:#4e3ff4;padding:10px >
       <h2 style="color:white ;text-align:center;"> No Diabetes</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Yes you do have Diabetes</h2>
       </div>
    """
    if st.button("Predict"):
         output=predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
         if output == 1:
               st.markdown(danger_html,unsafe_allow_html=True)
         else:
            st.markdown(safe_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()
