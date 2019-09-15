# geocurator

**geocurator** curates customers based on the distance to a reference location. Location points are given as (Latitude, Longitude).


## Quick start

The quickest way for running this is by pulling the latest container. That only requires `docker` installed (you may need to `sudo` commands below):

```bash
docker run montenegrodr/geo_curator:latest
```

or, at this repository root:

```
make run-image
```

## Development

This python library requires **Python 3.6** or superior. For local build, it is recommended to use a virtual environment. Install requirements and geocurator library with (you may need to `sudo` commands below):

```bash
make build
```

And then run it:

```bash
make run
```

That uses default values that can be changed by overriding these environment variables:

```bash
INPUT_FILE_NAME    # input text file
OUTPUT_FILE_NAME   # output text file
REFERENCE_LAT      # reference latitude
REFERENCE_LONG     # reference longitude
RADIUS             # distance threshold
MONITOR            # prometheus monitor port
```

For instance:
```
REFERENCE_LAT=21.0227387 REFERENCE_LONG=105.8194541 make run
```

Run tests for a sanity check (you expect to see an `OK`):

```
make test
```

# Deployment


Build a new image:

```
make build-image
```

Publish new container image to registry:

```
make push-image
```

Override these variables to change default registry, version or repository name:

```make
REGISTRY        # docker registry 
VERSION         # container image version tag  
REPOSITORY      # docker repository
```
