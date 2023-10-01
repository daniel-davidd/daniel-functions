package main

import (
	"context"
	"fmt"

	helper "github.com

	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
	Data string `json:"data"`
}

func HandleRequest(ctx context.Context, name MyEvent) (string, error) {
	return fmt.Sprintf("Hello %s!", helper.GetName(name)), nil
}

func main() {
	lambda.Start(HandleRequest)
}
