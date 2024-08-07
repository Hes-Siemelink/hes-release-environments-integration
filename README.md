# _Template Project for Digital.ai Release Integrations_

_This project serves as a template for developing a Python-based container plugin._

_See [How to create a new project](#how-to-create-a-new-project) below_

---

# Digital.ai Release integration to TARGET by PUBLISHER

⮕ Insert description here

---
## How to build and run

This section describes the quickest way to get a setup with Release to test containerized plugins using the SDK Development environment. For a production setup, please refer to the documentation. <!-- XXX insert link to documentation -->

### Prerequisites

You need to have the following installed in order to develop Python-based container tasks for Release using this project:

* Python 3
* Git
* Docker

### Start Release

We will run Release within a local Docker environment. In the development setup, the Release server will manage containerized tasks in Docker.

Start the Release environment with the following command

```commandline
cd dev-environment
docker compose up -d --build
```

### Configure your `hosts` file

The Release server needs to be able to find the container images of the integration you are creating. In order to do so the development setup has its own registry running inside Docker. Add the address of the registry to your local machine's `hosts` file.

**Unix / macOS**

Add the following entry to `/etc/hosts` (sudo privileges is required to edit):

    127.0.0.1 container-registry

**Windows**

Add the following entry to `C:\Windows\System32\drivers\etc\hosts` (Run as administrator permission is required to edit):

    127.0.0.1 container-registry


### Build & publish the plugin

Run the build script

**Unix / macOS**

```commandline
sh build.sh 
```

**Windows**

```commandline
build.bat 
```

The above command builds the zip, creates the container image, and then pushes the image to the configured registry.

`build.bat --zip` Builds the zip.

`build.bat --image` Creates the container image, and then pushes the image to the configured registry.

### Install plugin into Release

There are two ways to install the plugin into Release.

**Install plugin via commandline**

Update the Release server details in `release-integration-template-python/.xebialabs/config.yaml`

Run the command for Unix / macOS:
```commandline
sh build.sh --upload 
```

Run the command for Windows:
```commandline
build.bat --upload 
```
The above command builds the zip, creates the container image, pushes the image to the configured registry, and uploads the zip to the release server.

**Install plugin via Release server UI**

In the Release UI, use the Plugin Manager interface to upload the zip from `build`.
The zip takes the name of the project, for example `release-integration-template-python-1.0.0.zip`.

Then:
* Refresh the UI by pressing Reload in the browser.

### 5. Test it!

Create a template with the task **Container Example: Hello** and run it!

### 6. Clean up

Stop the development environment with the following command:

    docker compose down

