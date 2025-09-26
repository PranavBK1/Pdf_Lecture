from transformers import pipeline

# load once
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, chunk_size: int = 800, max_len: int = 120) -> list[str]:
    """
    Break text into chunks and summarize each.
    """
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    summaries = []
    for chunk in chunks:
        out = summarizer_pipeline(chunk, max_length=max_len, min_length=30, do_sample=False)
        summaries.append(out[0]['summary_text'])
    return summaries
