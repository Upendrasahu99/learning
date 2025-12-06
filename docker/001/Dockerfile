## base image we can make ubuntu also
# FROM ubuntu 

## base image
FROM node:22-alpine

## working directory
WORKDIR /app

## Copy everything to working directory ex. index.js, package.json, node_modules etc.
## we can copy specific file also "COPY ./index.js ./index.js"
COPY . .

## Run command to build the code
RUN npm install

## Expose Port
EXPOSE 3000


## Final command that runs when running the container
CMD ["node", "index.js"]