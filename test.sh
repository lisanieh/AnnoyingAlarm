pid_of_stats="$(ps aux | grep stats.py | awk '{print $2}' | head -n1)"
echo $pid_of_stats
kill $pid_of_stats

