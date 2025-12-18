import pickle
import streamlit as st
import numpy as np
model=pickle.load(open('model.pkl','rb'))

st.title("Placement Prediction System")
CGPA=st.number_input("CGPA",min_value=0,max_value=10)
Internships=st.number_input("No of internships done",min_value=0,max_value=10)
Projects=st.number_input("No of projects done",min_value=0,max_value=20)
Workshops=st.number_input("No of Workshops/Certifications done",min_value=0)
Aptitude_Score=st.number_input("Aptitude_Score out of 100",min_value=0,max_value=100)
Soft_Skills_Rating=st.number_input("Soft_Skills_Rating out of 5",min_value=0,max_value=5)
ExtracurricularActivities=st.selectbox("ExtracurricularActivities",("Yes","No"))
PlacementTraining=st.selectbox("Placement_Training_Taken",("Yes","No"))
SSC_Marks=st.number_input("10th percentage",min_value=0,max_value=100)
HSC_Marks=st.number_input("12th percentage",min_value=0,max_value=100)

ExtracurricularActivities_val=1 if ExtracurricularActivities=="Yes" else 0
PlacementTraining_val=1 if PlacementTraining=="Yes" else 0

if st.button("Predict"):
    input_data = np.array([[CGPA,Internships,Projects,Workshops,Aptitude_Score,Soft_Skills_Rating,ExtracurricularActivities_val,PlacementTraining_val,SSC_Marks,HSC_Marks]])
    prediction = model.predict(input_data)
    if(prediction[0]==0):
        st.success("Hard Luck")
    else:
        st.success("Congratulations!!")
    # st.success(f"Prediction: {prediction[0]}")
