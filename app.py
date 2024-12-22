from dotenv import load_dotenv
load_dotenv() # load all the enviorment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

##Configure our API key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY "))

##function to load Google Gemini model and provide Sql query  as response 
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text
# function to retrive query from sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Create a Prompt

Prompt= [
    """
        You are an expert in converting English questions to SQl query!
        The SQL database has the Name STUDENT and has the following colums - NAME, CLASS,
        SECTION and MARKS \n\nFor example, \nExample1 - How many entries of records are present
        the SQl command will be something like this SELECT COUNT(*) from STUNDENT ;
        \nExample 2 - Tell me all the students studying in the data Science class?,
        the sql command will be something like this SELECT * From STUDENT
        where CLASS = "DATA SCIENCE";
        also the sql query should not have ''' in begining or end and sql word in output
    """
]

## streamlit app
st.set_page_config(page_title="I can retrive any SQl Query")
st.header("Gemini APP to retrive SQL Data")

question=st.text_input("input: ", key ="Input")

submit=st.button("Ask the question")

##if submit is clicked
if submit:
    response=get_gemini_response(question, Prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader(" The response is ")
    for row in data:
        print(row)
        st.header(row)

    
