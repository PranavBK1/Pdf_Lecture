from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from pptx import Presentation
from pathlib import Path

def slides_to_video(pptx_path: str, audio_path: str, out_path: str, slide_duration: int = 5):
    prs = Presentation(pptx_path)
    # Export slides as images
    img_dir = Path("outputs/slide_imgs")
    img_dir.mkdir(parents=True, exist_ok=True)

    image_clips = []
    for i, slide in enumerate(prs.slides):
        img_file = img_dir / f"slide_{i}.png"
        # NOTE: pptx-python cannot export images, so in real impl we’d need `python-pptx-to-img` workaround.
        # Placeholder: create blank image for now
        from PIL import Image, ImageDraw
        img = Image.new("RGB", (1280, 720), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((100,100), f"Slide {i+1}", fill=(0,0,0))
        img.save(img_file)

        clip = ImageClip(str(img_file)).set_duration(slide_duration)
        image_clips.append(clip)

    video = concatenate_videoclips(image_clips, method="compose")
    audio = AudioFileClip(str(audio_path))
    video = video.set_audio(audio)
    video.write_videofile(str(out_path), fps=24)
