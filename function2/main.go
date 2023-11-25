package main

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/memphisdev/memphis-functions.go/memphis"
)

type Event struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func eventHandlerFunc(msgPayload []byte, msgHeaders map[string]string, inputs map[string]string) ([]byte, map[string]string, error) {
	// Get data from msgPayload
	var event Event
	json.Unmarshal(msgPayload, &event)

	time.Sleep(60 * time.Second)

	event.Name = fmt.Sprintf("%v %v", event.Name, event.Age)
	eventBytes, _ := json.Marshal(event)
	return eventBytes, msgHeaders, nil
}

func main() {
	memphis.CreateFunction(eventHandlerFunc)
}
