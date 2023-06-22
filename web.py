import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    todos.sort()
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")


for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Enter a new todo..",
              on_change=add_todo, key="new_todo")

st.session_state
