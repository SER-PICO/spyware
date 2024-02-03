# Spyware - Serpico

---

### Server

- **Organization:** Received data from the key logger organized by IP, date and time

---

### Client

- **Keyboard Keystroke Logging:** The spyware records keystrokes from the infected client.
- **Clipboard Logging:** The spyware records text copied into the clipboard.
- **Transmission:** The spyware sends the obtained data to the server every 60 seconds.

---

### Dependencies

- Python 3
- pynput (Python library)
- clipboard (Python library)

---

## Installation

### Client:

1. **Clone the repository to your local machine:**
git clone https://github.com/SER-PICO/spyware.git

3. **Navigate to the client directory:**
cd client

5. **Install dependencies:**
   
### Server:

1. **Clone the repository to your local machine:**
git clone https://github.com/SER-PICO/spyware.git

2. **Navigate to the server directory:**
cd server

---

## Usage

### Server:

- **Open a terminal and navigate to the server directory.**
- **Run the server script with a chosen port number:**
./python3 server.py -l <port>

*Replace `<port>` with your desired port number. Example: ./python3 server.py -l 26431*
- **Run the server BEFORE the client**

### Client:

- **Open a terminal and navigate to the client directory.**
- **Run the client script:**
*Ensure that the server IP address (`ip_server`) and port (`port`) in `client.py` match the server configuration.*

---

### Help:
- **Run the server script with -h:**
./python3 server.py -h
---

### Important Notes

- **Make sure the client and server are on the same network for communication.**
- **(Optionnal) Configure your firewall to allow communication through the specified port.**
- **Use responsibly and only with appropriate permissions.**



