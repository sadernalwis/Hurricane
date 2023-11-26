
export class Socket{
    constructor(socket_address) {
        this.socket_address = socket_address ? socket_address : `ws${location.protocol.endsWith('s:') ? 's' :''}://${location.host}/ws`
        this.open_channel(socket_address);
    }

    transmit(message, json){
        if (json!==undefined){ this.socket.send(JSON.stringify({ gatepass: gatepass, parseltongue: parseltongue, payload: payload }));}
        else                 { this.socket.send(message);}
    }

    open_channel(socket_address) {
        let program = this;
        program.socket_address = socket_address;
        program.socket = new WebSocket(program.socket_address);
        program.socket.onopen = function (event) { program.socket_open(event);};
        program.socket.onmessage = function (event) { program.socket_message(event);};
        program.socket.onclose = function (event) { program.socket_close(event);};
        program.socket.onerror = function (error) { program.socket_error(error);};
    }

    socket_open (e) {
        console.log("[socket open] Connection established" + this.socket_address);
    }

    socket_message (event) {
        console.log("[socket message] ", JSON.parse(event.data))
    }
    socket_close (event) {
        if (event.wasClean) { 
            console.log(`[socket close] ${this.socket_address}, code=${event.code} reason=${event.reason}`); }
        else { 
            console.log(`[socket close] ${this.socket_address} Connection died`); } /*  e.g. server process killed or network down event.code is usually 1006 in this case */
        if(this.reconnect){
            this.open_channel(this.socket_address);
        }
    }
    socket_error (error) { 
        alert(`[socket error] ${this.socket_address} ${error.message}`);
    }
}