# Hostname Connectivity Checker (Python Script)

This Python script automates the process of checking network connectivity to a list of hostnames. It reads hostnames from a specified input text file, pings each one, and records the results (reachable or unreachable) to an output text file.

## Features
* Reads hostnames from a user-defined input file (e.g., `hostnames.txt`).
* Pings each hostname using the system's `ping` utility.
* Determines OS (Windows/Linux/macOS) to use the correct `ping` parameters.
* Outputs connectivity status (reachable/unreachable) for each hostname.
* Saves all results to a specified output file (e.g., `ping_results.txt`).
* Provides real-time console feedback during the ping process.
* Includes basic error handling for file not found and `ping` command issues.

## How to Use
* Input hostnames into hostnames.txt (file must be in the same directory as Hostname_Lookup.py)
* Run Hostname_Lookup.py

### Prerequisites
* Python 3.x installed on your system.

### Setup
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YourGitHubUsername/Hostname_Pinger_Project.git](https://github.com/YourGitHubUsername/Hostname_Pinger_Project.git)
   cd Hostname_Pinger_Project# Hostname_Pinger_Project
