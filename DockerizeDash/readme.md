# Dockerize Dash
This section contains the quick-start note for dockerizing Plotly and Dash for your solution. We would go over the tips on writing the <i>Dockerfile</i> and the dependent Python scripts.
<br><br>
You may read the instructions in this Medium Post: <a href="https://medium.com/@jjsham/dockerizing-plotly-dash-5c23009fc10b">Dockerizing Plotly/Dash</a>

## Dockerfile
Beside copying the scripts to the docker container, you would need to install the right version of dependencies in order to have Dash run properly. Here are the important note:
<ul>
	<li>Beside Plotly and Dash, <b>You must include flask v2.1.3</b></li>
	<li><b><i>werkzeug</i> must be v2.0.3</b> which is downloaded from this <a href="https://github.com/pallets/werkzeug/archive/refs/tags/2.0.3.tar.gz">repository</a>. It is also included in the <i>Dockerfile</i></li>
</ul>


### Note on Python Scripts
When initiate the Dash app object, <b>the host must be set at 0.0.0.0</b> in order for the local environment to access the container environment.

```
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=9000)
```
<br>
Since we have set the port to 9000 here, the dashboard will be ran in port 9000 in the <b>Container environment</b>.

## How to Run?
Once you have Dockerfile ready, then:
<ol>
	<li>Build the docker image (<b>Be sure to include "." for the Dockerfile path</b>)</li>
	<li>Run and create a docker container</li>
	<li>Access the dashboard on your browser with the right port number</li>
	</ol>
<br>
See the code below, given we have declared port at 9000 in the container environment.

```
# Build the docker image
docker build -t [image_name] .

# Run and create a docker container
docker run -h localhost -p 9002:9000 -d --name [container_name] [image_name]
```

<br>
In the code above, we have expose the dashboard at port 9000 in the local environment. It means once we access port 9000 in the local environment, it would redirect us to the port 9002 in the container environment.
<br><br>
Note: This example we have set local machine port at 9002 and container port 9000 (According to the port declared in the Python script). You may choose other port number.


## Reference
Troubleshoot Host Error <a href="https://community.plotly.com/t/running-dash-app-in-docker-container/16067">Running dash app in docker container</a> in the Plotly Community
<br><br>
Troubleshoot Werkzeug Error <a href="https://stackoverflow.com/questions/71654590/dash-importerror-cannot-import-name-get-current-traceback-from-werkzeug-debu">Dash ImportError</a> in Stack Overflow