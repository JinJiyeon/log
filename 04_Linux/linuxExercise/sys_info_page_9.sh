#!/bin/bash

# Program to output a system information page

title="System Information Report For $HOSTNAME"
current_time="$(date +"%x %r %Z")"
timestamp="Generated $current_time, by $USER"

report_uptime () {
  echo "<h2>System Uptime</h2>
        <pre>$(uptime)</pre>"
  return
}

report_disk_space () {
  echo "<h2>Disk Space Utilization</h2>
        <pre>$(df -h)</pre>" 
  return
}

report_home_space () {
  if [[ "$(id -u)" -eq 0 ]]; then
    echo "<h2>Home Space Utilization</h2>
          <pre>$(sudo du -sh /home/*)</pre>" 
  else
    echo "<h2>Home Space Utilization ($USER)</h2>
          <pre>$(du -sh $HOME)</pre>"
  fi
  return
}

cat << _EOF_ 
<html>
        <head>
          <title>$title</title>
        </head>
        <body>
          <h1>$title</h1>
		  <p>$timestamp</p> 
		  $(report_uptime)
		  $(report_disk_space)
		  $(report_home_space)
        </body>
</html>
_EOF_
