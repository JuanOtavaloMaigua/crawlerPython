# Craler with BeautifulSoup
Crawler to get names of hotels and users from paper: https://www.sciencedirect.com/science/article/abs/pii/S0950705119302862  
This crawler is for TripAdvisor data set
# How to use?
  * crawler.py: contains all the code of crawler with Beautiful Soup  
    Also, contains the links with all hotels from TripAdvisor
  * dataProcessing.py: contains all code to extract names of users and
    hotels. Removing characters like: !"#$%&/(). Also, Change numbers
    with words, example: juan90 become to juanninety.

Note: All user names in other languages was removed. 
These codes was developed in Pycharm
