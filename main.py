from pathlib import Path

import httpx

DATA_DIR = Path.cwd() / "data"

RAW_PDF_URLS = [
    "https://www.ebooksgratuits.com/ebooksfrance/moliere-oeuvres_completes_1.pdf",
    "https://www.ebooksgratuits.com/ebooksfrance/moliere-oeuvres_completes_2.pdf",
]


def download_pdf(url: str, output_path: str) -> None:
    """Download a PDF from the given URL and save it to the specified output path."""
    with httpx.stream("GET", url, follow_redirects=True) as response:
        response.raise_for_status()  # ensure we got a 200 OK
        with open(output_path, "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)


def main():
    # make sure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # download raw PDFs if they don't already exist
    for url in RAW_PDF_URLS:
        filename = url.split("/")[-1]
        output_path = DATA_DIR / filename
        if not output_path.exists():
            print(f"Downloading {filename}...")
            download_pdf(url, output_path)
        else:
            print(f"{filename} already exists, skipping download.")

    # fetch from
    # 2. process data into clean tiny-shakespeare like format

    # 3. save processed data to disk
    print("Hello from tiny-moliere!")


if __name__ == "__main__":
    main()
