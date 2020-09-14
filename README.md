# challenge
## Challenge Solution for Inovola
### IV: Use Cases:
### All Espresso Machines: 
##### . EM001<br /> . EM002<br />. EM003<br /> 
### All Small Pods:
##### . CP001<br /> · CP003 <br />· CP011 <br />· CP013<br />· CP021<br /> · CP023 <br /> · CP031<br />· CP033 <br />· CP041 <br />· CP043 <br />

### V. It Is deployed on an EC2 instance to make it easier visually to try.<br />  Tech used for deployment: Docker, Nginx, Gunicorn, Whitenoise
### Also there are two End Points To upload the the data as json files.
#### Here Are the end points:
###### *No Authentication is required, to be able to try posting products using one_time_startup() in post_data.py
#### api/create-machine/ <br />api/create-pod/<br />api/get-machine/<br />api/get-pod/
#### Some Examples of filtering:
#### api/get-pod/?pack_size=3 <br/> api/get-pod/?coffee_flavor=vanilla&pack_size=3
#### api/get-machine/?water_line_compatible=true  <br/> api/get-machine/?model_type=deluxe&water_line_compatible=true
