#!/usr/bin/env python3

import random
import socketserver

WORDS_FILE = "words.txt"
HOST = "0.0.0.0"
PORT = 1234


class Insulter:
    def __init__(self):
        self.words = []
        with open(WORDS_FILE) as wordsf:
            for line in wordsf:
                self.words.append(line.strip().split())

    def insult(self):
        return " ".join((
            "Thou",
            random.choice(self.words)[0],
            random.choice(self.words)[1],
            random.choice(self.words)[2],
        ))


class InsultHandler(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        self.insulter = Insulter()
        super().__init__(*args, **kwargs)

    def handle(self):
        self.request.sendall(self.insulter.insult().encode("utf-8") + b"\r\n")


if __name__ == "__main__":
    socketserver.TCPServer((HOST, PORT), InsultHandler).serve_forever()
