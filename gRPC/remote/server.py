# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import projeto_DSID_pb2
import projeto_DSID_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(projeto_DSID_pb2_grpc.GreeterServicer):

    # def SayHello(self, request, context):
    #     return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    # def SayHelloAgain(self, request, context):
    #     return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)

    # def ChamadaSemValor(self, request, context):
    #     pass
    def ChamadaVoid(self, request, context):
        return projeto_DSID_pb2.ReplyLong()

    def ChamadaLong(self, request, context):
        return projeto_DSID_pb2.ReplyLong(message=request.num)

    def Chamada8Long(self, request, context):
        return projeto_DSID_pb2.ReplyLong(message=request.num2)

    def ChamadaString(self, request, context):
        return projeto_DSID_pb2.ReplyString(message=request.name)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    projeto_DSID_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
