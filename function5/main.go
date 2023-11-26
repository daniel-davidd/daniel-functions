package memphis

import (
	"context"
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
)

type MemphisMsg struct {
	Headers map[string]string `json:"headers"`
	Payload string            `json:"payload"`
}

type MemphisMsgWithError struct {
	Headers map[string]string `json:"headers"`
	Payload string            `json:"payload"`
	Error   string            `json:"error"`
}

type MemphisEvent struct {
	Inputs   map[string]string `json:"inputs"`
	Messages []MemphisMsg      `json:"messages"`
}

type MemphisOutput struct {
	Messages       []MemphisMsg          `json:"messages"`
	FailedMessages []MemphisMsgWithError `json:"failed_messages"`
}

type EventHandlerFunction func([]byte, map[string]string, map[string]string) ([]byte, map[string]string, error)

func CreateFunction(eventHandler EventHandlerFunction) {
	LambdaHandler := func(ctx context.Context, event *MemphisEvent) (*MemphisOutput, error) {
		var processedEvent MemphisOutput
		for _, msg := range event.Messages {

			fmt.Println("Processing message")
			fmt.Println(msg)
		}
		return &processedEvent, nil

	}
	lambda.Start(LambdaHandler)

}
