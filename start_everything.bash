#!/bin/bash

# Function to check if a tmux session exists
session_exists() {
    tmux has-session -t $1 2>/dev/null
}

# Function to kill a tmux session if it exists
kill_session() {
    if session_exists $1; then
        tmux kill-session -t $1
    fi
}

echo "ensuring python packages, this could take a while..."
pip install -r requirements.txt > /dev/null 2>&1

if [[ "$*" == *--model* ]]; then
    kill_session server_model
    tmux new-session -d -s server_model 'cd src && python3 server_model.py'
    echo "Model server started, connect to it with \"tmux a -t server_model\""
    echo "Note: the server might take some time to get ready"
fi

if [[ "$*" == *--watcher* ]]; then
    kill_session server_watcher
    tmux new-session -d -s server_watcher 'cd src && python3 server_watcher.py'
    echo "Watcher server started, connect to it with \"tmux a -t server_watcher\""
fi

if [[ "$*" == *--mail* ]]; then
    kill_session server_mail
    tmux new-session -d -s server_mail 'cd src && python3 server_mail.py'
    echo "Mail server started, connect to it with \"tmux a -t server_mail\""
fi
