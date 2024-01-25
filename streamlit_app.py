from zlibrary import Zlibrary
import streamlit as st

st.title('Zlibrary API hosted by tourkveg')
email = st.text_input('email')
password = st.text_input('password', type='password')
book_name = st.text_input('书名')
number = st.slider('数量限制',1,100)

book_list = list()
if st.button('搜索'):
  z = Zlibrary()
  z.login(email=email, password=password)
  res = z.search(message=book_name,limit=number)
  for book in res['books']:
    book_list.append(f'{book["title"]}|{book["extension"]}|{book["language"]}')
  choice = st.selectbox('选择下载',book_list)
  st.text(choice)
  filename, filecontent = z.downloadBook(res['books'][book_list.index(choice)])
  with open(filename, "wb") as bookfile:
    bookfile.write(filecontent)
  st.text(filename)
  file_name = f"book.{filename.split('.')[1]}"
  with open(file_name, "rb") as file:
      btn = st.download_button(
            label="下载文件",
            data=file,
            file_name=file_name
          )
  st.text("downloading...")
