import streamlit as st

def app(data):
    """
        data : It describes the data in the
               Info page
    """
    st.title("Information Page")
    st.subheader("View Data")

    # check the data
    with st.expander("View Data"):
        st.dataframe(data)

    # Columns values
    st.subheader("Column Description : ")

    # Check box
    if st.checkbox("View Summary"):
        st.dataframe(data.describe())

    # Check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Name of all DataFrames
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(data.columns)

    # Data Type of all columns
    with col_dtype:
        if st.checkbox("Column Data Types"):
            dtypes = data.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)

    # Data for each columns
    with col_data:
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name ", list(data.columns))
            st.dataframe(data[col])

    # Link to the dataset
    st.markdown('''
        <p style="font-size: 24px;">
            <a 
                href="https://www.kaggle.com/uciml/pima-indians-diabetes-database"
                target=_blank
                style="text-decoration: none;"   
            >
                Get Dataset    
            </a>        
        </p>
    ''', unsafe_allow_html=True)

