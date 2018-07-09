FROM golang:alpine AS builder

ADD ./vendor /go/vendor
ADD . /go/src/github.com/eliaszs/erepro/services/branches-gw

WORKDIR /go/src/github.com/eliaszs/erepro/services/branches-gw

RUN apk update && apk add ca-certificates
RUN CGO_ENABLED=0 go install -tags netgo -ldflags '-w'


FROM alpine
COPY --from=builder /go/bin/branches-gw /app
COPY --from=builder /usr/share/ca-certificates /usr/share/ca-certificates
COPY --from=builder /etc/ssl/certs /etc/ssl/certs

ENV HOSTPORT=":9090"
ENV ENDPOINT=":8080"

CMD ["/app"]
