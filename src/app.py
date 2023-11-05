import streamlit as st
import sys
sys.path.append('../backend/services')

from dotenv import load_dotenv
from backend.data_layer.repo import StoryRepository


def main():
    load_dotenv()
    repo = StoryRepository()
    # Set page title and favicon.
    st.set_page_config(page_title="Code Tales", page_icon="📖")

    st.title("Code Tales - Embark on an Epic Adventure in the World of Coding! 🚀")

    stories = repo.get_stories()

    # Create a navigation menu in the sidebar
    selected_story = st.sidebar.radio("Select your next coding adventure.", ["Home"] + [story["title"] for story in stories])

    if selected_story == "Home":
        st.subheader(" \n Select a story from the sidebar to get started.")
        st.write(
            """
                Welcome to a place where learning is an exciting journey. Dive into the magical realms of logic and programming with our interactive and fun stories. Join our young heroes as they conquer challenges, solve puzzles, and unleash their creative potential.\n

                🌟 Uncover the Secrets of Coding\n
                🌈 Explore New Worlds of Logic\n
                🎮 Play, Learn, and Code Together\n
                🔥 Ignite Your Child's Imagination\n\n

                Turn your child into a coding wizard while they have a blast! Get started on the path to a brighter future today. Let the adventure begin!
            """
        )
    else:
        # Display the selected page's text and image
        story = [s for s in stories if s["title"] == selected_story][0]
        st.header(story["title"])
        st.write(f"Category: {story['category']}")
        # Display music player
        st.audio(story["audio"])

        st.write(story["text"])

        # Display the story illustration
        st.image(story["illustration"])


if __name__ == "__main__":
    main()
