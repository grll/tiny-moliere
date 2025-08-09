from pathlib import Path

import httpx
import pymupdf # type: ignore

# where to save / load data
DATA_DIR = Path.cwd() / "data"

# URLs of the raw PDFs to download
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


def detect_toc(doc: pymupdf.Document) -> tuple[int, int]:
    """Detect the table of contents in the first quarter of the document.
    
    Args:
        doc: A pymupdf Document object representing the PDF document.

    Returns:
        A tuple containing the start and end page indices of the TOC.
        If no TOC is found, returns (-1, -1).
    """
    start = -1
    end = -1
    i = 0

    for page in doc[:len(doc) // 4]:
        if page.get_links():
            start = i
            break
        i += 1

    if start == -1:
        print("No table of contents found in the first quarter of the document.")
        return -1, -1  # no TOC found

    for page in doc[start:len(doc) // 4]:
        if not page.get_links():
            end = i
            break
        i += 1

    if end == -1:
        end = len(doc) // 4

    print(f"Table of contents detected from page {start} to {end}.")
    return start, end


def main():
    # make sure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # download raw PDFs if they don't already exist
    paths = []
    for url in RAW_PDF_URLS:
        filename = url.split("/")[-1]
        output_path = DATA_DIR / filename
        paths.append(output_path)
        if not output_path.exists():
            print(f"Downloading {filename}...")
            download_pdf(url, output_path)
        else:
            print(f"{filename} already exists, skipping download.")

    # fetch from

    for path in paths:
        with open(path, "rb") as f:
            doc = pymupdf.open(f)
            # process the document as needed

            # detect toc in first quarter of the document
            toc_start, toc_end = detect_toc(doc)
            breakpoint()

            # read toc

            # extract info from toc
            data = {
                "title": None,
                "actors": None,
                "acts": [
                    {
                        "start_page": 0,
                        "end_page": 0,
                        "title": None,
                        "scenes": [
                            {
                                "start_page": 0,
                                "end_page": 0,
                                "title": None,
                            }
                        ]
                    }
                ]
            }
            breakpoint()
    # 1. download raw PDFs from URLs
    # 2. process data into clean tiny-shakespeare like format

    # 3. save processed data to disk
    print("Hello from tiny-moliere!")


if __name__ == "__main__":
    main()
