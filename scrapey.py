# Import libraries
import streamlit as st
from bs4 import BeautifulSoup
import requests

st.title("Link Scraper")


def show():

    # Prompt user to enter the URL
    url = st.text_input(value="https://canadacouncil.ca/", label="Input url below")

    # Make a request to get the URL
    page = requests.get(url)

    # Get the response code of given URL
    response_code = str(page.status_code)

    # Display the text of the URL in str
    data = page.text

    # Use BeautifulSoup to use the built-in methods
    soup = BeautifulSoup(data)

    # Iterate over all links on the given URL with the response code next to it
    for link in soup.find_all('a'):
      st.write(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")

if __name__ == "__main__":
    show()