from story_generator import get_daily_stories
from illustration_generator import generate_illustration
from audio_generator import generate_audio_story

blob_url = "https://codetales.blob.core.windows.net/code-tales"

def run_pipeline():
    # Get new daily stories
    new_stories = get_daily_stories()
    for story in new_stories:
        # Generate audio version for each story
        generate_audio_story(story_id=story["id"], story=story["text"])
        # Generate illustration for each story
        generate_illustration(story_id=story["id"], story_title=story["title"])

run_pipeline()


