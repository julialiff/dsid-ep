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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import projeto_DSID_pb2
import projeto_DSID_pb2_grpc


def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = projeto_DSID_pb2_grpc.GreeterStub(channel)
	# response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
	# print("Greeter client received: " + response.message)
	# response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
	# print("Greeter client received: " + response.message)
	
	response = stub.ChamadaVoid(projeto_DSID_pb2.RequestLong())
	print("Greeter client received from void call: ")

	response = stub.ChamadaLong(projeto_DSID_pb2.RequestLong(num=99999999999))
	print("Greeter client received from long call: " + str(response.message))
	
	response = stub.Chamada8Long(projeto_DSID_pb2.Request8Long( num1=99999999999,num2=99999999999,num3=99999999999,num4=99999999999,num5=99999999999,num6=99999999999,num7=99999999999,num8=99999999999, ))
	print("Greeter client received from 8 long call: " + str(response.message))
	
	for n in range(11):
		response = stub.ChamadaString(projeto_DSID_pb2.RequestString(name="a"*2**n))
		print("Greeter client received from string call: " + str(response.message))
		
	

if __name__ == '__main__':
    run()



