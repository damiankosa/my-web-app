import streamlit as st
import functions as fu

todos = fu.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    fu.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a todo app which you can use to"
             " increase your productivity for e.g at work :)")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fu.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')