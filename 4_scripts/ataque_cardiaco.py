import pandas as pd
import streamlit as st

df = pd.read_csv('../heart.csv')

#Titulo do Site
st.title("Previsão de Ataque Cárdiaco")

#Sub-titulo
st.subheader("Informações dos dados")

#User insere o nome
user_input = st.sidebar.text_input("Digite seu nome")

#escrevendo o nome do usuário
st.write("Paciente:", user_input)


#dados de entrada
# x = df.drop(['HeartDisease'])

# #variavel resposta
# y = df['HeartDisease']


#separando base


#Essa função coleta os dados do paciente
def get_user_date():

    #Input de Idade
    idade = st.sidebar.number_input('Idade',18,100)

    #Input de Sexo
    sexo_opcoes = {"Masculino": "M","Feminino": "F"}
    sexo = st.sidebar.radio("Sexo", list(sexo_opcoes.keys()))

    #Input Tipo de Dor no Peito
    tipo_dor_peito_opcoes = {"Angina típica": "TA","Angina típica":"ATA",
                              "Dor não anginosa":"NAP", "Assintomática":"ASY"}
    tipo_dor_peito = st.sidebar.radio ("Tipo de Dor no Peito",list(tipo_dor_peito_opcoes.keys()))
    
    #Input Pressão Arterial em Repouso
    pa_repouso = st.sidebar.number_input("Pressão Arterial em Repouso",0,350,1)

    #Input de Colesterol
    colesterol = st.sidebar.number_input('Colesterol',0,700)

    #Input Glicemia em Jejum
    glicemia_opcoes = {"Sim": 1,"Não": 0}
    glicemia_jejum = st.sidebar.radio("Glicemia em Jejum >120 mg ?", list(glicemia_opcoes.keys()))

    #Input resultado Eletrocardiograma em Repouso
    eletrocardiograma_opcoes = {"Normal": "Normal","Com anormalidade das ondas(ST)": "ST",
                                "Mostrando Hipertrofia Ventricular(LVH)":"LVH"}
    eletrocardiograma = st.sidebar.radio("Resultado Eletrocardiograma em Repouso", list(eletrocardiograma_opcoes.keys()))

    #Input Frequência Cardia Maxima Alcançada
    frequencia_cardiaca_max = st.sidebar.number_input('Qual foi a frequência cardíaca maxima alcançada ?',0,300)

    #Input Exercicio Induz Angina
    exercicio_opcoes = {"Sim": 1,"Não": 0}
    exercio_induz_angina = st.sidebar.radio("O exercicio induz a angina ?", list(exercicio_opcoes.keys()))

    #Input Depressão ECG
    depressao_ecg_opcoes = st.sidebar.number_input('Depressao ECG', -50, 100)

    #Input Inclinação ECG
    inclinacao_ecg_opcoes = {"Up":"Up","Flat":"Flat","Down":"Down"}
    inclinacao_ecg = st.sidebar.radio("Inclinação do Eletrocardiograma",list(inclinacao_ecg_opcoes()))




    #dicionário para receber informações

    user_data = {
    'Idade': idade,
    'Sexo': sexo,
    'Tipo de Dor no Peito': tipo_dor_peito,
    'Pressão Arterial em Repouso': pa_repouso,
    'Colesterol': colesterol,
    'Glicemia em Jejum >120 mg ?': glicemia_jejum,
    'Resultado Eletrocardiograma em Repouso': eletrocardiograma,
    'Qual foi a frequência cardíaca maxima alcançada ?': frequencia_cardiaca_max,
    'O exercicio induz a angina ?' : exercio_induz_angina,
    'Depressao ECG' : depressao_ecg,  
    'Inclinação do Eletrocardiograma' : inclinacao_ecg
        }


    features = pd.DataFrame(user_data, index=[0])


    return features

user_input_variables = get_user_date()

#grafico

graf = st.bar_chart(user_input_variables.iloc[0])

