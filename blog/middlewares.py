def my_middleware(get_response):
      #initalizes only one time 
      print('One time initialization')
      def my_func(request):
            print('This will be Executed Before the view')
            response = get_response(request)
            print('this will be executed after the view')
            return response
      return my_func


class SampleMiddlewareStructure:
      def __init__(self, get_response):
            self.get_response = get_response


      def __call__(self,request):
            print('This part will be Executed Before the views is Called')
            response = self.get_response(request)
            print('This part will be Executed After the views is Called')
            return response



                 


