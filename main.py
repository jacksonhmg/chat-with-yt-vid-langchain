import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))

if animal_type == "Cat":
    pet_colour = st.sidebar.text_area("What is your cat's colour?", max_chars=15)

if animal_type == "Dog":
    pet_colour = st.sidebar.text_area("What is your dog's colour?", max_chars=15)

if animal_type == "Cow":
    pet_colour = st.sidebar.text_area("What is your cow's colour?", max_chars=15)

if animal_type == "Hamster":
    pet_colour = st.sidebar.text_area("What is your Hamster's colour?", max_chars=15)

if pet_colour:
    response = lch.generate_pet_names(animal_type, pet_colour)
    st.text(response)