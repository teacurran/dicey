FROM node:20.11.0-bookworm

USER root

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install
COPY . .

EXPOSE 5173

# allows us to run it on a Virtual Machine.
#RUN npm config set unsafe-perm true

CMD [ "npm", "run", "dev" ]

