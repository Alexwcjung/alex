# Import required libraries
import gradio as gr

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

# Define the correct order for the images
correct_order = [4, 5, 3, 1, 2]

# Rearrange the story pairs according to the correct order
ordered_story_pairs = [(story_texts[i - 1], story_images[i - 1]) for i in correct_order]


# Function to check the order of the images
def check_order(order):
    if order == "45312":
        return "🎉 Congratulations! You got the correct order. 🎉"
    else:
        return "❌ Try again. The order is not correct."

# Gradio Interface
def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 🌍 Story Reconstruction Activity")
        gr.Markdown("Listen to the story and place the images in the correct order!")

        # Display the audio file
        gr.Audio(audio_url, autoplay=False)

        # Display text-image pairs
        for num, (txt, img) in enumerate(ordered_story_pairs, 1):
            with gr.Row():
                gr.Image(img, width=200, height=200)
                gr.Markdown(f"**{num}.** {txt}")

        # Input for order checking
        gr.Markdown("### 🧩 Enter the order of images (e.g., `45312`)")
        order_input = gr.Textbox(label="Image Order")
        result = gr.Textbox(label="Feedback", interactive=False)

        submit_btn = gr.Button("Check Order")
        submit_btn.click(fn=check_order, inputs=order_input, outputs=result)

    return demo

# Launch the app
demo = create_interface()
demo.launch(share=True)
