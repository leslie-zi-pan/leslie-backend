
import grpc
from concurrent import futures
import dummy_pb2
import dummy_pb2_grpc

class DummyService(dummy_pb2_grpc.DummyServiceServicer):

  def ProcessData(self, request, context):
    # Process the data (e.g., make a prediction)
    return dummy_pb2.DataResponse(processed_data=request.input_data)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  dummy_pb2_grpc.add_DummyServiceServicer_to_server(DummyService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
  serve()