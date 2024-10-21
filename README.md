# 1.0 EDTeam AI School 

## 1.1 AI for programmers - Path

### 1.1.1 Build APPs with OpenAI API - Course

#### Virtual Environment with MacOS

##### Create and activate a virtual environment
``` bash
python3.12 -m venv .venv
source .venv/bin/activate    
```

##### Install libraries

``` bash
pip3 install openai
pip3 install python-dotenv   
```
##### Save dependencies

``` bash
pip3 freeze > requirements.txt  
```

##### Install dependencies

``` bash
pip3 install -r requirements.txt   
```

#### Virtual Environment with Window

##### Create and activate a virtual environment

``` bash
py -3.12 -m venv .venv
.venv\Scripts\activate  
```

##### Install libraries

``` bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org openai
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org python-dotenv   
```
##### Save dependencies

``` bash
pip freeze > requirements.txt  
```

##### Install dependencies

``` bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt   
```

#### Environment Variables

add environment variables

* openai_api_edt=[__YourAPIKey__]

* openai_organization=[__YourOrganizationID__]

* openai_project=[__YourProjectID__]

``` bash
cd api_openai
touch .env
```

