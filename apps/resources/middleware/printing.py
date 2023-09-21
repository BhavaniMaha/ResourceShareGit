def printing_middleware(get_response):
    def middleware(request):
        # pre-processing takes place here
        print("pre-processing takes place here")
        response = get_response(request)
        
        #post-processing
        print("post-processing takes place here")
        return response
    return middleware
        