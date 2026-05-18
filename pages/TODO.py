import streamlit as st

st.title("TODO List App ")

with st.form("todo_form"):
    new_todo = st.text_input("Masukkan tugas baru:")
    new_todo_description = st.text_area("Deskripsi tugas (opsional):")
    submitted = st.form_submit_button("Tambah")

    if submitted and new_todo:
        st.session_state.todos.append((new_todo, new_todo_description))
        st.success(f"Tugas '{new_todo}' berhasil ditambahkan!")


if "todos" not in st.session_state:
    st.session_state.todos = []
else : 
    for i, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{todo[0]}**")
            if todo[1]:
                st.write(f"*{todo[1]}*")
        with col2:
            if st.button("Hapus", key=f"delete_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()