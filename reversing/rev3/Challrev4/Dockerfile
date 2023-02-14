FROM nginx:alpine
COPY ./* /usr/share/nginx/html/
COPY ./img /usr/share/nginx/html/img
ENTRYPOINT ["nginx","-g","daemon off;"]
