import streamlit as st
from pathlib import Path
from flattened_app.core import pdf_parser, summarizer, slide_generator, tts, video_generator
from flattened_app.utils import file_utils

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

st.title("📚 PDF → Lecture/Slides Converter")

uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
option = st.radio("Choose Output Type:", ["Slides (PPTX)", "Video Lecture"])

if uploaded_pdf:
    pdf_path = file_utils.save_temp_file(uploaded_pdf, OUTPUT_DIR)

    st.write("Extracting text...")
    text = pdf_parser.extract_text(pdf_path)

    st.write("Summarizing...")
    summary_chunks = summarizer.summarize_text(text)

    if option == "Slides (PPTX)":
        pptx_path = OUTPUT_DIR / "lecture_slides.pptx"
        slide_generator.generate_slides(summary_chunks, pptx_path)
        st.success("Slides generated!")
        st.download_button("Download Slides", pptx_path.read_bytes(), file_name="slides.pptx")

    elif option == "Video Lecture":
        audio_path = OUTPUT_DIR / "narration.mp3"
        pptx_path = OUTPUT_DIR / "lecture_slides.pptx"
        mp4_path = OUTPUT_DIR / "lecture_video.mp4"

        slide_generator.generate_slides(summary_chunks, pptx_path)
        tts.text_to_speech(" ".join(summary_chunks), audio_path)
        video_generator.slides_to_video(pptx_path, audio_path, mp4_path)

        st.success("Video generated!")
        st.video(str(mp4_path))
        st.download_button("Download Video", mp4_path.read_bytes(), file_name="lecture.mp4")
