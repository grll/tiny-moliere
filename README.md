# tiny-moliere

A dataset repo generating `tinymoliere.txt` containing Molière's complete work.

Inspired by [tinyshakespeare](https://github.com/karpathy/char-rnn/blob/master/data/tinyshakespeare/input.txt) by Andrej Karpathy, this project provides a consolidated small text corpus ideal for training and learning with small transformer models.

## What it does

Downloads Molière's complete works from public PDFs, processes them to remove headers/footers and table of contents, then outputs a single clean text file suitable for machine learning tasks.

## Usage

```bash
uv sync
uv run python main.py
```

This will:
1. Download the source PDFs to `data/` directory
2. Process and clean the text
3. Generate `data/tinymoliere.txt`