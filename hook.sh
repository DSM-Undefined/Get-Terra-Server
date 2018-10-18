git pull 
kill $(ps a | grep python | grep -v "grep" | awk '{print $1}')
python3 server.py