To SSH into the VM Instance we can use a command like this:
ssh -i <full-key-path> azureuser@<public-ip>

The command I used was as follows:
ssh -i /home/arvind/arvindazfundamentalsvm_key.pem azureuser@172.173.166.74

Incase you need the key pair to verify the working of the flask app, please contact me at arvind.kishore@tigeranalytics.com.

After performing SSH, you need to export the flask file as an environment variable in order to make it work:
export FLASK_APP=flask_file_app_v1.py

Once exported we can run the flask app using:
flask run -h 0.0.0.0

The URL for the flask app is of the form:
http://<public-ip>:5000/list-files?folder_name=<folder_name>

I have created three folders in the storage container namely folder 1,2 and 3 with one file indicative of the folder name inside each:	
Example usage: http://172.173.166.74:5000/list-files?folder_name=folder3	