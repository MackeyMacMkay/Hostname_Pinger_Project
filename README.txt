DESCRIPTION:
This script is designed to look at a hostnames text file and ping each hostname, checking for connectivity.

DEPENDENCIES:
1. Create a txt file named "hostnames.txt" within the same directory as the script
2. Input the hostnames on their own individual lines and save the hostnames.txt file

FUNCTION:
The script will ping each individual hostname, one by one (this may take a little bit of time depending on number of hostnames). Once complete, it will create a file named ping_results.txt in the same directory as the script.

USAGE: 
Troubleshooting connectivity to multiple hosts at once.

EXAMPLE:
An example output, showing success and failures, in the ping_results.txt file will look as follows:

--- Ping Results from hostnames.txt ---

  google.com: REACHABLE
  weather.com: REACHABLE
  microcenter.com: UNREACHABLE
    Output:     Packets: Sent = 2, Received = 0, Lost = 2 (100% loss),
  linkedin.com: REACHABLE

--- End of Results ---