import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# Botão na barra lateral para exibir o gráfico
if st.sidebar.button("Exibir gráfico"):
    # Dados reais
    dados = {
        'Ano do óbito': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
        'Masculino': [3887, 3916, 3939, 3851, 3737, 3567, 3520, 3539, 2975, 2945, 3236],
        'Feminino': [3211, 3137, 3219, 2978, 2907, 3090, 2982, 2889, 2457, 2484, 2537],
        'Ign': [20, 17, 15, 20, 23, 23, 28, 15, 27, 21, 22],
        'Total': [7118, 7070, 7173, 6849, 6667, 6680, 6530, 6443, 5459, 5450, 5795]
    }

    # Criando o DataFrame com os dados reais
    df = pd.DataFrame(dados)
    df['Ano do óbito'] = df['Ano do óbito'].astype(int)

    # Definindo o título do gráfico
    st.write("Óbitos p/Residênc por Sexo segundo Ano do Óbito")
    st.write("Período: 2012-2022 - Fonte DataSus")

    # Exibindo o gráfico de linhas
    st.line_chart(df.set_index('Ano do óbito'))

    # Exibindo o gráfico de barras
    st.bar_chart(df.set_index('Ano do óbito'))
    st.dataframe(df)









