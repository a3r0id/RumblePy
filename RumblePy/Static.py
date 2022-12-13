class Static:
    
    class Request:
        
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
       
        def base_headers():
            return {
                "User-Agent": Static.Request.user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "deflate, utf-8",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache"
            }
    
    class URI:
        service = "https://rumble.com/service.php"
        base    = "https://rumble.com"