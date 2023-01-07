import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans




st.header('Cluster Analysis')

# Allow the user to select a CSV file from the sidebar or upload their own
st.sidebar.subheader('Input File')
file_1 = 'supermarket_MY.csv'
file_2 = 'workshop_MY.csv'
#file_3 = 'trump_clean.csv'
# uploaded_file = st.sidebar.file_uploader('Upload a CSV file')
# if uploaded_file is not None:
#   file = uploaded_file.getvalue().decode()
# else:
file = st.sidebar.radio('Or choose a default CSV file', options=[file_1, file_2])
df = pd.read_csv(file)
df = df.drop(df.columns[0], axis=1)
# perform one-hot encoded for categorical data
df = pd.get_dummies(df)
# Create a sidebar with options to select the X and Y variables, the number of clusters, and the CSV file
st.sidebar.header('Select the X and Y variables')
x_var = st.sidebar.selectbox('X variable', df.columns.tolist())
y_var = st.sidebar.selectbox('Y variable', df.columns.tolist())

st.sidebar.header('Select the number of clusters')
n_clusters = st.sidebar.slider('Number of clusters', 2, 10, 3, 1)

# Add a "Analyze" button to the sidebar
if st.sidebar.button('Analyze'):
    if file is not None:
        # Load the data from the CSV file
        df = pd.read_csv(file)

    # Perform KMeans clustering on the selected columns
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(df[[x_var, y_var]])
    labels = kmeans.predict(df[[x_var, y_var]])
    df['cluster'] = labels

    # Plot the clusters using a scatter plot
    sns.scatterplot(x=x_var, y=y_var, hue='cluster', data=df)
    st.pyplot()
