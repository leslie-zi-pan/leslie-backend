import grpc
from concurrent import futures
import time
import os
import dummy_pb2
import dummy_pb2_grpc

class DummyService(dummy_pb2_grpc.DummyServiceServicer):

    def ProcessData(self, request, context):
        """
        This method processes the incoming data and returns a response.
        """
        print(f"Received request: {request.input_data}")
        # Simulate some processing time
        time.sleep(1)  
        return dummy_pb2.DataResponse(processed_data=f"Processed: {request.input_data}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dummy_pb2_grpc.add_DummyServiceServicer_to_server(DummyService(), server)
    port = os.environ.get('PORT', '8080')  # Get port from environment or default to 8080
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()