import asyncio
import websockets
import json

async def connect_to_tobii_pro_lab():
    uri = "ws://localhost:8080/project?client_id=TestClient"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Connection established successfully")
            
            # Request media list
            media_request = {
                "operation": "ListMedia"
            }
            await websocket.send(json.dumps(media_request))
            media_response = await websocket.recv()
            print("\nMedia list:")
            print(media_response)
            
            # Request participant list
            participant_request = {
                "operation": "ListParticipants"
            }
            await websocket.send(json.dumps(participant_request))
            participant_response = await websocket.recv()
            print("\nParticipant list:")
            print(participant_response)
    
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed unexpectedly")
    except websockets.exceptions.WebSocketException as e:
        print(f"WebSocket error: {e}")
    except ConnectionRefusedError:
        print("Connection refused. Make sure Tobii Pro Lab is running and the WebSocket server is enabled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Connecting to Tobii Pro Lab...")
    asyncio.run(connect_to_tobii_pro_lab())
