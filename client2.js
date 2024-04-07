const WebSocket = require('websocket');

// Create a WebSocket client
const client = new WebSocket.client();

// Connect to the WebSocket server
client.connect('ws://127.0.0.1:8765');

client.on('connect', (connection) => {
    console.log('WebSocket: Client Connected.');

    // Listen for user input
    process.stdin.on('data', (data) => {
        let message = data.toString().trim();

        // Send message to the server
        if (connection && connection.connected) {
        connection.sendUTF(message);
    }

        // Handle exit command
        if (message === 'exit') {
            console.log('Exiting...');
            connection.close();
            process.exit(0);
        }
    });

    // Listen for messages from the server
    connection.on('message', (message) => {
        if (message.type === 'utf8') {
            console.log('Response from server:', message.utf8Data);
        }
    });

    // Handle connection close
    connection.on('close', () => {
        console.log('Connection closed.');
        process.exit(0);
    });

    // Handle connection errors
    connection.on('error', (error) => {
        console.error('Connection error:', error);
        process.exit(1);
    });
});

client.on('connectFailed', (error) => {
    console.error('Connection failed:', error);
    process.exit(1);
});
