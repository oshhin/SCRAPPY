## SCRAPPY
### Web Scraping Project with Scrapy

This project demonstrates a basic setup for web scraping using the Scrapy framework in Python. It includes features such as proxy rotation and user-agent rotation for enhanced anonymity and robustness.

## Directory Structure

> bot/ 
> ├ ── bot/ 
>  │ ├── **init**.py # Initialization file for Python
> package   
> │ ├── **settings.py** # Scrapy settings and configurations   │
> └── spiders/   
> │ └── **proxy_spider.py**# Example Scrapy spider for web
> scraping    
> ├── **proxy_list.txt** # List of proxy servers for rotation   
> ├── **user_agent_list.txt** # List of user-agent strings for rotation   
> └── **run_spider.py** # Script to initiate web scraping process

## Files

- **`proxy_list.txt`**: Contains a list of proxy servers used for proxy rotation.
- **`user_agent_list.txt`**: Contains a list of user-agent strings used for user-agent rotation.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/godlyharry/SCRAPPY.git
   cd SCRAPPY
   pip install -r requirements.txt
 2. **Usage:** 
 `python run_spider.py
`This script initializes the Scrapy `CrawlerProcess` with configured settings and starts the scraping process using the `ProxySpider` defined in `bot/spiders/proxy_spider.py`.
2. **Contributing**
Contributions are welcome! Fork the repository and submit a pull request with your enhancements.
4. **License**
This project is licensed under the MIT License - see the [License](https://github.com/godlyharry/SCRAPPY/blob/main/LICENSE) file for details.




