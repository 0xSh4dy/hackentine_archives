FROM pwn.red/jail:0.3.1

COPY --from=ubuntu@sha256:c985bc3f77946b8e92c9a3648c6f31751a7dd972e06604785e47303f4ad47c4c / /srv
COPY flag /srv/app/
COPY orw /srv/app/run