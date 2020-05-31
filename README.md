# InShorts API
---

An API that fetches and returns news, including headline and content, from www.inshorts.com
---

[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](https://documenter.getpostman.com/view/7941616/Szf6WnxK?version=latest) 


## Instructions to run

```
$ git clone https://github.com/Shreya549/InShortsScraper
$ cd InShortsScraper
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

## URL

  `https://limitless-shelf-94834.herokuapp.com/scrape`

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
        'url': 'https://limitless-shelf-94834.herokuapp.com/scrape?category=sports',
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

    url = "https://limitless-shelf-94834.herokuapp.com/scrape?category=sports"

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

    fetch("https://limitless-shelf-94834.herokuapp.com/scrape?category=sports", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
      
  * **cURL - cURL**
  
    ```
    curl --location --request GET 'https://limitless-shelf-94834.herokuapp.com/scrape?category=sports'
    
<p align="center">
	With :heart: by <a href="" target="_blank">Shreya Chatterjee</a>
</p>
    
      

    
  



