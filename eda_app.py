import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title(':bar_chart: Explore Your DATA :bar_chart:')
st.markdown(""
            "")

upload_file = st.sidebar.file_uploader("Upload a file", type="csv")
file_1 = 'supermarket_MY.csv'
file_2 = 'workshop_MY.csv'
file_3 = 'supermarket_sales - Sheet1.csv'
### assigning columns inside 1 df into a class or numerical variable ###
if upload_file is not None:
    data = pd.read_csv(upload_file)
    obj = []
    int_float = []
    for i in data.columns:
        clas = data[i].dtypes
        if clas == 'object':
            obj.append(i)
        else:
            int_float.append(i)

choose_file = st.sidebar.radio('Or choose a default CSV file', options=[file_1, file_2, file_3])
if choose_file is not None:
    data = pd.read_csv(choose_file)
    obj = []
    int_float = []
    for i in data.columns:
        clas = data[i].dtypes
        if clas == 'object':
            obj.append(i)
        else:
            int_float.append(i)

    # #### adding a submit button sidebar
    # with st.form(key='my_form'):
    #     with st.header("Press button below to remove all Null Values in your dataset"):
    #         submit_button = st.form_submit_button(label='Remove Null')
    #
    # #### if we click remove null button, null values will be replaced with Mean(int_float) and mode(obj)
    # if submit_button:
    #     for i in data.columns:
    #         clas = data[i].dtypes
    #         if clas == 'object':
    #             data[i].fillna(data[i].mode()[0], inplace=True)
    #         else:
    #             data[i].fillna(data[i].mean(), inplace=True)
    #
    # #### finding number of null values in each columns
    # null = []
    # for i in data.columns:
    #     dd = sum(pd.isnull(data[i]))
    #     null.append(dd)

    # #### if number of null values are zero, text will display. Else, bar plot for each column will display
    # if max(null) == 0:
    #     st.write("Total no. of Null Values = " +str(max(null)))
    # else:
    #     st.write("Bar Plot for the number of Null Values for each column")
    #     st.write("Total no. of Null Values = " +str(max(null)))
    #     fig2 = px.bar(x=data.columns, y=null, labels={'x':"Column Names", 'y':"No. of Null Values"})
    #     st.plotly_chart(fig2)

    ## show df
    st._legacy_dataframe(data, height=200, width=1200)



    col_1, col_2 = st.columns(2)
    #### Frequency Plot
    with col_1:
        st.sidebar.header("Select Variable")
        selected_post = st.sidebar.selectbox('Object Variables', obj)
        st.subheader("Frequency for each category")
        frequency_data = data[selected_post].value_counts()
        # st.write(frequency_data)
        fig = px.bar(frequency_data, x=frequency_data, y=selected_post, labels={'x':selected_post})
        fig.update_layout(height=500, width=300)
        st.plotly_chart(fig)

    #### Histogram
    with col_2:
        st.sidebar.header("Select Variable")
        selected_post1 = st.sidebar.selectbox('Integer or Float Variable', int_float)
        st.subheader("Frequency for each values")
        counts, bins = np.histogram(data[selected_post1], bins=range(int(min(data[selected_post1])), int(max(data[selected_post1]))))
        bins = 0.5 * (bins[:-1] + bins[1:])
        fig1 = px.bar(x=bins, y=counts, labels={'x':selected_post1, 'y':'counts'})
        fig1.update_layout(height=500, width=400)
        st.plotly_chart(fig1)


    #### Correlation Chart
    st.sidebar.header("Select Variable")
    selected_post2 = st.sidebar.multiselect('Int or Float Variables-Correlation', int_float)
    st.write("Scatter Plot for Correlation")
    if len(selected_post2) == 2:
        fig3 = px.scatter(data, x=selected_post2[0], y=selected_post2[1])
        st.plotly_chart(fig3)
    else:
        st.write("Select Two Variables")