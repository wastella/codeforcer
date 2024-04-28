from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_problem(link):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = Request(link, headers=hdr)
    except:
        req = Request(link, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')

    problem_html = soup.find_all("div", {"class": "problem-statement"})

    problem_text = problem_html[0].get_text()

    return problem_text
