import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Machine Learning')
model = pickle.load(open('C:\\Users\\pc\\OneDrive\\Documents\\project python\\Book_Project\\kaggleBookDataSet\\artifacts\\model.pckl', 'rb'))
book_names = pickle.load(open('C:\\Users\\pc\\OneDrive\\Documents\\project python\\Book_Project\\kaggleBookDataSet\\artifacts\\books_name.pckl', 'rb'))
final_rating = pickle.load(open('C:\\Users\\pc\\OneDrive\\Documents\\project python\\Book_Project\\kaggleBookDataSet\\artifacts\\final_rating.pckl', 'rb'))
book_pivot = pickle.load(open('C:\\Users\\pc\\OneDrive\\Documents\\project python\\Book_Project\\kaggleBookDataSet\\artifacts\\book_pivot.pckl', 'rb'))




def fecth_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['Book-Title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['Image-URL-L']
        poster_url.append(url)
    return poster_url




def recommend_book(book_name):
    book_list = []

    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    
    poster_url = fecth_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url



selected_books = st.selectbox(
    "Type or select a book",
    book_names
)


if st.button('Show recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])