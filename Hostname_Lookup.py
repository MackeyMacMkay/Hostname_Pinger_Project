import subprocess
import platform

def ping_hostnames_from_file(input_filename, output_filename="ping_results.txt"):

    try:
        with open(input_filename, 'r') as f:
            hostnames = [line.strip() for line in f if line.strip()]

        if not hostnames:
            print(f"No hostnames found in '{input_filename}'. Please ensure the file is not empty and contains one hostname per line.")
            return

        print(f"Attempting to ping {len(hostnames)} hostnames from '{input_filename}'...")
        print(f"Saving results to '{output_filename}'...\n")

        # Open the output file in write mode. 'w' will create the file if it doesn't exist,
        # or overwrite it if it does.
        with open(output_filename, 'w') as out_f:
            out_f.write(f"--- Ping Results from {input_filename} ---\n\n")

            # Determine the correct ping command based on the operating system
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            # Ping count: 2 packets, to increase speed of task
            count = '2'

            for hostname in hostnames:
                status_message = ""
                print(f"Pinging {hostname}...") # Still print to console for immediate feedback
                try:
                    command = ['ping', param, count, hostname]
                    result = subprocess.run(
                        command,
                        capture_output=True,
                        text=True,
                        check=False
                    )

                    if result.returncode == 0:
                        status_message = f"  {hostname}: REACHABLE"
                    else:
                        status_message = f"  {hostname}: UNREACHABLE"
                        if result.stderr:
                            status_message += f"\n    Error: {result.stderr.strip()}"
                        elif result.stdout:
                            status_message += f"\n    Output: {result.stdout.strip().splitlines()[-1]}"

                except FileNotFoundError:
                    status_message = f"  Error: 'ping' command not found. Please ensure ping is installed and in your system's PATH."
                    print(status_message) # Print error to console immediately
                    out_f.write(status_message + "\n")
                    break # Exit if ping command itself is not found
                except Exception as e:
                    status_message = f"  An unexpected error occurred while pinging {hostname}: {e}"
                    print(status_message) # Print error to console immediately

                print(status_message) # Print status to console
                out_f.write(status_message + "\n") # Write status to file
            out_f.write("\n--- End of Results ---\n")
        print(f"\nPing results saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found. Please ensure the file exists in the correct directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    input_hostname_file = "hostnames.txt"
    output_ping_results_file = "ping_results.txt"

    ping_hostnames_from_file(input_hostname_file, output_ping_results_file)
