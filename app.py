import streamlit as st
import random

def realizar_sorteo(participantes, num_ganadores):
    if num_ganadores > len(participantes):
        return participantes
    return random.sample(participantes, num_ganadores)

def main():
    st.title("Programa de Sorteos")
    if 'participantes' not in st.session_state:
        st.session_state.participantes = []

    if 'sorteo_realizado' not in st.session_state:
        st.session_state.sorteo_realizado = False

    st.header("Agregar Participantes")
    nuevo_participante = st.text_input("Nombre del Participante", help="Ingrese el nombre del nuevo participante")
    if st.button("Agregar Participante", key='add_participant', help="Agregar un nuevo participante a la lista"):
        if nuevo_participante and nuevo_participante not in st.session_state.participantes:
            st.session_state.participantes.append(nuevo_participante)
            st.success(f"Participante '{nuevo_participante}' agregado con éxito.")
        elif nuevo_participante in st.session_state.participantes:
            st.warning("Este participante ya está en la lista.")
        else:
            st.warning("Por favor, ingrese un nombre válido.")

    st.header("Eliminar Participantes")
    if st.session_state.participantes:
        participante_a_eliminar = st.selectbox("Seleccione un participante para quitar de la lista",
                                               st.session_state.participantes, help="Seleccione un participante para eliminar de la lista")
        
        if st.button("Eliminar Participante", key='remove_participant', help="Eliminar el participante seleccionado de la lista"):
            st.session_state.participantes.remove(participante_a_eliminar)
            st.success(f"Participante '{participante_a_eliminar}' eliminado de la lista.")
        
    else:
        st.info("No hay participantes en la lista para eliminar.")
    
    st.header("Realizar Sorteo")
    num_participantes = len(st.session_state.participantes)
    if num_participantes > 0:
        num_ganadores = st.number_input("Número de Ganadores", min_value=1, max_value=num_participantes, value=1, help="Ingrese el número de ganadores para el sorteo")
        if st.button("Realizar Sorteo", key='run_draw', help="Realizar el sorteo entre los participantes"):
            ganadores = realizar_sorteo(st.session_state.participantes, num_ganadores)
            st.success("¡Sorteo Realizado!")
            st.header("Ganadores del Sorteo:")
            for i, ganador in enumerate(ganadores, 1):
                st.write(f"{i}. {ganador}")
            st.session_state.sorteo_realizado = True

        if st.button("Reiniciar Sorteo", key='reset_draw', help="Reiniciar el sorteo para realizar un nuevo sorteo"):
            st.session_state.sorteo_realizado = False
            st.success("Sorteo reiniciado. Puedes realizar un nuevo sorteo.")

        if st.button("Eliminar a Todos los Participantes", key='remove_all', help="Eliminar a todos los participantes de la lista"):
            st.session_state.participantes = []
            st.session_state.sorteo_realizado = False
            st.success("Todos los participantes han sido eliminados.")
    else:
        st.warning("No hay participantes para realizar el sorteo.")

if __name__ == "__main__":
    main()


#para correr: streamlit run app.py