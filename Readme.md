Owner: Tarek R.<br></br>
Contact: https://www.upwork.com/freelancers/~01cb49d3357f7915f8


Disclaimer: This instruction is for Windows OS<br></br>
First Time Setup:
  1. Download Python from https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
  2. Open the downloaded file
  3. Check the box called “Add Python 3.9 to PATH“
  ![add_Python_to_Path](https://user-images.githubusercontent.com/44648395/133729705-585a5085-eb2d-4033-8dc2-3ec5660d101f.png)

  5. Click "Install Now" to and finish the installation normally.
  6. Open Powershell
  7. execute following three commands:<br></br>
    pip3 install selenium<br></br>
    pip3 install undetected-chromedriver<br></br>
    pip3 install pandas<br></br>
  7. Extract the zip into an empty folder where the program will run (basically puting the two file, 'import.csv' and 'Insta Hashtag Survey.py' into a folder).

Usage:
-  create a csv file named import.csv and write "keywords" in the first cell (this is a must. see sample import.csv for example)
-  ![csv file header example](https://user-images.githubusercontent.com/44648395/133727864-44d04745-694f-438e-bd9b-4d81016e297c.png)

-  you must put this csv file in the folder where you extracted the source code (in step 7 above)
-  doubke click "Insta Hashtag Survey.py" file and wait a few moments for the browser to open
-  wait till the browser goes to instagram log in page by itself
-  log in as usual
-  after signing in, when the browser goes to instagram homepage, go back to the python window
-  you will see "Log in and press enter to continue..."
-  so, press enter and sit back :)

 Note - try to scrap less than 800/1000 keywords at a single time and give a fair break between each runs
