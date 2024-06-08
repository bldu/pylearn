import streamlit as st

def page_home():
    st.title('Home Page')
    # 在Home页面中显示数据和功能组件

def page_about():
    st.title('About Page')
    # 在About页面中显示数据和功能组件

def main():
    # 设置初始页面为Home
    session_state = st.session_state
    if 'page' not in session_state:
        session_state['page'] = 'Home'

    # 导航栏
    page = st.sidebar.radio('Navigate', ['Home', 'About'])

    if page == 'Home':
        page_home()
    elif page == 'About':
        page_about()

if __name__ == '__main__':
    main()
