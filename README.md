# Initialising Jenkins

##### 1. Launch a Jenkins container
Hit the following command.
```shell
docker-compose up
```
it would create necessary files in `jenkins_data` to launch and start listening to localhost with `port.8080` for the web interface.

##### 2. Open Jenkins web interface
Open a web browser anything you like and click [Jenkins web page](http://localhost:8080) for the ready initial setup.

##### 3. Set up the admin user
Jenkins would ask you the password created automatically and it needs to set up the admin user for the first time.
you can see the password in the 
`docker-compose` prompt or the `jenkins_data/secrets/initialAdminPassword` file.
Enter the password then push the `Continue` button, Jenkins would continue on setting up.

##### 4. Install the recommendation plugins
Push `Install suggested Plugins` then Jenkins starts the installation of the plugins.

##### 5. Create a user
After finishing installing the plugin, Jenkins would ask you a new user.
Insert appropriate information in each form then push the `Save and Continue` button.

##### 6. Instance configuration
Enter the `Save and Finish` button without changing.


##### 7. Stop Jenkins
Hit `Ctrl+C` on `docker-compose` prompt to stop.
you will finish the Initialising Jenkins!

# Restore jobs configuration data
Hit the following command.
```shell
cp -r backup/jobs/* jenkins_data/jobs
```
This command would copy all jobs file for the tutorial to the current Jenkins home directory.
you need to restart Jenkins to load these configurations with the following command.
```shell
docker-compose up -d
```
All settings up are finished and you can enjoy the Jenkins test tutorial!