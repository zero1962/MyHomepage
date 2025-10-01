//
//  デジタル時計付　スライドショー
//

var n;
var interval = 5;// 表示間隔（秒）
var pn       =70;// 画像の数


function slideshow(){
      n=Math.floor(Math.random() * pn);
      img3.src = "./jpg/"+ n + ".jpg";
      setTimeout( "slideshow()",interval*1000);
}

function picchange(){
      n++;
            if( n > pn ){
                  n=0
            };
      img3.src = "./jpg/"+ n + ".jpg";
}


function speedup(){
            interval --;
            if( interval < 0 ) {
                interval = 0;
            }
}

function speeddown(){
            interval ++;
}

function checknum(nn){
      if(nn > pn)
      {
            alert("そんなに多く画像がありません。");
            return(ture);
      }
      else
      {
            return(false);
      }
}

function Realtime() {
dd = new Date();
//year = dd.getYear(); if (year < 2000) year += 1900;
//mon = dd.getMonth() + 1; if (mon < 10) mon = "0" + mon;
//date = dd.getDate(); if (date < 10) date = "0" + date;
hour = dd.getHours(); if (hour < 10) hour = "0" + hour;
min = dd.getMinutes(); if (min < 10) min = "0" + min;
sec = dd.getSeconds(); if (sec < 10) sec = "0" + sec;
//document.form1.text1.value =
document.getElementById("tokei").innerHTML=
"画像No."+ n +" 表示間隔=" +interval+ "(s)  "+
//year + "/" + mon + "/" + date + 
"      " +
hour + ":" + min + ":" + sec;
setTimeout("Realtime()", 1000);
}

//