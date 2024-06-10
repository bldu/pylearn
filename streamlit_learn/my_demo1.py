import streamlit as st
import pandas as pd
import numpy as np

# define some constant string
basic_concepts = 'Basic Concepts'
advanced_concepts = 'Advanced Concepts'
tabs = "tabs"

def page_basic_concepts():
    st.title(basic_concepts)

    st.write("### `st.button`")
    if st.button('Say hello'):
        st.write('*Why hello there*')
    else:
        st.write('**Goodbye**')

    st.write("### Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

    st.write("### `st.slider`")
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

    st.write("### `st.text_input`")
    st.text_input("Your name", key="name")
    # You can access the value at any point with:
    st.write(f"Your name is {st.session_state.name}")

    st.write("### `st.checkbox`" )
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])
        st.write(chart_data)

    st.write("### `st.selectbox`" )
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })
    option1 = st.selectbox(
        'Which number do you like best?',
        df['first column'])
    st.write('You selected: ', option1)
    arr = [100, 200, 300]
    option2 = st.selectbox("supported numbers", arr)
    st.write('You selected: ', option2)

    st.write("### `st.columns`" )
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')
    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")


def page_advanced_concepts():
    st.title(advanced_concepts)

def page_tabs():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

def main():
    # 设置初始页面为Home
    session_state = st.session_state
    if 'page' not in session_state:
        session_state['page'] = 'Home'

    # 导航栏
    page = st.sidebar.radio('Navigate', [basic_concepts, advanced_concepts, tabs], index=None)

    if page == basic_concepts:
        page_basic_concepts()
    elif page == advanced_concepts:
        page_advanced_concepts()
    elif page == tabs:
        page_tabs()

if __name__ == '__main__':
    main()
