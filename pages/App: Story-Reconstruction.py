import streamlit as st

# Define the story text and audio URL
story_texts = [
    "Sometimes you may feel upset when you wake up suddenly from a nightmare, but you can always let out a sigh of relief. No matter how scary the dream was, at least you’ve woken up safe and sound in your own home.",
    "Unfortunately, this is not a reality that everyone shares. Many people around the world don’t wake up in a soft and comfortable bed. Instead, they open their eyes to see a dirt floor or a leaking roof.",
    "One day, I learned about a program that needed volunteers to go to different parts of the world to help build houses for the poor. After watching a presentation about it, I decided to take part in the next volunteer trip.",
    "The volunteers and I got to meet the family. We had to slowly take apart the family’s hut to get more bricks and other materials for the new house.",
    "After another week, the home was finally finished. On the last day, we had a party to celebrate the completion of the new house.",
    "This experience has inspired me to continue building houses for others. I hope it will also encourage my friends and family members to help out in the future."
]

audio_url = "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/output.mp3"

# Pair the text and images together in the correct order
story_images = [
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image1.jpeg",
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image2.jpeg",
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image3.jpeg",
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image4.jpeg",
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image5.jpeg",
    "https://raw.githubusercontent.com/Alexwcjung/24-final-project/main/image6.jpeg"
]

correct_order = [4, 5, 3, 1, 2]
ordered_story_pairs = [(story_texts[i - 1], story_images[i - 1]) for i in correct_order]

# Function to check the order
def check_order(order):
    if order == "45312":
        return "🎉 Congratulations! You got the correct order. 🎉"
    else:
        return "❌ Try again. The order is not correct."

# Streamlit App
st.title("🌍 Story Reconstruction Activity")
st.markdown("Listen to the story and place the images in the correct order!")

# Audio Section
st.subheader("🎧 Listen to the Story:")
st.audio(audio_url)

# Display Text and Images
st.subheader("🖼️ Story Steps:")
for idx, (text, image) in enumerate(ordered_story_pairs, 1):
    st.write(f"**Step {idx}:** {text}")
    st.image(image, caption=f"Step {idx}", width=200)

# User Input for Order
st.subheader("🧩 Enter the Order of Images")
user_input = st.text_input("Enter the image order as numbers (e.g., 45312):")

# Check Button and Feedback
if st.button("Check Order"):
    if user_input:
        result = check_order(user_input)
        st.subheader(result)
    else:
        st.warning("Please enter the image order before submitting.")

st.caption("Built with ❤️ using Streamlit")
