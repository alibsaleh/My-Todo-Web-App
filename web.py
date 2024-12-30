import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#order matters here
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

#iterates the updated todos
for index, todo in enumerate(todos):
   checkbox = st.checkbox(todo, key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# pip freeze > requirements.txt
#tells us all the packages we've installed

