import argparse
from pathlib import Path
from flattened_app.core import pdf_parser, summarizer, slide_generator, tts, video_generator

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="PDF → Slides/Video CLI")
    parser.add_argument("pdf", help="Input PDF path")
    parser.add_argument("--mode", choices=["slides", "video"], default="slides")
    args = parser.parse_args()

    text = pdf_parser.extract_text(args.pdf)
    summaries = summarizer.summarize_text(text)

    if args.mode == "slides":
        pptx_path = OUTPUT_DIR / "slides.pptx"
        slide_generator.generate_slides(summaries, pptx_path)
        print(f"Slides saved to {pptx_path}")
    else:
        pptx_path = OUTPUT_DIR / "slides.pptx"
        audio_path = OUTPUT_DIR / "narration.mp3"
        mp4_path = OUTPUT_DIR / "lecture.mp4"
        slide_generator.generate_slides(summaries, pptx_path)
        tts.text_to_speech(" ".join(summaries), audio_path)
        video_generator.slides_to_video(pptx_path, audio_path, mp4_path)
        print(f"Video saved to {mp4_path}")

if __name__ == "__main__":
    main()
