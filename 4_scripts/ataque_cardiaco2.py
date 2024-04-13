!pip install scikit-learn
!pip install pandas

import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# carregando dados
df = pd.read_csv('../heart.csv')
df['Sex'] = df['Sex'].replace({'F': 0, 'M': 1})

#Titulo do Site
st.title("Previsão de Ataque Cárdiaco")

#Sub-titulo
st.subheader("Informações dos dados")


#Usuario escreve o nome
user_input = st.sidebar.text_input("Digite seu nome")
#Printando o nome do usuário
st.write("Paciente:", user_input)


#Criando função para coletar os dados do paciente
def get_user_data():
    # Input Idade
    age = st.sidebar.number_input("Idade", 18, 100, 25)

    #Input Sexo
    sex_options = {"Masculino": "M", "Feminino": "F"}
    sex = st.sidebar.radio("Sexo", list(sex_options.keys()))

    #Input Tipo de Dor no Peito
    chest_pain_type_options = {"Angina típica": "TA", "Angina típica": "ATA",
                               "Dor não anginosa": "NAP", "Assintomática": "ASY"}
    chest_pain_type = st.sidebar.radio("Tipo de Dor no Peito", list(chest_pain_type_options.keys()))

    #Input Pressão Arterial em Repouso
    resting_blood_pressure = st.sidebar.number_input("Pressão Arterial em Repouso", 0, 350, 120)

    #Input Colesterol
    cholesterol = st.sidebar.number_input('Colesterol', 0, 700, 200)

    #Input Glicemia em Jejum
    fasting_blood_sugar_options = {"Sim": 1, "Não": 0}
    fasting_blood_sugar = st.sidebar.radio("Glicemia em Jejum >120 mg ?", list(fasting_blood_sugar_options.keys()))

    #Input Eletrcardiograma
    resting_ecg_options = {"Normal": "Normal", "Com anormalidade das ondas(ST)": "ST",
                           "Mostrando Hipertrofia Ventricular(LVH)": "LVH"}
    resting_ecg = st.sidebar.radio("Resultado Eletrocardiograma em Repouso", list(resting_ecg_options.keys()))

    #Input Frequencia Max Cardiaca
    max_heart_rate_achieved = st.sidebar.number_input('Qual foi a frequência cardíaca maxima alcançada ?', 0, 300, 150)

    # Input Exercicio Induz Angina
    exercise_induced_angina_options = {"Sim": 1, "Não": 0}
    exercise_induced_angina = st.sidebar.radio("O exercicio induz a angina ?", list(exercise_induced_angina_options.keys()))

    #Input ST Depression
    st_depression = st.sidebar.number_input('Depressao ECG', -50, 100, 0)

    #Input ST SLpe
    st_slope_options = {"Up": "Up", "Flat": "Flat", "Down": "Down"}
    st_slope = st.sidebar.radio("Inclinação do Eletrocardiograma", list(st_slope_options.keys()))

    # Criando dicionario de dados
    user_data = {
        'Age': age,
        'Sex': sex,
        'ChestPainType': chest_pain_type,
        'RestingBloodPressure': resting_blood_pressure,
        'Cholesterol': cholesterol,
        'FastingBloodSugar': fasting_blood_sugar,
        'RestingECG': resting_ecg,
        'MaxHeartRateAchieved': max_heart_rate_achieved,
        'ExerciseInducedAngina': exercise_induced_angina,
        'STDepression': st_depression,
        'STSlope': st_slope
    }

    # Convertendo Dicionario em Dataframe
    user_data_df = pd.DataFrame(user_data, index=[0])

    return user_data_df

#treinando modelos

# user_input_variables = get_user_data()

# x = df.drop(columns =['HeartDisease','ChestPainType','RestingECG',
#                         'ExerciseAngina','ST_Slope'],axis=1)

# y = df['HeartDisease']

# x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2)

# dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3)

# dtc.fit(x_train, y_train)

# #acurácia do modelo

# st.subheader('Acurácia do modelo')

# st.write(accuracy_score(y_test, dtc.predict(x_text))*100)


# #previsão
# prediction = dtc.predict(user_input_variables)

# st.subheader('Previsão:')

# st.write(prediction)

# st.write(prediction)

# Transformando funcao get_user_data em variavel
user_data = get_user_data()

# Plotando grafico
chart = st.bar_chart(user_data)
