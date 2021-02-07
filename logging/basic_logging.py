import logging

def main():
    logging.basicConfig(level=logging.DEBUG, filename="output.log")

    logging.debug("DEBUG")
    logging.info("INFO")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")

if __name__ == "__main__":
    main()