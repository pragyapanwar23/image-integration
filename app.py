import streamlit as st
from PIL import Image

st.title("Final Composited Image Viewer")
st.markdown("**Note:** This deployment can only display the final image formed at the end of the model due to time constraints.")
# Load and show image
image_path = "final_result_grounded.jpg"  # Update with the path to your generated image
img = Image.open(image_path)
st.image(img, caption="Seamlessly Integrated Image", width=350)

