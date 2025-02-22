import streamlit as st
import openai
import time

# Set the OpenAI API key
openai.api_key = "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"

# Set Streamlit app theme and styling with custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ff7b00, #ff4b00, #ff0000);
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .stTextInput>div>div>input {
            background-color: #f4f4f4;
            color: #333;
            border-radius: 12px;
            padding: 10px;
            font-size: 18px;
        }

        .stButton>button {
            background-color: #ff6f61;
            color: white;
            border-radius: 30px;
            padding: 10px 20px;
            font-size: 16px;
        }

        .stButton>button:hover {
            background-color: #ff4d3f;
            cursor: pointer;
        }

        .stText {
            font-size: 20px;
            color: #fff;
            font-weight: 600;
        }

        .stMarkdown {
            font-size: 22px;
            color: #f9f9f9;
            font-family: 'Verdana', sans-serif;
            text-align: center;
        }
        .stTextInput input::placeholder {
            color: #888;
        }

        /* Styling the input text box */
        .stTextInput>div>div {
            background-color: #f4f4f4;
            border-radius: 12px;
        }

        .stTextInput input {
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app title with some cool emoji
st.title("💬 Chat with ClarifAI 💬")
st.markdown("<h3 style='text-align: center; color: white;'>Your Personal AI Chat Assistant 🚀</h3>", unsafe_allow_html=True)

# Add a fun message
st.markdown("""
    <div style="text-align: center; font-size: 20px; color: #fff; font-weight: 300;">
        Enter your message below and let ClarifAI handle it! ✨
    </div>
    """, unsafe_allow_html=True)

# Text input box for user input
user_input = st.text_input("💬 Type your message:", placeholder="Ask me anything!")

# Placeholder for showing loading indicator while waiting for response
placeholder = st.empty()

# On button click, perform the API call
if st.button("🚀 Generate Response"):
    if user_input:
        # Show loading message while waiting for response
        with placeholder.container():
            st.write("🌀 Fetching your answer...")

        try:
            # Requesting response from the AI model
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or another model of your choice
                messages=[{"role": "user", "content": user_input}],
                temperature=0.5,
                max_tokens=1024
            )

            # Extract the response
            response = completion.choices[0].message['content']

            # Display the final response
            st.markdown(f"### 🤖 **ClarifAI's Response:**")
            st.markdown(f"<div style='font-size: 20px; color: #fff; background-color: #333; padding: 10px 15px; border-radius: 15px;'>{response}</div>", unsafe_allow_html=True)

        except openai.error.AuthenticationError:
            st.error("Authentication failed. Please check your API key.")
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred with the OpenAI API: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    else:
        st.error("Please enter a message to chat with ClarifAI.")
