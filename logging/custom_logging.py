import logging

def add():
    logging.info("OKA")
    return "ok"

def main():
    format_log = "%(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    logging.basicConfig(level=logging.DEBUG, filename="output.log", format=format_log)

    logging.debug("DEBUG")
    logging.info("INFO")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")
    add()

if __name__ == "__main__":
    main()