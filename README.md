# djinni-statistics
Djinni Python technologies statistics


The application allows you to track the most popular technologies among open vacancies in the python section on the Djinni resource.




### Installation
1. To work with the project, you must have python 3.8 or higher installed.
2. Clone the forked repo
    ```
    git clone https://github.com/vadim-kosnovskiy/djinni-statistics
    ```
3. Open the project folder.
4. Install all of the Python modules and packages listed in requirements.txt file to your environment
   ```
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS) 
   pip install -r requirements.txt
   ```

###  Usage

- Run scraper from directory, where is spiders directory
   ```
  cd djinni\djinni (on Windows)
  cd djinni/djinni (on macOS)
  
  scrapy crawl djinni_python -O vacancies.csv

   ```
- Open Jupyter notebook da.ipynb and run
