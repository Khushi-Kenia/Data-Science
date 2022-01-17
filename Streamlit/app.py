from hashlib import new
import matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import sqlite3
conn =  sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author, title, article, postdate)')

def add_data(author, title, articlae, postdate):
    c.execute('INSERT INTO blogtable(author, title, article, postdate) VALUES (?, ?, ?, ?)', (author, title, article, postdate))
    conn.commit()

def view():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title= "{}".format(title)')
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable WHERE author= "{}".format(author)')
    data = c.fetchall()
    return data

def delete_data(title):
    c.execute('DELETE FROM blogtable WHERE title="{}".format(title)')

#Layout templates
title_temp = """
<div style = "background-color:#464ef; padding: 10px; margin: 10px;">
<h4 style = "color:white; text-align: center;">{}</h4>
<h4 style = "color:white; text-align: center;">Author:{}</h4>
<p>{}</p>
<h6 style = "color:white; text-align: center;">Post Date:{}</h6>
</div>

"""
#head_temp, article_temp, author_temp left to code 

def main():
    #Simple CRUD Blog
    # st.title("Hello World!")
    # st.header("This is a header")
    # st.subheader("This is a subheader")
    # st.text("Welcome Khushi")

    menu = ["Home", "View", "Edit", "Search", "Manage"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        result = view()
        st.write(result)
        for i in result:
            b_author = i[0]
            b_title = i[1]
            b_article = str(i[2])[0:50]
            b_post_date = i[3]
            st.markdown(title_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)
            st.write(i[0])

    elif choice == "View":
        st.subheader("View Posts")
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.sidebar.selectbox("View Posts", all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            b_author = i[0]
            b_title = i[1]
            b_article = i[2]
            b_post_date = i[3]
            st.markdown(head_message_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)
            st.markdown(full_message_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)

    elif choice == "Edit":
        st.subheader("Edit Posts")
        st.subheader("Add posts")
        create_table()
        blog_author = st.text_input("Enter author name", max_chars=50)
        blog_title = st.text_input("Title Name", max_chars=50)
        blog_article = st.text_area("Post Article", height=200)
        blog_date = st.date_input("Date")
        if st.button("Add"):
            add_data(blog_author, blog_title, blog_article, blog_date)
            st.success("Post:{} saved".format(blog_title))

    elif choice == "Search":
        st.subheader("Search Posts")
        search_table = st.time_input("Enter Search Term")
        search_choice = st.radio("Field to Search", ("title", "author"))
       
        if st.button("Search"):
            
            if search_choice == "title":
                article_result = get_blog_by_title(search_term)
            elif search_choice == "author":
                article_result = get_blog_by_author(search_term)

            for i in article_result:
                b_author = i[0]
                b_title = i[1]
                b_article = i[2]
                b_post_date = i[3]
                st.markdown(head_message_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)
                st.markdown(full_message_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)

    elif choice == "Manage":
        st.subheader("Manage Blog")
    
    result = view()
    clean_db = pd.DataFrame(result, columns=["Author", "Title", "Articles", "Post Date"])
    st.dataframe(clean_db)

    delete_title = [i[0] for i in view_all_titles()]
    delete_blog_by_title = st.selectbox("Delete Title", all_titles)
    if st.button("Delete"):
        delete_data(delete_blog_by_title)
        st.warning("Deleted: '{}'".format(delete_blog_by_title))

    if st.checkbox("Metrics"):
        new_df = clean_db
        new_df["Length"] = new_df["Articles"].str.len()
        st.dataframe(new_df)

        st.subheader("Author Stats")
        new_df["Author"].value_counts().plot(kind='bar')
        st.pyplot()

        st.subheader("Author Stats")
        new_df["Author"].value_counts().plot.pie(autopct="%1.1f%%")
        st.pyplot()

if __name__ == '__main__':
    main()