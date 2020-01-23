from concurrent import futures
import time
import grpc
from base_package import helloworld_pb2
from base_package import helloworld_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'


# 实现 proto 文件中定义的 GreeterServicer
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg=request.name))

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg=request.name))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(_HOST + ':' + _PORT)
    server.start()
    try:
        while True:
            # one day in seconds
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
