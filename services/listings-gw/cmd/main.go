package cmd

import (
	"context"
	"flag"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/codegangsta/negroni"
	"github.com/golang/glog"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"google.golang.org/grpc"

	gw "github.com/eliaszs/erepro-apis/erepro/api/listings/v1"
)

var (
	endpoint = flag.String("endpoint", "localhost:9090", "Endpoint to the service")
	hostport = flag.String("hostport", "localhost:8080", "hostport for the proxy")
)

// Run is the main function of this gateway
func Run() {
	flag.Parse()
	defer glog.Flush()

	log.Println("Starting server " + os.Args[0])

	ctx := context.Background()
	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()

	apiAddr := *endpoint
	if value := os.Getenv("SERVICE"); len(value) != 0 {
		apiAddr = value
	}

	log.Println("Registering gRPC service handler")
	mux := runtime.NewServeMux()
	n := negroni.Classic()
	n.UseHandler(mux)
	opts := []grpc.DialOption{grpc.WithInsecure()}
	err := gw.RegisterListingsHandlerFromEndpoint(ctx, mux, apiAddr, opts)
	if err != nil {
		log.Fatal(err)
	}

	addr := *hostport
	if value := os.Getenv("HOSTPORT"); len(value) != 0 {
		addr = value
	}

	server := http.Server{Addr: addr, Handler: n}
	go func() {
		log.Printf("Listening on %s", addr)
		if err := server.ListenAndServe(); err != http.ErrServerClosed {
			log.Fatalf("fatal error: %s\n", err)
		}
	}()

	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
	<-sigs

	log.Println("Shutting down the server")
}
