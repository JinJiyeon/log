#!/bin/bash

# Program to output a system information page

title="System Information Report For $HOSTNAME"
current_time="$(date +"%x %r %Z")"
timestamp="Generated $current_time, by $USER"

cat << _EOF_ 
<html>
        <head>
          <title>$title</title>
        </head>
        <body>
          <h1>$title</h1>
		  <p>$timestamp</p> 
        </body>
</html>
_EOF_
