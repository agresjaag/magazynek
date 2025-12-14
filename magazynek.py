import streamlit as st

# Wstrzyknięcie niestandardowego CSS dla tęczowego tła
st.markdown("""
<style>
.stApp {
  background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
}
</style>
""", unsafe_allow_html=True)

# Używamy st.session_state do przechowywania listy, aby zmiany były trwałe
# przez całą sesję użytkownika.
if 'my_list' not in st.session_state:
    st.session_state.my_list = ['komputer', 'pralka', 'drabina', 'młotek', 'drukarka']

st.title('Magazyn') # Zmieniony tytuł na 'Magazyn'
st.write('Zmiany na liście są trwałe dzięki `st.session_state`!')

# Wyświetl aktualną zawartość my_list
st.subheader('Aktualna lista elementów:')
st.write(st.session_state.my_list)

# Utwórz pole tekstowe do wprowadzania nowego elementu
new_item = st.text_input('Wprowadź nowy element:', key='add_item_input')

# Utwórz przycisk do dodawania elementu
if st.button('Dodaj element') and new_item:
    st.session_state.my_list.append(new_item)
    st.success(f'Dodano: {new_item}')

# Utwórz pole tekstowe do wprowadzania elementu do usunięcia
item_to_remove = st.text_input('Wprowadź element do usunięcia:', key='remove_item_input')

# Utwórz przycisk do usuwania elementu
if st.button('Usuń element') and item_to_remove:
    if item_to_remove in st.session_state.my_list:
        st.session_state.my_list.remove(item_to_remove)
        st.warning(f'Usunięto: {item_to_remove}')
    else:
        st.error(f"Element '{item_to_remove}' nie znaleziono na liście.")

# Ponowne wyświetlenie listy po zmianach
st.subheader('Lista po interakcji:')
st.write(st.session_state.my_list)
