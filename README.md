# Fetch
fetch receipt predictor app

Files included in this repository:
  - Fetch(Lin_Reg).ipynb: this is the google colab notebook where I created the linear regression algorithm using Tensorflow which makes the predictions for the monthly receipt totals in 2022
  - app.py: This is the python file where I created the tkinter app to deploy the linear regression model
  - data_daily.csv: is the original csv data file for the project
  - docker image: is just a file that contains the docker pull command you can use to pull the image from GitHub

This is a simple tkinter app that allows you to upload the csv file data_daily.csv, it will then run a linear regression algorithm on the data and return the predicted monthly receipt totals for 2022 and display a simple matplotlib plot of the results.

In order to be able to show the GUI of the app it does require the use of an Xserver and the process is slightly different whether you are on Mac or Windows but below are directions for whichever system you are using.

### Windows

For Windows I used an Xserver which can be downloaded from here https://sourceforge.net/projects/vcxsrv/

Once you have this downloaded you can launch it and it will ask you some display settings:
  - choose Multiple windows, then click next
  - choose Start no client, then click next
  - Then on the Extra settings page make sure to check the box for Disable access control as this will allow the Docker container to interact with the Xserver and then click next and finish.

Now with the Xserver setup make sure you have Docker open and then you can go into your command prompt and run the following: docker pull ghcr.io/jwyatt09/fetch:receipt_predictor

This will pull the docker image from GitHub

Once this process is complete you can run the Docker container but first you will need to have your local IP address. You can find this by going to settings>Network & Internet>then selecting your Wi-Fi or Ethernet and scrolling down to properties where you can find your IPv4 address which should be a number listed in the format xxx.xxx.x.xxx

Now to run the container go to your command prompt and run the following: docker run -it --rm -e DISPLAY=your_local_ip:0 -v /path/to/your/home/directory/.Xauthority:/root/.Xauthority --net=host ghcr.io/jwyatt09/fetch:receipt_predictor
  - Replace "/path/to/your/home/directory" with the actual path to your home directory.
  - Make sure to replace "your_local_ip" with your actual local IP address.

This may take a moment but then the Fetch Receipt Predictor window will pop up.

Once the window pops up at the top you will see Upload CSV file: and underneath this will be a button that says "Upload", clicking this button will bring up a window that will let you select the data_daily.csv file.

Once you have selected the file, you can then click the button that says "Make Predictions for 2022"

This will take a moment to run but then it will populate the window below with the predicted monthly totals for each month of 2022 and below this it will generate a simple barplot of the totals for each month.

### MAC

For Mac I used an Xserver called Xquartz which can be downloaded here https://www.xquartz.org/

Once you have this downloaded you can launch Xquartz it will bring up a terminal window but you can close out of this terminal window we do not need to do anything with it directly we just need to make sure Xquartz is running in the background.

Now make sure you have Docker running then open up a terminal window and run the following: docker pull ghcr.io/jwyatt09/fetch:receipt_predictor

This will pull the docker image from GitHub

Once this process is complete we can run the Docker container but first you will need to have your local IP address. You can find this by going to system settings>then choosing your Wi-Fi or ethernet connection details which will then display your local IP address which should be a number listed in the format xxx.xxx.x.xxx

On Mac you will need to add your IP address to the access control list. You can do this in the terminal by running the following: xhost +your_local_ip
  - replace 'your_local_ip' with your actual local IP address
  - it will let you know that your IP address is being added to the access control list

Now that your IP address has been added to the access control list you can run the docker image by entering the following into your terminal: docker run -e DISPLAY=your_local_ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix ghcr.io/jwyatt09/fetch:receipt_predictor
  - replace 'your_local_ip' with your actual local IP address

This may take a moment but then the Fetch Receipt Predictor window will pop up.

Once the window pops up at the top you will see Upload CSV file: and underneath this will be a button that says "Upload", clicking this button will bring up a window that will let you select the data_daily.csv file.

Once you have selected the file, you can then click the button that says "Make Predictions for 2022"

This will take a moment to run but then it will populate the window below with the predicted monthly totals for each month of 2022 and below this it will generate a simple barplot of the totals for each month.
