# fetch
fetch receipt predictor app

This is a simple tkinter app that allows you to upload the csv file data_daily.csv it will then run a linear regression algorithm on the data and return the predicted monthly receipt totals for 2022 and display a simple matplotlib plot of the results.

In order to be able to show the GUI of the app it does require the use of an Xserver and the process is slightly different whether you are on Mac or Windows but below are directions for whichever system you are using.

### Windows

For Windows I used an Xserver which can be downloaded from here https://sourceforge.net/projects/vcxsrv/

Once you have this downloaded you can launch it and it will ask you some display settings:
  - choose Multiple windows, then click next
  - choose Start no client, then click next
  - Then on the Extra settings page make sure to check the box for Disable access control as this will allow the Docker container to interact with the Xserver and then click next and finish.
  - 
Now with the Xserver setup make sure you have Docker open and then you can go into your command prompt and run the following: docker pull ghcr.io/jwyatt09/fetch:receipt_predictor

This will pull the docker image from GitHub

Once this process is complete we can run the Docker container but first you will need to have your local IP address. You can find this by going to settings>Network & Internet>then selecting your Wi-Fi or Ethernet and scrolling down to properties where you can find your IPv4 address which should be a number listed in the format xxx.xxx.x.xxx

Now to run the container go to your command prompt and run the following: docker run -it --rm -e DISPLAY=your_local_ip:0 -v /path/to/your/home/directory/.Xauthority:/root/.Xauthority --net=host ghcr.io/jwyatt09/fetch:receipt_predictor
  - Replace "/path/to/your/home/directory" with the actual path to your home directory.
  - Make sure to replace "your_local_ip" with your actual local IP address.

This may take a moment but then the Fetch Receipt Predictor window will pop up.

Once the window pops up at the top you will see Upload CSV file: and underneath this will be a button that says "Upload", clicking this button will bring up a window that will let you select the data_daily.csv file.

Once you have selected the file, you can then click the button that says "Make Predictions for 2022"

This will take a moment to run but then it will populate window below with the predicted monthly totals for each month of 2022 and below this it will generate a simple barplot of the totals for each month.
