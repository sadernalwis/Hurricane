# HURRICANE

### Tornado based Websocket

> Run Backend
```bash
python3 Hurricane.py
```

> Run Frontend
```javascript
import { Socket } from "Hurricane/Frontend/Socket.js"
const socket = new Socket() // Socket('ws://192.168.1.1:8081/ws') 
socket.transmit("hello")
socket.transmit(null, {name:"ALice", age:"21"})

socket.socket_open  = (event)=>{ console.log("overriden function") } 
socket.socket_message  = (event)=>{ console.log("overriden function") } 
socket.socket_close  = (event)=>{ console.log("overriden function") } 
socket.socket_error  = (error)=>{ console.log("overriden function") } 

```