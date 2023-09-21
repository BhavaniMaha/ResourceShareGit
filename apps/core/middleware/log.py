import logging

#Get logging insatnce
logger = logging.getLogger('logging_mw') # __name__

def simple_logging_middleware(get_response):
    def middleware(request):
        # TO DO: pre-processing
        #print('pre-processing happening here')
        #breakpoint()
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content-Type']
        user_agent = request.headers['User-Agent']
        
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logger.info(msg)
        
        response = get_response(request)
        
        # headers = response.headers
        # status_code = response.status_code
        
        # msg = f"{status_code} | {headers}"
        # logger.info(msg)
        
        # TO DO: post-processing
        # TO DO: Investigate the response and decide on what to log
        # TO DO: Formulate your msg
        # TO DO: log the msg using the info level method
        #print('post-processing happening here')
        
        return response
    
    return middleware