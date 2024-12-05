# scripts/main.py
import logging
from scripts.movie_booking import book_movie_ticket
from scripts.utils import setup_logging
from config.settings import LOG_FILE_PATH

if __name__ == "__main__":
    setup_logging(LOG_FILE_PATH)
    logging.info("Starting movie booking automation...")
    try:
        book_movie_ticket()
        logging.info("Booking process completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
