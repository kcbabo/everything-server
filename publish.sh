#!/bin/sh

# note that we'll need to build separately on newer versions of arctl past 0.0.8

arctl mcp publish everything-server --docker-url docker.io/kcbabo --github https://github.com/kcbabo/everything-server --push --version 2.0.2 --platform linux/amd64,linux/arm64