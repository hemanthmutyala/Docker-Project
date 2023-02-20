# Docker-Project
Lists the name of all the text file at location: /home/data
Read the two text files and count total number of words in each text files
Add all the number of words to find the grand total (total number of words in both files)
List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
Find the IP address of your machine
Write all the output to a text file at location: /home/output/result.txt (inside your container).
Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

******** Steps to Execute***************

format:
docker build -t [image name]
docker run -v [PATH]:/home/data [image name]

example:
docker build -t mydocr . 
docker run -v /Users/hemanthsmacbook/Desktop:/home/data mydocr
