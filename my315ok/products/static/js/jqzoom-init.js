require([
  'jquery','jqzoom'
], function($,jqzoom) {
  'use strict';
   $(document).ready(function(){ 
       var options3 =
                 {
        zoomWidth: 400,
        zoomHeight: 350,
        yOffset: -10,
        title: false,
        lens:false
                  };
       $(".jqzoom").jqzoom(options3);
      });
      }
);