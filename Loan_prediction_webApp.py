import streamlit as st
# from PIL import Image
import pickle
# import sklearn
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# import category_encoders as ce
def predict ():
    model = pickle.load(open('./Loan_ML_Model1.pkl', 'rb'))

    st.title("Loan Approval Predictor")

    nav = st.sidebar.radio("Navigation",["Home","Prediction"])
    #st.sidebar.title('Developers Contact - Jay Vattikuti')

    if nav == "Home":
        st.image("Loan.jpg", width=1000)
        st.markdown("<h1 style='text-align: bottom; color: Blue;'>Developer Contact - Jay Vattikuti</h1>",
                    unsafe_allow_html=True)

    if nav == "Prediction":


        ## Account No
        account_no = st.text_input('Account number')

        ## Full Name
        fn = st.text_input('Full Name')

        ## For income
        income = st.number_input("Enter your income",10000,1000000,step = 10000)

        #Age
        age=st.number_input("Enter your Age",21,60,step = 1)

        #Experience
        exp=st.number_input("Total working experience ",1,40,step = 1)

        #job details
        current_job_years=st.number_input("How many years have been working in current job",1,40,step = 1)

        ## For Marital Status
        mar_display = ('No','Yes')
        mar_options = list(range(len(mar_display)))
        mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

        # if mar == 'No':
        #     mar=1
        # else:
        #     mar=0

        ## House ownership
        House_owner_display=('rented','owned','norent_noown')
        House_options = list(range(len(House_owner_display)))
        house = st.selectbox("House ownership", House_options, format_func=lambda x: House_owner_display[x])

        # if house== 'rented':
        #     house=0
        # elif house=='owned':
        #     house=1
        # else:
        #     house=2

        #CURRENT_HOUSE_YRS
        current_house_years=st.number_input("How many years have been staying in this house ",1,40,step = 1)

        ## Car ownership
        car_display = ('No','Yes')
        car_options = list(range(len(car_display)))
        car = st.selectbox("Car ownership", car_options, format_func=lambda x: car_display[x])
        #
        # if car =='No':
        #     car=1
        # else:
        #     car=0

        # Profession
        profession = st.text_input('Profession')
        # count_encoder = ce.CountEncoder()
        # count_encoded = count_encoder.fit_transform(profession)

        #CITY
        city = st.text_input('City')

        #STATE
        state = st.text_input('STATE')


        features = [[income,age,exp, mar,house,car,profession,city,state,current_job_years,current_house_years]]

        #print (features)


        if st.button("Predict"):
            print(features)
            features[0][6] = 1
            features[0][7] = 1
            features[0][8] = 1


            prediction = model.predict(features)
            lc = [str(i) for i in prediction]
            ans = int("".join(lc))
            if ans == 0:
                st.error(
                "According to our Calculations, Customer " + fn + ", Account number: " + account_no + " may be a Defaulter of the loan "
                )
            else:
                st.success(
                # "Hello: " + fn + " || "
                # "Account number: " + account_no + ' || '
                # 'Congratulations!! you will get the loan from Bank'
                "According to our Calculations, Customer " + fn + ", Account number: " + account_no + " is a good customer for the loan  "
                )











