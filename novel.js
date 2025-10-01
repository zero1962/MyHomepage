function	DomToolkit()
{
	if(document.all) {
		// IE4/IE5
		this.getLayer = function(id) {
			return document.all[id];
		};
		this.setLayerVisibility = function(layer, f) {
			layer.style.visibility = (f ? "visible" : "hidden");
		};
	}
	else if(document.getElementById) {
		// NN6
		this.getLayer = function(id) {
			return document.getElementById(id);
		};
		this.setLayerVisibility = function(layer, f) {
			layer.style.visibility = (f ? "visible" : "hidden");
		};
	}
	else {
		// NN4
		this.getLayer = function(id) {
			var	i = arguments.length - 1;
			var	layer = document.layers[arguments[i--]];
			while(i >= 0 && layer) {
				layer = layer.layers[arguments[i--]];
			}
			return layer;
		};
		this.setLayerVisibility = function(layer, f) {
			layer.visibility = (f ? "show" : "hide");
		};
	}
}


var		page = 0;		// �y�[�W�ԍ�
var		sect = 0;		// �i���ԍ�
var		eos = false;	// �V�[���I���t���O
var		lastpage;		// �ŏI�y�[�W�ԍ�
var		domtool;		// DOM�ˑ��̃c�[��
var		timerid;
var		masked = false;

function	init()
{
	domtool = new DomToolkit();
	
	if(document.layers) {
		// NN4
		window.captureEvents(Event.CLICK);
		window.onclick = showNext;
	}
	
	for(lastpage = 0 ; getParaLayer(lastpage, 0) ; ++lastpage);
	--lastpage;
	
	timerid = setTimeout("setMask()", 500);
}

function	setMask()
{
	clearTimeout(timerid);
	domtool.setLayerVisibility(domtool.getLayer("mask0"), true);
	masked = true;
	showNext();
}

function	getParaLayer(page, sect)
{
	var	pageid = "page" + page;
	var	sectid = "p" + page + "_" + sect;
	
	return domtool.getLayer(sectid, pageid);
}

function	showNext()
{
	if(!masked || eos) return;
	
	layer = getParaLayer(page, sect);
	if(!layer) {
		// ���s�y�[�W���\��
		for(var i = 0 ; i < sect ; ++i) {
			domtool.setLayerVisibility(getParaLayer(page, i), false);
		}
		++page;
		sect = 0;
		layer = getParaLayer(page, sect);
	}
	domtool.setLayerVisibility(layer, true);
	++sect;
	
	// �V�[���̏I��
	if(page == lastpage && !getParaLayer(page, sect)) {
		domtool.setLayerVisibility(domtool.getLayer("cover0"), false);
		eos = true;
	}
}
