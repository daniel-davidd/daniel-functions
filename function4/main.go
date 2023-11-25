package main

import (
	"encoding/json"

	"github.com/memphisdev/memphis-functions.go/memphis"
)

type Event struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func eventHandlerFunc(msgPayload []byte, msgHeaders [string]string, inputs [string]string) ([]byte, map[string]string, error) {
	// Get data from msgPayload
	var event Event
	json.Unmarshal(msgPayload, &event)

	if event.Age%2 == 0 {
		return nil, nil, nil
	}

	eventBytes, _ := json.Marshal(event)
	return eventBytes, msgHeaders, nil
}

func main() {
	memphis.CreateFunction(eventHandlerFunc)
}
