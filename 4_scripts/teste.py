import streamlit as st
import psycopg2
import pandas as pd
import altair as alt

# Função para conectar ao banco de dados Redshift
def connect_db():
    conn = psycopg2.connect(
        host='redshift-cluster-premierleague1.crbya6ximafi.us-east-1.redshift.amazonaws.com',
        port='5439',
        user='premierleague1',
        password='Premierleague1',
        database='dev'
    )
    return conn

# Função para executar uma consulta no banco de dados
def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return cursor, result

# Criar um aplicativo Streamlit com escolha de visualização e colunas
def main():
    st.title('Conectar Streamlit ao Banco de Dados Redshift')

    # Conectar ao banco de dados
    try:
        conn = connect_db()
        st.write("Conexão estabelecida com sucesso!")
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {str(e)}")
        return

    # Exemplo de consulta
    query = "SELECT * FROM premier_league;"

    # Adicionar opção para escolher entre tabela e gráfico de barras
    visualizacao = st.radio("Escolha a visualização:", ["Tabela", "Gráfico de Barras"])

    try:
        cursor, result = run_query(conn, query)

        # Converter os resultados para um DataFrame do Pandas
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)

        if visualizacao == "Tabela":
            # Exibir os resultados em forma de tabela
            st.write("Resultados da consulta:")
            st.table(df)
        elif visualizacao == "Gráfico de Barras":
            # Permitir ao usuário escolher as colunas para o gráfico
            colunas_grafico = st.multiselect("Escolha as colunas para o gráfico:", columns)

            if not colunas_grafico:
                st.warning("Por favor, selecione pelo menos uma coluna para o gráfico.")
            else:
                # Criar um gráfico de barras usando Altair
                st.write("Gráfico de Barras:")
                chart = alt.Chart(df).mark_bar().encode(
                    x=alt.X("nome_da_coluna_x:N", title="Nome da Coluna X"),
                    y=alt.Y("sum(nome_da_coluna_y):Q", title="Soma da Coluna Y"),
                    color=alt.Color("nome_da_coluna_cor:N", title="Nome da Coluna de Cor")
                ).interactive()
                st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Erro ao executar a consulta: {str(e)}")

if __name__ == '__main__':
    main()
