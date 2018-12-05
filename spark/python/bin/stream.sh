#!/usr/bin/env sh
rm /tmp/streamlog
touch /tmp/streamlog
tail -f /tmp/streamlog | nc -lk 7777 &
TAIL_NC_PID=$!
sleep 2
cat ./data/logs/log1.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log2.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log3.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log4.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log5.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log6.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log7.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log8.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log9.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log10.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log11.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log12.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log13.log >> /tmp/streamlog
sleep 2
cat ./data/logs/log14.log >> /tmp/streamlog
sleep 2
kill $TAIL_NC_PID
