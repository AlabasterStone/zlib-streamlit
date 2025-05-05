from zlibrary import Zlibrary
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0
def set_state(i):
    st.session_state.stage = i

if st.session_state.stage >= 0:
    st.title('Zlibrary API\n made with ❤️ by tourkveg')
    #email = st.text_input('email')
    email = st.secrets['ZLIB_EMAIL']
    #password = st.text_input('password', type='password')
    password = st.secrets['ZLIB_PASSWORD']
    book_name = st.text_input('书名')
    number = st.slider('数量限制',1,100)
    book_list = list()
    st.button('搜索', on_click=set_state,args=[1])

if st.session_state.stage>=1:
  z = Zlibrary()
  z.login(email=email, password=password)
  res = z.search(message=book_name,limit=number)
  for book in res['books']:
    book_list.append(f'{book["title"]}|{book["extension"]}|{book["language"]}')
  choice = st.selectbox('选择下载',book_list)
  st.button('确认',on_click=set_state,args=[2])

if st.session_state.stage>=2: 
  with st.spinner("downloading..."):
      filename, filecontent = z.downloadBook(res['books'][book_list.index(choice)])
      file_name = f"book.{filename.split('.')[1]}"
      with open(filename, "wb") as bookfile:
        bookfile.write(filecontent)
  with open(filename, "rb") as file:
    btn = st.download_button(
              label="下载文件",
              data=file,
              file_name=filename
            )


