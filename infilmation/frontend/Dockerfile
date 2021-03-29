from node:14-alpine as build

ENV WORKDIR=/app

WORKDIR $WORKDIR

COPY ./package*.json $WORKDIR/

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
RUN npm install

COPY ./ $WORKDIR/

EXPOSE 3000

CMD ["npm", "start"]
