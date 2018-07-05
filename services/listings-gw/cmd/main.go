package main

import (
	"context"
	"flag"
	"log"
	"net/http"
	"os"

	"github.com/golang/glog"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"google.golang.org/grpc"

	gw "github.com/eliaszs/erepro-apis/erepro/api/listings/v1"
)

var (
	endpoint = flag.String("endpoint", "localhost:9090", "Endpoint to the service")
	hostport = flag.String("hostport", "localhost:8080", "hostport for the proxy")
)

func run() error {
	log.Println("Starting server " + os.Args[0])

	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	log.Println("Registering gRPC service handler")
	mux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}
	err := gw.RegisterListingsHandlerFromEndpoint(ctx, mux, *endpoint, opts)
	if err != nil {
		return err
	}

	log.Printf("Listening on %s\n", *hostport)
	return http.ListenAndServe(*hostport, mux)
}

func main() {
	flag.Parse()
	defer glog.Flush()

	if err := run(); err != nil {
		glog.Fatal(err)
	}
}
