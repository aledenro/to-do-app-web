import streamlit as stl
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = stl.session_state["new_todo"] + "\n"
    if new_todo.strip() != "":
        todos.append(new_todo)
        functions.write_todos(todos)


stl.title("My Todo App")
stl.subheader("This is my todo app.")
stl.write("This app is to increase you productivity.")

for index, todo in enumerate(todos):
   checkbox = stl.checkbox(todo, key=todo)

   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del stl.session_state[todo]
       stl.rerun()


stl.text_input(label="", placeholder="Add new todo...",
               on_change=add_todo, key="new_todo")
