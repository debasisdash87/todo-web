import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    todos.sort()
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("This is my todo app")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todos.sort()
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("", placeholder="Enter a new todo..",
              on_change=add_todo, key="new_todo")
