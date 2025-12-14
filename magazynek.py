import streamlit as st

# WAŻNE: Ta lista będzie resetowana za każdym razem, gdy użytkownik wejdzie w interakcję z aplikacją
# ponieważ nie używamy st.session_state do zachowania stanu.
my_list = ['komputer', 'pralka', 'drabina', 'młotek', 'drukarka']

st.title('Prosta aplikacja do zarządzania listą (bez trwałości)')
st.write('Pamiętaj, że lista resetuje się po każdej interakcji!')

# Wyświetl aktualną zawartość my_list przed jakąkolwiek interakcją
st.subheader('Aktualna lista elementów:')
st.write(my_list)

# Utwórz pole tekstowe do wprowadzania nowego elementu
new_item = st.text_input('Wprowadź nowy element:')

# Utwórz przycisk do dodawania elementu
# Po kliknięciu, aplikacja uruchomi się ponownie, a lista zostanie zresetowana do początkowej definicji
if st.button('Dodaj element') and new_item:
    my_list.append(new_item)
    st.success(f'Dodano: {new_item} (ale to nie będzie trwałe!)')

# Utwórz pole tekstowe do wprowadzania elementu do usunięcia
item_to_remove = st.text_input('Wprowadź element do usunięcia:')

# Utwórz przycisk do usuwania elementu
# Po kliknięciu, aplikacja uruchomi się ponownie, a lista zostanie zresetowana do początkowej definicji
if st.button('Usuń element') and item_to_remove:
    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        st.warning(f'Usunięto: {item_to_remove} (ale to nie będzie trwałe!)')
    else:
        st.error(f"Element '{item_to_remove}' nie znaleziono na liście (lista mogła się zresetować).")

# Ponowne wyświetlenie listy po hipotetycznych zmianach (które i tak się nie utrzymają)
st.subheader('Lista po interakcji (natychmiastowe zmiany):')
st.write(my_list)
