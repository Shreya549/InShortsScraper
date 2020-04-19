**InShorts API**
---

An API that fetches and returns news, including headline and content, from www.inshorts.com

* **URL**

  `https://limitless-shelf-94834.herokuapp.com`

* **Method**

  `GET`

* **URL Params**

  **Required:**

    `category = [String]`

* **Success Response**

  * **Code:** `HTTP 200 OK`
  * **Content:** `{"news": [ {"headline": "headline_data","content": "content_data"} ] }`
       
* **Error Response:**

  * **Code:** `HTTP 404 Not Found`
  
* **Sample Call:**

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
    
      

    
  



