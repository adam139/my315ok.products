require([
  'jquery','jqlightbox'
], function($,box) {
	$('a.lightbox').lightBox(
{
	overlayBgColor: '#FFF',
	overlayOpacity: 0.6,
	imageLoading: 'http://images.315ok.org/images/lightbox-ico-loading.gif',
	imageBtnClose: 'http://images.315ok.org/images/lightbox-btn-close.gif',
	imageBtnPrev: 'http://images.315ok.org/images/lightbox-btn-prev.gif',
	imageBtnNext: 'http://images.315ok.org/images/lightbox-btn-next.gif',
	containerResizeSpeed: 350,
	txtImage: '图片',
	txtOf: '总共'	
   }	
	); 
});