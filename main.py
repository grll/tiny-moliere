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
    # 1. fetch raw data if (not already fetched)

    # fetch from
    # 2. process data into clean tiny-shakespeare like format

    # 3. save processed data to disk
    print("Hello from tiny-moliere!")


if __name__ == "__main__":
    main()
