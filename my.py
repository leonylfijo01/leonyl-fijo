import streamlit as st
 
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi!, Everyone :wave:")
    st.header("Programming Logic and Design Blog's Ativity")
    st.subheader("Do you want to know about my story?")

# ---- PERSONAL INFORMATION ----
with st. container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("EMBRACING JOY")
        st.subheader("I'm Leonyl Quiban Fijo, and a great journey has begun. Since the beginning of my life. I've discovered the profound power of happiness as a guiding force. Childhood days were filled with laughter, curiosity, and an instinctive ability to discover joy in the most insignificant of circumstances.")   
    with right_column:
        st.image("https://media.giphy.com/media/1Qi7GG8my6uhLHPLP5/giphy.gif", use_column_width=True)

with st. container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("myself.jpg")
    with right_column:
        st.subheader("I faced challenges and trials that may have put a shadow over the story. However, with patience and an unbreakable commitment to happiness, every challenge became a stepping stone to success. Each chapter revealed moments of meditation in which the full richness of life's stuff was realized. From the brilliant colors of sunsets to the warmth of deep relationships. I've made thankfulness a daily discipline.")
        st.subheader("Respect was crucial. I learned to appreciate not only the significant achievements, but also the tiny aspects that added to the complexity within my story. From the taste of morning coffee to the rustle of leaves in the breeze, appreciation became the lens through which the world was perceived.")
        st.subheader("My story was not a great ending, but rather a collection of events connected by a common thread of happiness, thanks, and appreciation. The awareness dawned that joy was a journey, and each step along the way was cause for celebration.")
        st.subheader("As a story, it turned my pages; a life well-lived is one filled with happiness, steeped in gratitude, and set with appreciation for the complex detail that unfolds in each chapter.")
        
st.write("Just message me for more details!")
st.write("[My Facebook>]https://www.facebook.com/leonyl.fijo)")
