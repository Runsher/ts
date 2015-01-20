<script>
        var imgUrl = "图片地址";
        var lineLink = "网址";
        var descContent = '爱在五月，\n\n妈咪爱1+1亲子健康之旅开启全国行首站----重庆站妈咪爱活性益生菌';
        var shareTitle = '标题';
        var appid = '';
        function shareFriend() {
            WeixinJSBridge.invoke('sendAppMessage',{
                "appid": appid,
                "img_url": imgUrl,
                "img_width": "200",
                "img_height": "200",
                "link": lineLink,
                "desc": descContent,
                "title": shareTitle
            }, function(res) {
                //_report('send_msg', res.err_msg);
                       })
              }
        function shareTimeline() {
            WeixinJSBridge.invoke('shareTimeline',{
                "img_url": imgUrl,
                "img_width": "200",
                "img_height": "200",
                "link": lineLink,
                "desc": descContent,
                "title": shareTitle
            }, function(res) {
            });
        }
        function shareWeibo() {
            WeixinJSBridge.invoke('shareWeibo',{
                "content": descContent,
                "url": lineLink,
            }, function(res) {

          });
        }
        document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
            WeixinJSBridge.on('menu:share:appmessage', function(argv){
                shareFriend();
            });
            WeixinJSBridge.on('menu:share:timeline', function(argv){
                shareTimeline();
            });
            WeixinJSBridge.on('menu:share:weibo', function(argv){
                shareWeibo();
            });
        }, false);
</script>

