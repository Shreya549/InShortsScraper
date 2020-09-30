# InShorts API

> <Subtitle>
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Shreya549/InShortsScraper?logo=github&style=social)](https://github.com/Shreya549/) [![GitHub last commit](https://img.shields.io/github/last-commit/Shreya549/InShortsScraper?style=social&logo=git)](https://github.com/Shreya549/) [![GitHub stars](https://img.shields.io/github/stars/Shreya549/InShortsScraper?style=social)](https://github.com/Shreya549/InShortsScraper/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Shreya549/InShortsScraper?style=social&logo=git)](https://github.com/Shreya549/InShortsScraper/network)
> An API that fetches and returns news, including headline and content, from www.inshorts.com



[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](https://documenter.getpostman.com/view/7941616/Szf6WnxK?version=latest) 

---


## Instructions to run

```
$ git clone https://github.com/Shreya549/InShortsScraper
$ cd InShortsScraper
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

## Contributors
  <a href="https://github.com/Shreya549">Shreya Chatterjee</a>

## URL

  `https://scrape-inshorts.herokuapp.com/scrape`

## Method

  `GET`
      

## URL Params

  **Required:**

   `category = [String]`

## Success Response

  * **Code:** `HTTP 200 OK`
  * **Content:** `{"news": [ {"headline": "headline_data","content": "content_data"} ] }`
       
## Error Response:

  * **Code:** `HTTP 404 Not Found`
  
## Sample Call:

  * **NodeJs - Request:**

    ```
    var request = require('request');
      var options = {
        'method': 'GET',
        'url': 'https://scrape-inshorts.herokuapp.com/scrape?category=sports',
        'headers': {
           }
        };
    request(options, function (error, response) { 
      if (error) throw new Error(error);
      console.log(response.body);
    });
    
  * **Python - Requests:**
    
    ```
    import requests

    url = "https://scrape-inshorts.herokuapp.com/scrape?category=sports"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    
    print(response.text.encode('utf8')) 
    
  * **JavaScript - Fetch:**
  
    ```
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };

    fetch("https://scrape-inshorts.herokuapp.com/scrape?category=sports", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
      
  * **cURL - cURL**
  
    ```
    curl --location --request GET 'https://scrape-inshorts.herokuapp.com/scrape?category=sports'
    
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

    
<p align="center">
	With :heart: by <a href="" target="_blank">Shreya Chatterjee</a>
</p>
    
      

    
  



