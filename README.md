# Run a application on Docker 

### Build Image From Docker File using Following Command

`podman image build -t myapp .`

### List Image using Following Image

`podman image ls`

### Run a Container in Background using image we just build

`mkdir /data`

`podman container run -d --name myapp -p 8080:8080 -v /data:/data:Z myapp`

### Verify Container is Running

`podman ps`

### Create Systemd Daemon of given Container

`mkdir ~/.config/systemd/user`

`cd ~/.config/systemd/user`

`podman generate systemd --name myapp --new --files`

`systemctl --user enable container-myapp.service`

`systemctl --user start container-myappp.service`

### Reboot System and check your container will be in running state

`podman ps`

### Check application is working or not by following command 

`curl localhost:8080`

### now put some files in /data and check if applicaiton if picking them up or not 

`touch /data/it /data/is /data/awesome /data/hohoho`

`curl localhost:8080`



#### Happy Learning! :-)
