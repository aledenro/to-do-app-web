import streamlit as stl
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = stl.session_state["new_todo"] + "\n"
    if new_todo.strip() != "":
        todos.append(new_todo)
        functions.write_todos(todos)


stl.title("My Todo App")
stl.write("Please type your to-do and press <b>Enter</b>.", unsafe_allow_html=True)
stl.write("To complete a to-do please check the <b>Checkbox</b> associated to that to-do.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
   checkbox = stl.checkbox(todo, key=todo)

   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del stl.session_state[todo]
       stl.rerun()


stl.text_input(label="", placeholder="Add new todo...",
               on_change=add_todo, key="new_todo")
