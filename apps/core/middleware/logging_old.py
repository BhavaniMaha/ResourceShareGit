from typing import Any
from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from apps.core.logging import Logging


logging = Logging(str(settings.BASE_DIR / "logs" / "req_res_logs.txt"))
def simple_logging_middleware(get_response):
    def middleware(request):
        # TO DO: pre-processing
        print('pre-processing happening here')
        #breakpoint()
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content-Type']
        user_agent = request.headers['User-Agent']
        
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logging.info(msg)
        
        response = get_response(request)
        
        headers = response.headers
        status_code = response.status_code
        
        msg = f"{status_code} | {headers}"
        logging.info(msg)
        
        # TO DO: post-processing
        # TO DO: Investigate the response and decide on what to log
        # TO DO: Formulate your msg
        # TO DO: log the msg using the info level method
        print('post-processing happening here')
        
        return response
    
    return middleware

class ViewExecutionTimeMiddleware:
    
        def __init__(self, get_response):
             self.get_response = get_response
             
        def __call__(self,request):
            # pre-processing
            # start timer
             start_time = timezone.now()
             
             response = self.get_response(request)
             
             total_time = timezone.now() - start_time
             http_method = request.method
             url = request.get_full_path()
             host_port = request.get_host()
             
             msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
             
             # set a limit for the time my views should take to execute
             # compare total time
             logging.info(msg)
             return response
             
             

class ViewExecutionTime2Middleware(MiddlewareMixin):
    
        def process_request(self, request):
            request.start_time = timezone.now()
            
        def process_response(self, request, response):
            total_time = timezone.now() - request.start_time
            http_method = request.method
            url = request.get_full_path()
            host_port = request.get_host()
             
            msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
            logging.info(msg)
            
            return response
            