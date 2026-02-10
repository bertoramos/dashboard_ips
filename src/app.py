import logging
from pathlib import Path

import streamlit as st

from view.components.menu import menu
from view.pages.file_manager import render as render_file_manager
from view.pages.home import render as render_home
from view.pages.dashboard import render as render_dashboard

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def get_logger(name, log_dir=None):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_dir is not None:
        log_path = log_dir / f"{name}.log"
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def main():
    project_dir = Path(__file__).resolve().parent.parent

    # Set up logging
    log_output = project_dir / Path("logs")
    log_output.mkdir(parents=True, exist_ok=True)

    get_logger("ips_dashboard", log_output)

    st.set_page_config(page_title="IPS Dashboard", layout="wide")

    pages = [
        st.Page(render_home, title="Home", url_path="home"),
        st.Page(render_file_manager, title="File Manager", url_path="db_manager"),
        st.Page(render_dashboard, title="Dashboard", url_path="dashboard"),
    ]

    selected = menu(pages)
    if selected is not None:
        selected.run()


if __name__ == "__main__":
    main()
