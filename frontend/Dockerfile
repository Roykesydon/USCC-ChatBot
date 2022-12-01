FROM node:16.14.2

# make the 'app' folder the current working directory
WORKDIR /app

# copy 'package.json' to install dependencies
COPY . .

# install dependencies
RUN npm install

RUN npm install -g @vue/cli-service
RUN npm install -g @vue/cli

# copy files and folders to the current working directory (i.e. 'app' folder)
# COPY . .

EXPOSE 8080

# # build app for production with minification
# RUN npm install -g http-server
# RUN npm run build
# CMD [ "http-server", "dist" ]
CMD ["npm", "run", "serve"]