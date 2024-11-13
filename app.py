import streamlit as st
import pickle

model = pickle.load(open('span.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

st.title("Email spam Classification Application")
st.write("this is a Machine Learning application to classify emails as spam or harm.")
user_input=st.text_area("Enter an email to classify",height=150)
if st.button("classify"):
    if user_input :
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
        if pred[0] == 0:
            #st.writer("this email is not spam")
            st.success("this email is not spam")
        else:
            st.error("this is spam email")
    else:
        print("please type email")