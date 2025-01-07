import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def capture_google_slides(url, output_folder, headless=True):
    """
    Captures screenshots of slides from a Google Slides presentation.

    Args:
        url (str): The URL of the Google Slides presentation.
        output_folder (str): Folder where the slide images will be saved.
        headless (bool): Run browser in headless mode.
    """
    # Set up Chrome options
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Open the Google Slides presentation
        driver.get(url)

        # Allow time for the page to load fully
        time.sleep(20)

        # Pre locate all slide thumbnails in the filmstrip first
        slides = driver.find_elements(By.CLASS_NAME, "punch-filmstrip-thumbnail")
        slide_count = len(slides)
        print(f"[PRE] Number of slides detected: {slide_count}")
        for i in range(slide_count * 10): # Some bullshit number test!
            try:
                slides = driver.find_elements(By.CLASS_NAME, "punch-filmstrip-thumbnail")
                slides[i].click()
                # Allow time for the slide to load
                time.sleep(1)
            except:
                print(f"Page {i + 1} is not existed!")
                break
        
        slides = driver.find_elements(By.CLASS_NAME, "punch-filmstrip-thumbnail")
        slide_count = len(slides)
        print(f"[POST] Number of slides detected: {slide_count}")

        # Iterate through each slide
        for i, slide in enumerate(slides):
            slide.click()

            # Allow time for the slide to load
            time.sleep(3)

            # Locate the canvas-container
            canvas_container = driver.find_element(By.ID, "canvas-container")

            # Take a screenshot of the canvas-container
            screenshot = canvas_container.screenshot_as_png

            # Save the image
            image_path = os.path.join(output_folder, f"slide_{i + 1}.png")
            with open(image_path, "wb") as f:
                f.write(screenshot)
            print(f"Captured slide {i + 1}")
    finally:
        # Clean up
        driver.quit()


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Capture screenshots of Google Slides.")
    parser.add_argument("url", type=str, help="URL of the Google Slides presentation.")
    parser.add_argument(
        "--output-folder", type=str, default="output", help="Folder to save slide images (default: 'output')."
    )
    parser.add_argument("--no-headless", action="store_true", help="Run browser in non-headless mode for debugging.")

    args = parser.parse_args()

    # Run the function with provided arguments
    capture_google_slides(url=args.url, output_folder=args.output_folder, headless=not args.no_headless)
