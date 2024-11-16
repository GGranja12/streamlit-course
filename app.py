import streamlit as st

# Set up the page
st.set_page_config(
    page_title="Superhero App",
    layout="centered", # or wide
    page_icon="🦸", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)


st.title("SuperHero name creator 🦸🦸‍♀️" )

#User Inputs
favorite_color = st.text_input("Enter your favorite color:")
favorite_animal = st.text_input("Enter your favorite animal:")
lucky_number = st.number_input("Enter your lucky number:", step=1)

#Dropdown for superpower
superpower= st.selectbox("Choose your superpower:", ["Flying", "Invisibility", "Super Strength"])

#Superhero name generator
if st.button("Generate My Superhero Name") == True:
    superhero_name = (f"{favorite_color} {favorite_animal} of {lucky_number}")
    st.header(f"🦸 Your Superhero Name: {superhero_name}")
    st.write(f"🌟Superpower: {superpower}")

    st.subheader("Your Superhero motto:")
    st.write(f"With great power comes great {superpower}")
